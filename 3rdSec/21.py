#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 21.py

import json

from mymodule import extract_from_json

lines = extract_from_json(u'イギリス').split('\n')

for line in lines:
    if 'Category' in line:
        print(line)
