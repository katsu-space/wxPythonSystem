#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()


# ジェネレーターを使った方法
def iterparent(root):
    for parent in root.getiterator():
        for child in parent:
            yield parent, child


for p, c in iterparent(root):
    print c.tag + ":" + p.tag

# (child, parent)形式のマップを生成する方法
parent_map = dict((c, p) for p in tree.getiterator() for c in p)
for k in parent_map.keys():
    print k.tag + ":" + parent_map.get(k).tag
