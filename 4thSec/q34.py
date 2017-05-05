#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 34.py

from q30 import tabbed_str_to_dict
import ngram
from pprint import pprint
# https://pythonhosted.org/ngram/

def ngramed_list(lst: list, n: int = 3) -> list:
    """
    listをNグラムにする
    :param lst Nグラムするリスト
    :param n Nグラム defaultは3
    :return Nグラム化済のリスト
    """
    # https://pythonhosted.org/ngram/ngram.html?highlight=ngram#ngram.NGram
    # https://pythonhosted.org/ngram/tutorial.html#multi-byte-characters
    index = ngram.NGram(N=n)
    return [term for term in index.ngrams(lst)]

def is_noun_no_noun(words: list) -> bool:
    """
    3つの単語からなるリストが「名詞-の-名詞」になっているかの判定
    :param words 3つの単語からなるリスト
    :return bool
    """
    return  (type(words) == list) and (len(words) == 3) and \
            (words[0]['pos1'].find('名詞') == 0) and \
            (words[1]['surface'] == 'の') and \
            (words[2]['pos1'].find('名詞') == 0)

with open('neko.txt.mecab', encoding='utf-8') as f:
    morphemes = [tabbed_str_to_dict(line) for line in f]

noun_no_noun = [ngrams for ngrams in ngramed_list(morphemes) if is_noun_no_noun(ngrams)]
#print(noun_no_noun[::100])

result = [''.join([word['surface'] for word in ngram]) for ngram in noun_no_noun]
#print(result[::100])

pprint('morphemes[0:5]')
pprint(morphemes[0:5])
pprint('ngramed_list(morphemes)[0:5]')
pprint(ngramed_list(morphemes)[0:5])
pprint('noun_no_noun[0:5]')
pprint(noun_no_noun[0:5])
pprint('result[0:5]')
pprint(result[0:5])
