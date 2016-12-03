#!/usr/bin/env python
#-*- coding:utf-8 -*-

import codecs
from smb.SMBConnection import SMBConnection

def findFile(userID, password, client_machine_name, server_name, domain, server_ip):
#def findFile():
    """
    userID = 'katsu'
    password = 'katsuopen'
    client_machine_name = 'debian'
    server_name = 'homeserver1'
    domain = ''
    server_ip = '192.168.1.1'
    #server_ip = 'homeserver1'
    """
    #接続設定を指定し、コネクションオープン
    conn = SMBConnection(userID, password, client_machine_name, server_name, domain = '', use_ntlm_v2 = True)
    conn.connect(server_ip, 139)

    filelist = conn.listPath('movies', '/')             # Moviesフォルダ内のリスト
    #filelist = conn.listPath('workall', '/')             # Moviesフォルダ内のリスト
    #filelist = conn.listPath('field_a', '/')
    #filelist = conn.listPath('Movies', u'/星守る犬')#, "*.*")
    
    for f in filelist:
        print(f.filename)
    
    conn.close()

if __name__ == '__main__':
    #findFile()
    userID = 'katsu'
    password = 'katsuopen'
    client_machine_name = 'debian'
    server_name = 'homeserver1'
    domain = ''
    server_ip = '192.168.1.1'
    findFile(userID, password, client_machine_name, server_name, domain, server_ip)
