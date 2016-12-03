#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from wx import xrc 

XRC_FILE = "xrced_sampleHINA.xrc"                                         # xrcedから出力された *.xrc リソースファイル

class SampleApp(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource(XRC_FILE)
        self.init_frame()
        return True

    def init_frame(self):                                               # フレーム（ウィンドウ）作成
        self.MainForm = self.res.LoadFrame(None, "MainFrame")           # リソースファイルからフレームを生成
        self.MainForm.SetSize((400, 100))                               # フレーム（ウィンドウ）のサイズ変更
        self.tcText = xrc.XRCCTRL(self.MainForm, "tcText")              # リソースファイルからテキストボックスを生成
        self.btnChange = xrc.XRCCTRL(self.MainForm, "btnChange")        # リソースファイルからボタンを生成
        self.btnChange.Bind(wx.EVT_BUTTON, self.btnChange_Click)        # ボタンクリック用 イベントハンドラ紐付け
        self.MainForm.Show()                                            # フレーム（ウィンドウ）表示

    def btnChange_Click(self, event):                                   # ボタンクリック用 イベントハンドラ実装部
        self.MainForm.SetTitle(self.tcText.GetValue())                  # ウィンドウのタイトルを tcText に記述された文字列に変更する
        self.tcText.SetValue("")                                        # 


'''
#####################################################################
    xrcedで作成したリソースファイルの使い方
    リソースファイルを読み込む
    wx.Appからクラスを継承し、その中で
        １．フレームの作成
        ２．コントロールの生成
        ３．イベントハンドラ紐付け
        ４．フレーム（ウィンドウ）の表示

        ５．イベントハンドラ 実装
        　イベント処理記述

    #################################################################
    #!/usr/bin/local/python
    # -*- coding: utf-8 -*-
    #実行用 Pyファイル xrced_sample02_main.py

    import wx
    import xrced_sample02

    if __name__ == "__main__":
        app = xrced_sample02.SampleApp(False)
        app.MainLoop()
    #################################################################

#####################################################################
'''