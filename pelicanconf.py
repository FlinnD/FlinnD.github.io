#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Flinn Dolman'
SITENAME = u'Toucan Machine Learning Blog'
SITEURL = 'http://FlinnD.github.io'
IGNORE_FILES = ['.ipynb_checkpoints']
PATH = 'content'
THEME = "./themes/new-bootstrap2"
#THEME = "./themes/minimalX"
TIMEZONE = 'GB'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (
          ('Social Link Here!', '#'),)

DEFAULT_PAGINATION = 10


MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
