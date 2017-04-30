#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 08.py
import re

def cipher(text):
    return re.sub(r'[a-z]', lambda m: chr(219 - ord(m.group(0))), text)

sample = 'my birthday is 222'
encrypt = cipher(sample)
decrypt = cipher(encrypt)

print(encrypt)
print(decrypt)
