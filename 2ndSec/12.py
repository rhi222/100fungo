#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 12.py

import sys

def write_col(source_lines, column_number, filename):
    col = []
    for line in source_lines:
        col.append(line.split()[column_number] + "\n")
    with open(filename, "w") as writer:
        writer.writelines(col)

with open(sys.argv[1]) as f:
    lines = f.readlines()

write_col(lines, 0, "col1.txt")
write_col(lines, 1, "col2.txt")
