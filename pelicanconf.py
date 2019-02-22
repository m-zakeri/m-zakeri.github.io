#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Morteza'
SITENAME = 'Morteza ZAKERI'
SITEURL = 'http://localhost:8000'
SITETITLE = 'Morteza ZAKERI Personal Webpage'
SITESUBTITLE = 'Ph.D. Student, Computer Engineering'
SITEDESCRIPTION = 'Iran University of Science and Technology'

PYGMENTS_STYLE = 'monokai'

PATH = 'content'

# Copyrigth
CC_LICENSE = {
    'name': 'All rights reserved.',
    'version': '1.0',
    'slug': 'Morteza ZAKERI'
}

COPYRIGHT_YEAR = datetime.now().year

# Time and date
TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TYPOGRIFY = True

# Blogroll
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

MENUITEMS = ('Home', '/index.html'),
			('Archives', '/archives.html'),
            ('Tags', '/tags.html'),)

LINKS = (('IUST Reverse Engineering Laboratory', 'http://parsa.iust.ac.ir/reverse-engineering-lab/'),
         ('Micropedia', 'http://micropedia.ir'),
         ('IUST Personal Page', 'http://webpages.iust.ac.ir/morteza_zakeri/'),
		 
		 )

# Social widget
GITHUB_URL = 'https://github.com/m-zakeri/'
TWITTER_USERNAME = '_zakeri_'
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/mortazazakeri/'),
          ('twitter', 'https://twitter.com/_zakeri_'),
		  ('github', 'https://github.com/m-zakeri/'),
		  ('github', 'https://github.com/mortazazakeri/'),
		  ('orcid', 'https://orcid.org/0000-0003-4289-0606'))

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['_img', '_pdf', '_css']
THEME = 'Flex'
FAVICON = '_img/favicon.ico'
PROFILE = '_img/morteza_zakeri_lattary600x600.png'
CUSTOM_CSS = '_css/custom.css'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True