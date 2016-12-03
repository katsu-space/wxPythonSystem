#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import wx
import wx_utils
from wx_utils import XRC, XRCID, XRCCTRL

import main_icon

class MainFrame(wx.Frame):
  u"""MainFrame class deffinition.
  """
  RESOURCE_ID = 'MainFrame'
  #MENUBAR_ID = 'MainMenubar'
  binder = wx_utils.bind_manager(RESOURCE_ID)

  def __init__(self, parent=None):
    pre = wx.PreFrame()
    XRC().LoadOnFrame(pre, parent, self.RESOURCE_ID)
    self.PostCreate(pre)
    #self.SetMenuBar(XRC().LoadMenuBar(self.MENUBAR_ID))
    self.binder.bindall(self, self.RESOURCE_ID)
    self.SetIcon(main_icon.getIcon())

  @binder(wx.EVT_BUTTON, id=XRCID('ID_BIG_BUTTON'))
  def OnMenuAbout(self, event):
    wx.SafeShowMessage(u'情報', 'BIG Button Pressed!')

# startup application.
if __name__=='__main__':
  app = wx.App(False)
  wx_utils.XrcInit()
  frame = MainFrame()
  app.SetTopWindow(frame)
  frame.Show()
  app.MainLoop()