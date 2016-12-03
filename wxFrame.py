#!/usr/bin/env python
#coding: utf-8


import wx

application = wx.App()
#フレーム作成
frame = wx.Frame(None, wx.ID_ANY, u"フレーム")
frame.SetBackgroundColour("#000000")
#タイトルバーのアイコン設定（タイトルバーにアイコンが表示されない場合は無視される？）
icon = wx.Icon("./img/favicon.ico", wx.BITMAP_TYPE_ICO)
frame.SetIcon(icon)
frame.CreateStatusBar()
frame.SetStatusText(u"ステータスバー文字列")
frame.Show()

application.MainLoop()


