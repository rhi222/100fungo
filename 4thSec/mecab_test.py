#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://qiita.com/taroc/items/b9afd914432da08dafc8
import MeCab

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = '10日放送の「中居正広のミになる図書館」（テレビ朝日系）で、SMAPの中居正広が、篠原信一の過去の勘違いを明かす一幕があった。'
mecab.parse('')
node = mecab.parseToNode(text)
while node:
    # 単語を取得
    word = node.surface
    # 品詞を取得
    pos = node.feature.split(',')[1]
    print('{0}, {1}'.format(word, pos))
    node = node.next
