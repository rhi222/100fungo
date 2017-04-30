#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 09.py
import random

def rearrange(word):
    # 文字数の分岐
    if len(word) >= 5:
        # 最初の文字と最後の文字を取り出す [start, mid, end]
        head = word[0]
        last = word[-1]
        body = word[1:-1]

        # midに対してrandom処理
        # 結合
        ret = head + "".join(random.sample(body, len(body))) + last
    else:
        ret = word
    return ret

def genTypoglycemia(sentence):
    return ' '.join(map(rearrange, sentence.split(' ')))

plaintext = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(genTypoglycemia(plaintext))
