#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 30.py

def tabbed_str_to_dict(tabbed_str: str) -> dict:
    """
    名前    ナマエ  名前    名詞-一般
    タブ区切りの形態素を表す文字列をdict型に変換する
    :param tabbed_str タブ区切りで形態素を表す文字列
    :return dict型で表された形態素
    """
    elements = tabbed_str.split()
    if 0 < len(elements) < 4:
        return { 'surface': elements[0] # 表層形
                ,'base': '' # 基本形
                ,'pos': '' # 品詞
                ,'pos1': '' # 品詞細分類1
                }
    else:
        return { 'surface': elements[0] # 表層形
                ,'base': elements[1] # 基本形
                ,'pos': elements[2] # 品詞
                ,'pos1': elements[3] # 品詞細分類1
                }


def morphems_to_sentence(morphemes: list) -> list:
    """
    dict型で表された形態素の要素を句点ごとにグルーピングする
    :param morphems dict型で表された形態素のリスト
    :return 文章のリスト
    """
    sentences = []
    sentence = []

    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []

    return sentences

with open('neko.txt.mecab', encoding='utf-8') as f:
    # リスト内包表記
    # http://qiita.com/y__sama/items/a2c458de97c4aa5a98e7
    morphemes = [tabbed_str_to_dict(line) for line in f]

sentences = morphems_to_sentence(morphemes)

#print(morphemes[::100])
#print(sentences[::100])

