#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 10.py

import sys

f = open(sys.argv[1])
lines = f.readlines()
print(len(lines))

f.close
