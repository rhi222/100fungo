#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 18.py

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in sorted(lines, key = lambda x: x.split()[2], reverse = True):
    print(line, end = "")
