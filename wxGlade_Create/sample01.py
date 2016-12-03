#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import wx import xrc

XRC_FILE = "sample01.xrc"

class SampleApp(wx.App):
    self.res = xrc.XmlResource(XRC_FILE)
    self.init_frame()
    return True

    def init_frame(self):
        self.frm_main = self.res.LoadFrame(None, "frame_main")
        self.frm_main.SetTitle("")
        self.frm_main.SetSize(400, 300)
        self.frm_main.Show()

