#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 04.py

CONTEXT = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
SINGLE_LIST = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}

def context2words(CONTEXT):
    return (CONTEXT.replace('.', ' ').replace(',', ' ')).split()

if __name__ == '__main__':
    words = context2words(CONTEXT)
    for word in words:
        clen = 1 if words.index(word) + 1 in SINGLE_LIST else 2
        dict[word[:clen]] = words.index(word) + 1
    print(dict)
