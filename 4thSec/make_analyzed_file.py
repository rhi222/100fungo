#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MeCab

# Type hints
# https://docs.python.jp/3/whatsnew/3.5.html#pep-484-type-hints
# http://qiita.com/icoxfog417/items/c17eb042f4735b7924a3
def make_analyzed_file(input_file_name: str, output_file_name: str) -> None:
    _m = MeCab.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    # Ochasen 出力フォーマット指定
    # http://d.hatena.ne.jp/Kshi_Kshi/20110102/1293920002
    with open(input_file_name, encoding='utf-8') as input_file:
        with open(output_file_name, mode='w', encoding='utf-8') as output_file:
            output_file.write(_m.parse(input_file.read()))
            # https://openbook4.me/projects/147/sections/885

make_analyzed_file('neko.txt', 'neko.txt.mecab')

