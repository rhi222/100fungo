#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 03.py

CONTEXT = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
arrange_context = CONTEXT.replace('.', '').replace(',', '')
ary_context = arrange_context.split()
list = []

for word in ary_context:
    list.append(len(word))

print(list)
