from glob import glob
from os.path import expanduser
from sqlite3 import connect
from pycookiecheat import chrome_cookies

import requests
import requests.utils

from instaloader import ConnectionException, Instaloader

instaloader = Instaloader(max_connection_attempts=1)
session = requests.Session()
#copy session cookies from browser if there
session.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1',
                    'ig_vw': '1920', 'csrftoken': '',
                    's_network': '', 'ds_user_id': ''})

instaloader.context._session.cookies.update(session.cookies)

                                                     
try:
    username = instaloader.test_login()
    if not username:
        raise ConnectionException()
except ConnectionException:
    raise SystemExit("Cookie import failed. Are you logged in successfully in Firefox?")

instaloader.context.username = username
instaloader.save_session_to_file()