#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 33.py

from q30 import tabbed_str_to_dict

with open('neko.txt.mecab', encoding='utf-8') as f:
    morphemes = [tabbed_str_to_dict(line) for line in f]

# list内表記 if後置
# http://qiita.com/y__sama/items/a2c458de97c4aa5a98e7#if%E3%82%92%E5%90%AB%E3%82%80%E5%A0%B4%E5%90%88%E5%BE%8C%E7%BD%AEif
nouns_sahen = [morpheme['surface'] for morpheme in  morphemes if morpheme['pos1'] == '名詞-サ変接続']

print(nouns_sahen[::100])
