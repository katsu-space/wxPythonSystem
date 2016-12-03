#!/usr/bin/env python
#coding: utf-8

import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, u"フレーム・パネル", size=(570, 200))

icon = wx.Icon("./img/favicon.ico", wx.BITMAP_TYPE_ICO)
frame.SetIcon(icon)
panel = wx.Panel(frame, wx.ID_ANY, size=(100, 100))
panel.SetBackgroundColour("#FF0000")

button_1 = wx.Button(panel, wx.ID_ANY, u"ボタン１", size = (80, 30))
button_2 = wx.Button(panel, wx.ID_ANY, u"ボタン2", size = (80, 30))
button_3 = wx.Button(panel, wx.ID_ANY, u"ボタン3", size = (80, 30))
button_4 = wx.Button(panel, wx.ID_ANY, u"ボタン4", size = (80, 30))
button_5 = wx.Button(panel, wx.ID_ANY, u"ボタン5", size = (80, 30))
button_6 = wx.Button(panel, wx.ID_ANY, u"ボタン6", size = (80, 30))
button_7 = wx.Button(panel, wx.ID_ANY, u"ボタン7", size = (80, 30))

layout = wx.BoxSizer(wx.HORIZONTAL)
layout.Add(button_1, flag = wx.GROW)
layout.Add(button_2, flag = wx.SHAPED)
layout.Add(button_3, flag = wx.SHAPED | wx.ALIGN_TOP)
layout.Add(button_4, flag = wx.SHAPED | wx.ALIGN_BOTTOM)
layout.Add(button_5, flag = wx.SHAPED | wx.ALIGN_CENTER)
layout.Add(button_6, flag = wx.SHAPED | wx.ALIGN_LEFT)
layout.Add(button_7, flag = wx.SHAPED | wx.ALIGN_RIGHT)

panel.SetSizer(layout)

frame.Show()
application.MainLoop()


