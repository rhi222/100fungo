#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 29.py

import re
import requests
import json
from mymodule import extract_from_json

def json_search(json_data):
    ret_dict = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(json_search(e))
        elif isinstance(v, dict):
            ret_dict.update(json_search(v))
        else:
            ret_dict[k] = v
    return ret_dict


def remove_markup(text):
    # remove emphasis
    text = re.sub(r"'{2,5}", r"", text)
    # remove internal link
    text = re.sub(r"\[{2}([^\]]+?\|)*(.*?)\]{2}", r"\2", text)
    # remove br
    text = re.sub(r"<br\s?/>", r"", text)
    # remove external link
    text = re.sub(r"\[(http|https).*?\]", r"", text)
    # remove html
    text = re.sub(r"<.*?>", r"", text)
    return text

temp_dict = {}
lines = re.split(r'\n[\|}]', extract_from_json(u'イギリス'))

for line in lines:
    temp_line = re.search('^(.*?)\s=\s(.*)$', line, re.S)
    if temp_line is not None:
        temp_dict[temp_line.group(1)] = remove_markup(temp_line.group(2))

#for k, v in sorted(temp_dict.items(), key=lambda x: x[1]):
#    print(k, v)

print(temp_dict[u'国旗画像'])
url = "https://en.wikipedia.org/w/api.php"
payload = { 'action': 'query',
            'titles': 'File:{}'.format(temp_dict[u'国旗画像']),
            'prop': 'imageinfo',
            'format': 'json',
            'iiprop': 'url'}

#json_data = requests.get(url, params=payload).content
json_data = requests.get(url, params=payload).json()

# check json data
print(json_data)
print(json.dumps(json_data, sort_keys=True, indent=2))
print(json_data.items())


# search url
print(json_search(json_data))
print(json_search(json_data)['url'])
