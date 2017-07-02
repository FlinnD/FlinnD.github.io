#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Flinn Dolman'
SITENAME = u'Toucan Machine Learning Blog'
SITEURL = 'http://FlinnD.github.io'
#SITEURL = ''
IGNORE_FILES = ['.ipynb_checkpoints']
PATH = 'content'
#THEME = "./themes/w3-personal-blog"
THEME = "./themes/elegant"
TIMEZONE = 'GB'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

COMMENTS_INTRO = 'cheese'
SITE_LICENSE = 'string'
SITE_DESCRIPTION = 'A Data Science Portfolio by Flinn Dolman'
SITESUBTITLE = 'A Data Science Portfolio'
LANDING_PAGE_ABOUT = dict = {'title': 'My Data Science Portfolio', 'details': 'My name is Flinn Dolman. I am a current UCL student studying an Msc in Computational Finance. Herein lies a record of projects I have undertaken and topics that interest me pertaining to Machine Learning.'}
PROJECTS = [{
    'name': 'Performing PCA on Wildfire Data ',
    'url': 'http://FlinnD.github.io/PCA_Wildfire',
    'description': 'My first post. It details how I performed PCA on wildfire data in Python'
    ''}, ]


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )


# Social widget
SOCIAL = (
          ('Linkedin', 'http://www.linkedin.com/in/flinn-dolman-277564145/'),
          ('GitHub', 'http://www.github.com/FlinnD'), )

DEFAULT_PAGINATION = 10


MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup','sitemap','extract_toc', 'tipue_search']

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


