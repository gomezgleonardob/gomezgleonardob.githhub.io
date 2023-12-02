#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Leonardo'
SITENAME = u'Blog'
SITEURL = 'https://gomezgleonardo.xyz'

PATH = 'content'

TIMEZONE = 'America/Guayaquil'

DEFAULT_LANG = u'es-es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


HEADER_COVER = f'images/background.jpg'
SITESUBTITLE = 'Blog'
CSS_OVERRIDE = (
    f'{SITEURL}/static/css/custom.css',
)


# Menu
MENUITEMS = (('Inicio', SITEURL),)
# Blogroll


# Social widget


STATIC_PATHS = [
    'static',
    'images',
]

EXTRA_PATH_METADATA = {
    'static/favicon.png': {'path': 'favicon.png'},
    'static/CNAME': {'path': 'CNAME'},
}

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme - pelican-blue
THEME = 'themes/pelican-sober'



# URLs
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{lang}/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{lang}/{slug}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{lang}/{slug}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{lang}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{lang}/{slug}.html'
PAGE_LANG_SAVE_AS = 'pages/{lang}/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}.html'
YEAR_ARCHIVE_URL = 'posts/{date:%Y}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}.html'
MONTH_ARCHIVE_URL = 'posts/{date:%Y}/{date:%m}.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}.html'
DAY_ARCHIVE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}.html'
DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}.html'


PLUGINS = [
    # ...
    # ...
]
