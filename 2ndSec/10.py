#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 10.py

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
print(len(lines))

