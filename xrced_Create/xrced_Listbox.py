#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wx
from wx import xrc

XRC_FILE = os.path.dirname(__file__) + "/xrced_Listbox.xrc"

class MainWindow(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource(XRC_FILE)
        self.init_frame()
        return True

    def init_frame(self):                                               # フレーム（ウィンドウ）作成
        # コントロール
        self.MainForm = self.res.LoadFrame(None, "MainFrame")           # リソースファイルからメインウィンドウ（フレーム）を生成
        self.MainForm.SetSize((400, 400))                               # メインウィンドウのサイズを設定
        self.ListBox = xrc.XRCCTRL(self.MainForm, "Listbox1")           # リストボックスを生成
        self.btnADD = xrc.XRCCTRL(self.MainForm, "btnAdd")              # ボタン（アイテム追加用）を生成
        self.btnDEL = xrc.XRCCTRL(self.MainForm, "btnDel")              # ボタン（アイテム削除用）を生成
        self.Label01 = xrc.XRCCTRL(self.MainForm, "Label1")             # ラベルを生成

        # イベント定義
        self.btnADD.Bind(wx.EVT_BUTTON, self.btnAdd_Click)              # ボタンクリック用 イベントハンドラ紐付け
        self.btnDEL.Bind(wx.EVT_BUTTON, self.btnDel_Click)              # ボタンクリック用 イベントハンドラ紐付け
        self.ListBox.Bind(wx.EVT_LISTBOX, self.ListBox_Change)          # ListBox用 イベントハンドラ紐付け
        self.MainForm.Show()                                            # フレーム（ウィンドウ）表示

    def fild_all_files(self, directory):                                # 再帰処理でルートフォルダとそれ以下のフォルダ内を検索
        for root, dirs, files in os.walk(directory):
            yield root
            for file in files:
                yield os.path.join(root, file)

    # イベント実装部
    def btnAdd_Click(self, event):                                      # ボタンクリック用 イベントハンドラ実装部
        self.ListBox.Clear()                                            # リストボックスクリア
        strEXT = ".iso"                                                 # 検索対象拡張子指定
        for file in self.fild_all_files('/mnt/movies'):                 # 検索ヒットしたファイルの拡張子が検索対象拡張子かどうかをチェック
            path, ext = os.path.splitext(file)                          #
            if ext.upper() == strEXT.upper():                           #
                self.ListBox.Append(file)                               # 検索対象拡張子ならばリストボックスに追加

    def btnDel_Click(self, event):                                      # ボタンクリック用 アイテム削除
        if self.ListBox.GetSelection() >= 0:                            # アイテムが選択されていたら
            if self.ListBox.GetSelection() == self.ListBox.GetCount() - 1:  # 選択されているアイテムが一番最後だったら
                self.ListBox.Delete(self.ListBox.GetSelection())            # 選択されているアイテムを削除
                if self.ListBox.GetCount() != 0:                            # アイテムがあれば
                    self.ListBox.SetSelection(self.ListBox.GetCount()-1)    # 一番最後のアイテムを選択
            else:                                                           # 選択されているアイテムが一番最後でなかったら
                NextIndex = self.ListBox.GetSelection()                     # 選択されている順番（番号）をNextIndexに記録
                self.ListBox.Delete(self.ListBox.GetSelection())            # 選択されているアイテムを削除
                self.ListBox.SetSelection(NextIndex)                        # 消されたアイテムの下のアイテムを選択する

            self.ListBox_Change(self)
            self.ListBox.SetFocus()                                     # ListBoxにフォーカスを当てる

    def ListBox_Change(self, event):                                   # ボタンクリック用 イベントハンドラ実装部
        self.Label01.SetLabel(str(self.ListBox.GetSelection() + 1) + "/" + str(self.ListBox.GetCount()))# + ": " + self.ListBox.Get)
        #print (str(self.ListBox.GetSelection()))


if __name__ == "__main__":
    app = MainWindow(False)
    app.MainLoop()

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

    mainファイルと分ける場合は下記の通り
    xrced_sample02_main.py
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