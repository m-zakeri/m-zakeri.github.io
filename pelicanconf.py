#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Morteza'
SITENAME = 'Morteza Zakeri'
SITEURL = ''
SITETITLE = SITENAME
SITESUBTITLE = 'PhD in Computer Science'
# SITEDESCRIPTION = 'Iran University of Science and Technology'

# PYGMENTS_STYLE = 'monokai'

PATH = 'content'

# Copyright
COPYRIGHT_YEAR = '2016 - ' + str(datetime.now().year)
COPYRIGHT_NAME = SITENAME + '. All rights reserved.'
"""CC_LICENSE = {
    'name': 'All rights reserved.',
    'version': '2.1',
    'slug': 'Morteza Zakeri-Nasrabadi'
}"""

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

INDEX_SAVE_AS = 'blog_index.html'
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives']

MENUITEMS = (
    ('Blog', '/category/blog.html'),
    ('Research', '/pages/research.html'),
    ('Resources', '/pages/resources.html'),
    ('Courses', '/category/courses.html'),
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
    ('Sitemap', '/sitemap.xml')
)

LINKS = (
    # ('Courses', 'https://m-zakeri.github.io/category/courses.html'),
    ('Laboratory', 'http://reverse.iust.ac.ir'),
    # ('Micropedia', 'http://micropedia.ir'),
    ('University page', 'http://webpages.iust.ac.ir/morteza_zakeri/')
)

# Social widget
GITHUB_URL = 'https://github.com/m-zakeri/'
TWITTER_USERNAME = '_zakeri_'

SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/mortazazakeri/'),
    ('twitter', 'https://twitter.com/_zakeri_'),
    ('github', 'https://github.com/m-zakeri/'),
    # ('github', 'https://github.com/mortazazakeri/'),
    ('rss', '/feeds/all.atom.xml'),
)

DEFAULT_PAGINATION = 5

THEME = 'Flex'

STATIC_PATHS = ['static/img/', 'static/pdf/', 'static/css/']

CUSTOM_CSS = '/static/css/custom.css'
FAVICON = '/static/img/favicon.ico'
SITELOGO = '/static/img/profile.png'

PLUGIN_PATHS = ['D:\AnacondaProjects\pelican-addon-clones\pelican-plugins']
# PLUGINS = ['neighbors']
# PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']
# PLUGINS = ["disqus_static", "sitemap"]
PLUGINS = ['sitemap', 'tipue_search.tipue_search']

DISQUS_SITENAME = 'http://m-zakeri.github.io'
DISQUS_SECRET_KEY = 'npvZaCi9OxTTK0bhCiZhWJqRWG47e51YCozCyO0JcVwGXRTX2OIHx9Cc4R5FETeZ'
DISQUS_PUBLIC_KEY = 'mu9aEsQaD6JNZFSYr3xeLZxyyV79byzZDov5TtQTHQzPV0qjmaogBoYdDOUD0Qem'

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
