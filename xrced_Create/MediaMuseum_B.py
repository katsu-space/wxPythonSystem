#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx
from wx import xrc 

XRC_FILE = os.path.dirname(__file__) + "/MediaMuseum_B.xrc"

class SampleApp(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource(XRC_FILE)
        self.init_frame()
        return True

    def init_frame(self):
        self.MainForm = self.res.LoadFrame(None, "Frame1")
        self.spwMain = xrc.XRCCTRL(self.MainForm, "spwMain")
        self.spwRight = xrc.XRCCTRL(self.MainForm, "spwRight")
        self.ListBox = xrc.XRCCTRL(self.spwMain, "lbListBox")
        self.TextBox = xrc.XRCCTRL(self.MainForm, "tbTextBox")
        self.btnOK = xrc.XRCCTRL(self.MainForm, "btnOK")
        self.btnCancel = xrc.XRCCTRL(self.MainForm, "btnCancel")
        self.btnConfig = xrc.XRCCTRL(self.MainForm, "btnConfig")
        self.StatusBar = xrc.XRCCTRL(self.MainForm, "StatusBar1")
        self.TextBox.Value = str(self.spwRight.GetSashSize())
        self.MainForm.Show()

        # Event
        self.btnOK.Bind(wx.EVT_BUTTON, self.btnOK_Click)
        self.btnCancel.Bind(wx.EVT_BUTTON, self.btnCancel_Click)
        self.btnConfig.Bind(wx.EVT_BUTTON, self.btnConfig_Click)
        self.ListBox.Bind(wx.EVT_LISTBOX, self.ListBox_Change)


        # Setting
        self.MainForm.SetTitle("Hey mySample01")
        self.MainForm.SetSize((600, 500))
        self.spwRight.SetSashSize(5)

    def fild_all_files(self, directory):                                # 再帰処理でルートフォルダとそれ以下のフォルダ内を検索
        for root, dirs, files in os.walk(directory):
            yield root
            for file in files:
                yield os.path.join(root, file)

    # event Procedure
    def ItemAdd(self, val):
        for file in self.fild_all_files('/mnt/movies'):  # 検索ヒットしたファイルの拡張子が検索対象拡張子かどうかをチェック
            path, ext = os.path.splitext(file)  #
            if ext.upper() == str(val).upper():
                self.ListBox.Append(file)  #

    def btnOK_Click(self, event):
        self.ListBox.Clear()
        strEXT = [".mp4", ".iso", ".ils"]  # 検索対象拡張子指定
        map(self.ItemAdd, strEXT)

    def btnCancel_Click(self, event):
        print ("Cancel Click!")
        wx.Exit()

    def btnConfig_Click(self, event):
        print (str(self.ListBox.GetSelection() + 1) + "/" + str(self.ListBox.GetCount()))# + ": " + self.ListBox.Get)
        event.Skip()

    def ListBox_Change(self, event):
        self.TextBox.Value = str(self.ListBox.GetSelection() + 1) + "/" + str(self.ListBox.GetCount())
        #obj = event.GetEventObject()
        #self.TextBox.Value = obj.GetClientData(obj.GetSelection())

if __name__ == "__main__":
    app = SampleApp(False)
    app.MainLoop()