#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import wx
import fnmatch

"""
    ####################################################
    fild_all_files(directory)
    引数 dirrectory ルートディレクトリ
    引数によってしていされたディレクトリとそれ以下のディレクトリを対象に
    ファイルとフォルダを全て検索し、その結果を返す
    ####################################################
"""
def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def main():
    application = wx.App()
    # フレーム生成
    frame = wx.Frame(None, wx.ID_ANY, u"Find form", size=(600,800))
    # パネルを生成し、上記で生成したフレームの中に格納
    panel = wx.Panel(frame, wx.ID_ANY)
    panel.SetBackgroundColour("#AFAFAF")
    # リストボックスを生成し、上記で生成したパネルの中に格納
    listbox = wx.ListBox(panel, wx.ID_ANY)

    # 検索対象 拡張子を指定
    strEXT = ".iso"
    for file in fild_all_files('/mnt/movies'):
        
        path, ext = os.path.splitext(file)
        if ext.upper() == strEXT.upper():
            listbox.Append(file)

    layout = wx.GridSizer(1, 1)
    layout.Add(listbox, flag=wx.GROW | wx.ALL, border=10)

    panel.SetSizer(layout)

    frame.Show()
    application.MainLoop()

if __name__ == '__main__':
    main()