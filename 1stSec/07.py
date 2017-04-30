#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 07.py

def template(x, y, z):
    return u"{x}時の{y}は{z}".format(x=x, y=y, z=z)

x = 12
y = u'気温'
z = 33.54

print(template(x, y, z))
