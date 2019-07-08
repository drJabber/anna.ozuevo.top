import os 
import os.path as path
import fnmatch
import shutil
import time
import re
import json
from pelican import signals
from jsonpath_rw import jsonpath
import jsonpath_rw_ext as jp


import logging
logger = logging.getLogger(__name__)

try:
#import libraries here
    enabled = True
except ImportError:
    logging.warning("Unable to load libraries, disabling pelican-gram")
    enabled = False

DEFAULT_INSTAGRAM_DATA_DIR = "data"
DEFAULT_MARKDOWN_DIR='blog'
DEFAULT_IMAGES_DIR='blog/images'
DEFAULT_INSTAGRAM_CATEGORY='Instagram'
DEFAULT_INSTAGRAM_MEDIA_PATTERNS=['*.jpg', '*.mp4']

class _processor(object):
    def __init__(self,pelican,in_path):
        self.in_path=in_path
        self.out_path = path.join(pelican.settings['PATH'],
                            pelican.settings.get('PELIGRAM_OUTPUT_MARKDOWN_DIR', DEFAULT_MARKDOWN_DIR))
        self.img_path = path.join(pelican.settings['PATH'],
                            pelican.settings.get('PELIGRAM_OUTPUT_IMAGES_DIR', DEFAULT_IMAGES_DIR))
        self.category=pelican.settings.get("PELIGRAM_CATEGORY", DEFAULT_INSTAGRAM_CATEGORY)                   

    def extract_tags(post_text,post_tags):
        pattern=re.compile(r'#(\w+)')
        for match in pattern.finditer(post_text):
            post_tags+=[match]

    def make_tag_link(self,match):
        tag=match.group()
        return "["+tag.replace('#','')+"]({tag}"+tag.replace('#','')+")"
        # return "|category|Instagram"

    def make_post(self, filename, media_filenames):
        logger.debug("create post for "+filename)

        with open(path.join(self.in_path,filename),'r') as jf:
            json_data=json.load(jf) 

        if json_data:
            logger.debug("get metadata for "+filename)

            post_text=''
            tags_text=''
            post_tags=[]
            json_result=jp.match('$.node.__typename',json_data)
            if json_result:
                json_result=jp.match('$.node.edge_media_to_caption.edges[0].node.text',json_data)
                if json_result:
                    post_text=json_result[0]
                    pattern=re.compile('#(\w+)')
                    post_tags=re.findall(pattern,post_text)
                    post_text=re.sub(pattern,self.make_tag_link,post_text)
                    tags_text=', '.join(list(map(lambda match : match.replace('#',''),post_tags)))

                post_date=''
                json_result=jp.match('$.node.taken_at_timestamp',json_data)
                if json_result:
                    post_date=time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(json_result[0]))

                post_slug=''
                json_result=jp.match('$.node.shortcode',json_data)
                if json_result:
                    post_slug=json_result[0]

                post_meta={'Title':'', 'Date':post_date, 'Slug':post_slug, 'Category':self.category, 'Tags':tags_text}
                post_data=''.join(f'{x}:{y}\n' for (x,y) in post_meta.items())+post_text+'\n'
                

                for fn in media_filenames:    
                    ext=path.splitext(fn)[-1].lower()
                    if ext=='.jpg':
                        md_tags=post_data+'![instagram]({attach}images/'+fn+')\n'
                    elif ext=='.mp4':
                        md_tags='[video]\n[download.mp4]({attach}images/'+fn+')\n[size](800,600)'
                    else:
                        md_tags=''        

                post_data=post_data+md_tags

                with open(path.join(self.out_path,path.splitext(filename)[0]+'.markdown'),'w+') as md:
                    md.write(post_data)   

                return True    
            else: 
                return False        
        else:
            return False        

    def copy_media(self, filename, media_filenames):
        logger.debug("\tmedia filenames: "+', '.join(media_filenames))
        for fn in media_filenames:
            logger.debug("\t\tcopying media "+fn)
            shutil.copy(path.join(self.in_path,fn), path.join(self.img_path,fn))

    def process_instagram_metadata(self, filename, media_filenames):
        if self.make_post(filename,media_filenames):
            self.copy_media(filename,media_filenames)


def generate_markdown(pelican):
    """ generate markdown from folder where instagram posts were downloaded

    :param pelican: The pelican instance
    :return: None
    """
    global enabled
    if not enabled:
        return

    include_regex = pelican.settings.get('PELIGRAM_INCLUDE_REGEX')
    media_patterns=pelican.settings.get("PELIGRAM_MEDIA_PATTERNS", DEFAULT_INSTAGRAM_MEDIA_PATTERNS)

    if include_regex:
        pattern = re.compile(include_regex)
        is_included = lambda name: pattern.match(name)
    else:
        is_included = lambda name: not name.startswith('.')

    in_path = instagram_data_path(pelican)
    logger.debug("pelican-gram started")
    processor=_processor(pelican,in_path)
    for dirpath, _, filenames in os.walk(in_path):
        for filename in filenames:
            if is_included(filename):
                if filename.endswith('.json'):
                    logger.debug(f"Processing file: {filename}")
                    media_filenames=sum(list(map(lambda pattern: fnmatch.filter(filenames,path.splitext(filename)[0]+pattern),media_patterns)),[])
                    processor.process_instagram_metadata(filename,media_filenames)



def instagram_data_path(pelican):
    return path.join('.',
        pelican.settings.get("INSTAGRAM_DATA_PATH", DEFAULT_INSTAGRAM_DATA_DIR)).rstrip('/')


def register():
    signals.get_generators.connect(generate_markdown)
    
