#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os # osモジュールのインポート
import wx
 
# os.listdir('パス')
# 指定したパス内の全てのファイルとディレクトリを要素とするリストを返す
#files = os.listdir("\\homeserver1\movies\'")
files = os.listdir("Z:\MUSICS")

application = wx.App()

frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300,200))
panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")
listbox = wx.ListBox(panel, wx.ID_ANY)

for file in files:
    listbox.Append(file)

layout = wx.GridSizer(1, 1)
layout.Add(listbox, flag=wx.GROW | wx.ALL, border=10)
 
panel.SetSizer(layout)
 
frame.Show()
application.MainLoop()

"""
element_array = ("element_1", "element_2", "element_4", "element_3", "element_5")
#listbox = wx.ListBox(panel, wx.ID_ANY, choices=element_array)
listbox = wx.ListBox(panel, wx.ID_ANY, choices=element_array, style=wx.LB_SINGLE)
 """
