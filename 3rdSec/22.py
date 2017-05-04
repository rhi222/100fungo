#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 22.py

import json
import re
from mymodule import extract_from_json

lines = extract_from_json(u'イギリス').split('\n')

for line in lines:
    category_line = re.search("\[\[Category:(.*)\]\]", line)
    if category_line is not None:
        print(category_line.group(1))
