#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 39.py

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
    freq = list(dict(frequency).values())
    freq.sort(reverse=True)
    rank = list(range(1, len(freq) + 1))

    ax3 = fig.add_subplot(133)
    ax3.plot(freq, rank)
    ax3.set_xlabel('Rank')
    ax3.set_ylabel('Frequency')
    ax3.set_title('Zipf low')
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    fig.savefig('morphological_analysis.png')
    plt.show()
