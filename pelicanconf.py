#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Morteza'
SITENAME = 'Morteza ZAKERI'
SITEURL = ''
SITETITLE = SITENAME
SITESUBTITLE = 'Ph.D. Student, Computer Engineering'
#SITEDESCRIPTION = 'Iran University of Science and Technology'

THEME = 'Flex'

#PYGMENTS_STYLE = 'monokai'

PATH = 'content'

# Copyrigth

"""CC_LICENSE = {
    'name': 'All rights reserved.',
    'version': '1.0',
    'slug': 'Morteza ZAKERI'
}"""
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.now().year

# Time and date
TIMEZONE = 'Asia/Tehran'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TYPOGRIFY = True

# Blogroll
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True
HOME_HIDE_TAGS = False

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
			('Categories', '/categories.html'),
            ('Tags', '/tags.html'),
			 ('Sitemap', '/sitemap.xml'),
			 )

LINKS = (('Our Laboratory', 'http://parsa.iust.ac.ir/reverse-engineering-lab/'),
         ('Our Micropedia', 'http://micropedia.ir'),
         ('My University Page', 'http://webpages.iust.ac.ir/morteza_zakeri/'),)

# Social widget
GITHUB_URL = 'https://github.com/m-zakeri/'
TWITTER_USERNAME = '_zakeri_'
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/mortazazakeri/'),
          ('twitter', 'https://twitter.com/_zakeri_'),
		  ('github', 'https://github.com/m-zakeri/'),
		  ('github', 'https://github.com/mortazazakeri/'),
		  ('rss', '/feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['_img', '_pdf', '_css']

FAVICON = '_img/favicon.ico'
#SITELOGO = '_img/profile.png'
CUSTOM_CSS = '_css/custom.css'


PLUGIN_PATHS = ['D:\AnacondaProjects\pelican-addon-clones\pelican-plugins']
#PLUGINS = ['neighbors']
#PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False