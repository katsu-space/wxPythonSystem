#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

connector = MySQLdb.connect(host="localhost", db="SampleDB040", user="user1", passwd="pw", charset="utf8")
cursor = connector.cursor()
#str_1 = 'T03Town'
str_1 = 'T02City'
#str_2 = "select * from " + str_1 + " where CITY_CD < %s and PREF_CD = %s"
str_2 = """
    select
        CITY_CD, PREF_CD, CITY_NAME
    from
        %s
    where
        CITY_CD > %s and PREF_CD > %s
    ;
"""
cursor.execute(str_2, ("T02City", 1200, 10))

result = cursor.fetchall()

for row in result:
    print ("===== Hit! =====")
    #print(row)
    print ("CITY_CD -- " + str(row[0]))
    print ("PREF_CD -- " + str(row[1]))
    print ("CITY_NAME -- " + row[2] + "\n")

cursor.close()
connector.close()
