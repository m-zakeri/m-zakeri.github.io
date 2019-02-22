#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Morteza'
SITENAME = 'Morteza ZAKERI'
SITEURL = ''

PATH = 'content'

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
LINKS = (('IUST Reverse Engineering Laboratory', 'http://parsa.iust.ac.ir/reverse-engineering-lab/'),
         ('Micropedia', 'http://micropedia.ir'),
         ('IUST Personal Page', 'http://webpages.iust.ac.ir/morteza_zakeri/'),
         ('GitHub', 'https://github.com/m-zakeri/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/mortazazakeri/'),
          ('Twitter', 'https://twitter.com/_zakeri_'),)

DEFAULT_PAGINATION = 5

THEME = 'path/to/pelican-themes/chosen-theme'
STATIC_PATHS = ['_img', '_pdf']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True