#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 36.py

from q30 import tabbed_str_to_dict
from pprint import pprint
from collections import defaultdict
# https://docs.python.jp/3/library/collections.html#collections.defaultdict

def get_frequency(words: list) -> dict:
    """
    単語のリストを受け取って、リスト中に存在する単語の頻度を求める
    :param words 単語のリスト
    :return dict key:単語, value:頻度
    """
    frequency = defaultdict(lambda: 0)
    for word in words:
        frequency[word] += 1
    return frequency

if __name__ == '__main__':
    with open('neko.txt.mecab', encoding='utf-8') as f:
        morphemes = [tabbed_str_to_dict(line) for line in f]
    frequency = get_frequency([morpheme['surface'] for morpheme in morphemes])
    sorted_frequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
    pprint(sorted_frequency[0:20])
