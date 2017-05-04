#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 20.py

import json

with open('jawiki-country.json') as f:
    json_data = f.readline()
    while json_data:
        article_dict = json.loads(json_data)
        if article_dict['title'] == u'イギリス':
            print(article_dict['text'])
        json_data = f.readline()
