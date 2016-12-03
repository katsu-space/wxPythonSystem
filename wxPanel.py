#!/usr/bin/env python
#coding: utf-8


import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"フレーム・パネル", size=(300, 300))
frame.SetBackgroundColour("#000000")

r_panel = wx.Panel(frame, wx.ID_ANY, pos = (0, 0), size=(80, 300))
r_panel.SetBackgroundColour("#FF0000")

g_panel = wx.Panel(frame, wx.ID_ANY, pos = (80, 0), size=(80, 300))
g_panel.SetBackgroundColour("#00FF00")

b_panel = wx.Panel(frame, wx.ID_ANY, pos = (160, 0), size=(80, 300))
b_panel.SetBackgroundColour("#0000FF")
#icon = wx.Icon("./img/favicon.ico", wx.BITMAP_TYPE_ICO)
#frame.SetIcon(icon)
frame.Show()

application.MainLoop()


