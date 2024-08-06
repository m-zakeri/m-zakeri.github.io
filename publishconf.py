#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

sys.path.append(os.curdir)

try:
    from pelicanconf import *
except ImportError:
    sys.path.append(os.path.join(os.curdir, "content"))
    from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://m-zakeri.github.io'
RELATIVE_URLS = True
# USE_LESS = False


# PLUGIN_PATHS = ['D:\AnacondaProjects\pelican-addon-clones\pelican-plugins']
# PLUGINS = ['neighbors']
# PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']
# PLUGINS = ["disqus_static", "sitemap"]
# PLUGINS = ['sitemap', 'pelican-readtime']
# PLUGINS = ['tipue_search.tipue_search']



FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
# DISQUS_SITENAME = 'http://m-zakeri.github.io'
DISQUS_SITENAME = "zakeri"
# DISQUS_SECRET_KEY = 'npvZaCi9OxTTK0bhCiZhWJqRWG47e51YCozCyO0JcVwGXRTX2OIHx9Cc4R5FETeZ'
# DISQUS_PUBLIC_KEY = 'mu9aEsQaD6JNZFSYr3xeLZxyyV79byzZDov5TtQTHQzPV0qjmaogBoYdDOUD0Qem'

# GOOGLE_ANALYTICS = ""

# Pelican-search Configuration
STORK_INPUT_OPTIONS = {"stemming": "English", "url_prefix": SITEURL}
