#!/usr/bin/env python
#-*- coding:utf-8 -*-

import wx
import xrced_sample02_xrc

__frame = None

if __name__ == "__main__":
    app = wx.App(False)
    __frame = xrced_sample02_xrc.xrcMainFrame(None)
    app.SetTopWindow(__frame)
    __frame.Show()
    app.MainLoop()