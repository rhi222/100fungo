#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 05.py

text = 'I am an NLPer'

def ngram(input, n):
    last = len(input) - n + 1
    ret = []
    for i in range(0, last):
        ret.append(input[i:i+n])
    return ret

print(ngram(text, 2))
print(ngram(text, 3))
