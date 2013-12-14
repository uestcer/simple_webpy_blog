#!/usr/bin/env python
#-*- coding: utf-8 -*-


from controllers.index import Index
from config.setting import app
from config.url import urls
from controllers.init import init_list
from controllers.init import blog_posts

import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)

import web

if __name__ == "__main__":
    init_list()
    app.wsgifunc()
