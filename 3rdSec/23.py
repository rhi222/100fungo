#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 23.py

import re
from mymodule import extract_from_json

lines = extract_from_json(u'イギリス').split('\n')

for line in lines:
    #section_line = re.search("^=== (.*) ===$", line)
    section_line = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
    if section_line is not None:
        print(section_line.group(2), len(section_line.group(1)) - 1)
