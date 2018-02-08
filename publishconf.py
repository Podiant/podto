#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *

SITEURL = 'https://podto.org'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'blog/feeds.atom'
FEED_ALL_RSS = 'blog/feeds.rss'

DELETE_OUTPUT_DIRECTORY = True

GOOGLE_ANALYTICS = 'UA-113787178-2'
