#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import wx
import fnmatch

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        # パネルを生成し、上記で生成したフレームの中に格納
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.panel.SetBackgroundColour("#AFAFAF")

        # リストボックスを生成し、上記で生成したパネルの中に格納
        self.listbox = wx.ListBox(self.panel, wx.ID_ANY)
        self.btnOK = wx.Button(self.panel, wx.ID_ANY)
        self.btnOK.Label = "OK"
        self.btnCANCEL = wx.Button(self.panel, wx.ID_ANY)
        self.btnCANCEL.Label = "Cancel"

        self.layout = wx.BoxSizer(wx.VERTICAL)
        #self.layout.Add(self.listbox, proportion=1)
        self.layout.Add(self.listbox, flag=wx.GROW | wx.ALL, border=10)
        self.layout.Add(self.btnOK, proportion=1)
        self.layout.Add(self.btnCANCEL, proportion=1)

        self.panel.SetSizer(self.layout)
        self.Show()

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
    frame = MainWindow(None, "Application Title")

    # 検索対象 拡張子を指定
    strEXT = ".iso"
    for file in fild_all_files('/mnt/movies'):
        
        path, ext = os.path.splitext(file)
        if ext.upper() == strEXT.upper():
            frame.listbox.Append(file)

    #layout = wx.GridSizer(1, 1)
    #layout.Add(listbox, flag=wx.GROW | wx.ALL, border=10)

    #panel.SetSizer(layout)
    #frame.Show()

    application.MainLoop()

if __name__ == '__main__':
    main()