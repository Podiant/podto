#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from baseconf import *
from collections import OrderedDict

SITENAME = u'podTo'
SITESUBTITLE = u'The campaign for an easier way to subscribe to podcasts'
AUTHOR = u'podTo'
THEME = 'themes/clean-blog'

GITHUB_REPO = 'http://github.com/podiant/podto'
GITHUB_BRANCH = 'pelican'

ARTICLE_BANNERS_FOLDER = 'images/banners'
SITE_LOGO = 'images/logo.png'
SITE_LOGO_MOBILE = 'images/logo-mobile.png'

WELCOME_TITLE = 'Welcome to {}'.format(SITENAME)
WELCOME_TEXT = 'Something about podTo'
SITE_BACKGROUND_IMAGE = 'images/banners/background.png'
FOOTER_ABOUT = 'This is footer info'

PYGMENTS_STYLE = 'perldoc'
NAVBAR_HOME_LINKS = []

# Navbar Links do Blog
NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        'title': 'Categorias',
        'href': 'blog/categorias'
    },
    {
        'title': 'Authors',
        'href': 'blog/authors'
    },
    {
        'title': 'Tags',
        'href': 'blog/tags'
    }
]

SOCIAL = (
    ('github', 'https://github.com/podiant'),
)
