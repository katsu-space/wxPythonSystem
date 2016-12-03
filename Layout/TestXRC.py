#!/usr/bin/env python
#-*- coding:utf-8 -*-

import wx
from wx import xrc

class MyApp(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource("gui.xrc")
        self.init_frame()
        return True
    
    def init_frame(self):
        self.frame = self.res.LoadFrame(None, "myFrame")
        self.frame.Show()

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()