# coding: utf-8
# Here your code !

import os
import fnmatch

strEXT = ".iso"

def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def main():
    for file in fild_all_files('/mnt/movies'):
        path, ext = os.path.splitext(file)
        if ext.upper() == strEXT.upper():
            #ここで配列に格納する
            print file

if __name__ == '__main__':
    main()