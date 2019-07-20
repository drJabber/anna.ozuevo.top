import os 
import os.path as path
import shutil
import time
import re
import json
from pelican import signals


import logging
logger = logging.getLogger(__name__)

try:
#import libraries here
    enabled = True
except ImportError:
    logging.warning("Unable to load libraries, disabling pelican-extra")
    enabled = False

DEFAULT_OUTPUT_PATH = "output"
DEFAULT_INPUT_PATH='content/static'

def process_extra_directories(pelican):
    """ copies extra static directories to output folder
    """
    input_dir=path.join('.',
        pelican.settings.get("PATH", DEFAULT_INPUT_PATH)).rstrip('/')

    output_dir=path.join('.',
        pelican.settings.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)).rstrip('/')
    static_dirs=pelican.settings.get("STATIC_PATHS", [])
    extra_dirs=pelican.settings.get("EXTRA_DIRECTORIES", {})

    for static_dir in static_dirs:
        items=list(filter(lambda item : item[0].startswith(static_dir+'/'), extra_dirs.items()))
        for item in items:
            output_path=path.join(output_dir,item[1]['path'])
            input_path=path.join(input_dir,item[0])
            logger.debug('pelican_extra - input: '+input_path+', output: '+output_path)
            os.makedirs(output_path, exist_ok=True) 
            for dirpath, _, filenames in os.walk(input_path): 
                for filename in filenames:
                    logger.debug('pelican_extra - input: '+filename)
                    shutil.copy(path.join(input_path,filename),output_path)


def register():
    signals.get_generators.connect(process_extra_directories)
    
