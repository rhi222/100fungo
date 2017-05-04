#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 16.py

import sys

def split_file(filename, parts_num):
    with open(filename) as f:
        lines = f.readlines()

    if len(lines) % int(parts_num) != 0:
        raise Exception('Undividable by N={x}'.format(x = parts_num))
    else:
        line_num = len(lines) / int(parts_num)

    for i in range(int(parts_num)):
        with open('split{i}.txt'.format(i = str(i)), 'w') as w:
            w.writelines(lines[int(line_num) * i: int(line_num) * (i + 1)])


if __name__ == '__main__':
    try:
        split_file(sys.argv[1], sys.argv[2])
    except Exception as err:
        print('Error', err)

