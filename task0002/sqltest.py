#!/usr/bin/env python
#coding=utf-8
import MySQLdb
conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'test',
    charset='utf8')
cur = conn.cursor()

cur.close()
conn.close()
