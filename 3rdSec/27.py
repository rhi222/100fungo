#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 27.py

def remove_markup(text):
    # remove emphasis
    text = re.sub(r"'{2,5}", r"", text)
    # remove link
    text = re.sub(r"\[{2}([^\]]+?\|)*(.*?)\]{2}", r"\2", text)
    # remove br
    text = re.sub(r"<br\s?/>", r"", text)
    return text

import re
from mymodule import extract_from_json

temp_dict = {}
lines = re.split(r'\n[\|}]', extract_from_json(u'イギリス'))

for line in lines:
    temp_line = re.search('^(.*?)\s=\s(.*)$', line, re.S)
    if temp_line is not None:
        temp_dict[temp_line.group(1)] = remove_markup(temp_line.group(2))

for k, v in sorted(temp_dict.items(), key=lambda x: x[1]):
    print(k, v)
