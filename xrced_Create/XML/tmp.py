#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from xml.etree import ElementTree

def proc():
    f = open(os.path.dirname(__file__) + "/states.xml", "r")
    #f = open("page.xml", "r")
    try:
        tree = ElementTree.parse(f)
        for s in tree:
            print s.attrib
        #for item in tree.find("states").getiterator("label"):
        #    print item.get("name")
        #    print item.findtext("name")
        #    print item.findtext("price")
    finally:
        f.close()

if __name__ == "__main__":
    proc()


