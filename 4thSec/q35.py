#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 35.py

from q30 import tabbed_str_to_dict
import ngram
from pprint import pprint
# https://pythonhosted.org/ngram/

def morphemes_to_noun_array(morphemes: list) -> list:
    """
    辞書型で表された形態素のリストを名詞もしくは句点で区切ってグルーピング
    :param morphemes 辞書型で表された形態素のリスト
    :return 名詞の連接のリスト
    """
    nouns_list = []
    nouns = []
    for morpheme in morphemes:
        if morpheme['pos1'].find('名詞') >= 0:
            nouns.append(morpheme)
        elif (morpheme['pos1'] == '記号-句点') | (morpheme['pos1'].find('名詞') < 0):
            nouns_list.append(nouns)
            nouns = []
    return [nouns for nouns in nouns_list if len(nouns) > 1]

if __name__ == '__main__':
    with open('neko.txt.mecab', encoding='utf-8') as f:
        morphemes = [tabbed_str_to_dict(line) for line in f]
    noun_array = [ ''.join([noun['surface'] for noun in nouns]) for nouns in morphemes_to_noun_array(morphemes)]
    pprint(noun_array[::100])
