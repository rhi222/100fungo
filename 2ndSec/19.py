#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 19.py

import sys
from collections import defaultdict

filename = sys.argv[1]
prefectures = defaultdict(int)

with open(filename) as f:
    line = f.readline()
    while line:
        prefectures[line.split()[0]] += 1
        line = f.readline()

for k, v in sorted(prefectures.items(), key=lambda x: x[1], reverse=True):
    print(k)
