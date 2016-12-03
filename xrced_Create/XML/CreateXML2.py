#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
import xml.dom.minidom
import codecs
# DOM 実装を取得
impl = xml.dom.minidom.getDOMImplementation()
# 「top」というルートノードをもつドキュメントを作成
doc = impl.createDocument(None, 'top', None)
# 最上位のエレメントを取得
top_element = doc.documentElement
# 「node1」というエレメントを作成
node1 = doc.createElement('node1')
# 「node1」のテキストノード作成
node1_text = doc.createTextNode(u'node1のテキスト')
# 作成したテキストノードを設定
node1.appendChild(node1_text)
# 「node1_attr」というアトリビュート作成
node1_attr = doc.createAttribute("node1_attr")
node1_attr.value = u'node1のアトリビュート'
# 作成したアトリビュートを設定
node1.setAttributeNode(node1_attr)
# ルートノードに、作成したnode1を設定
top_element.appendChild(node1)
# 文字列にして表示
print(doc.toxml('UTF-8'))
# ファイルに保存
f = codecs.open('sample.xml', 'w', 'utf-8')
doc.writexml(writer=f, encoding='UTF-8', newl='\n', addindent='\t')
f.close()