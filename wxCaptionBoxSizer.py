#!/usr/bin/env python
#coding: utf-8


import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"フレーム・パネル", size=(300, 200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#FAFAFA")

button_1 = wx.Button(panel, wx.ID_ANY, u"ボタン１")
button_2 = wx.Button(panel, wx.ID_ANY, u"ボタン2")
button_3 = wx.Button(panel, wx.ID_ANY, u"ボタン3")

box = wx.StaticBox(panel, wx.ID_ANY, u"python-izm.com")

layout = wx.StaticBoxSizer(box, wx.HORIZONTAL)
layout.Add(button_1)
layout.Add(button_2)
layout.Add(button_3)

panel.SetSizer(layout)

frame.Show()
application.MainLoop()


