#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx
from wx import xrc 

XRC_FILE = os.path.dirname(__file__) + "/xrced_sample01.xrc"

class SampleApp(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource(XRC_FILE)
        self.init_frame()
        return True

    def init_frame(self):
        self.frm_main = self.res.LoadFrame(None, "MainFrame")
        self.frm_main.SetTitle("Hey mySample01")
        self.frm_main.SetSize((400, 300))
        self.frm_main.Show()

if __name__ == "__main__":
    app = SampleApp(False)
    app.MainLoop()