#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 37.py

from q30 import tabbed_str_to_dict
from q36 import get_frequency
from pprint import pprint
from collections import defaultdict
# https://docs.python.jp/3/library/collections.html#collections.defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np


if __name__ == '__main__':
    with open('neko.txt.mecab', encoding='utf-8') as f:
        morphemes = [tabbed_str_to_dict(line) for line in f]
    frequency = get_frequency([morpheme['surface'] for morpheme in morphemes])
    frequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
    fig = plt.figure(figsize=(10, 6))
    words = [f[0] for f in frequency[0:10]]
    x_pos = np.arange(len(words))
    fp = FontProperties(fname=r'/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', size=14)
    ax1 = fig.add_subplot(131)
    ax1.bar(x_pos, [f[1] for f in frequency[0:10]], align='center', alpha=0.4)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(words, fontproperties=fp)
    ax1.set_ylabel('Frequency')
    ax1.set_title('Top 10 frequent words')
