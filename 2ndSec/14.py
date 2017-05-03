#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 14.py

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

for line in lines [:int(sys.argv[2])]:
    print(line, end="")

