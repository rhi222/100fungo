#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 13.py

with open("col1.txt") as f1, open("col2.txt") as f2:
    lines1, lines2 = f1.readlines(), f2.readlines()

with open("merge.txt", "w") as writer:
    for col1, col2 in zip(lines1, lines2):
        writer.write("\t".join([col1.rstrip(), col2]))
