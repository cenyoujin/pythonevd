#!/usr/bin/env python
import MySQLdb

def dblook(dbname,tbname):
    cxn = MySQLdb.Connect(user='root',passwd='123456',db=dbname)
    cur = cxn.cursor()
    cur.execute('SELECT * FROM %s' % tbname)
    for data in cur.fetchall():
        print '%s' % data
    cur.close()
    cxn.commit()
    cxn.close()

if __name__ == '__main__':
    dbname=raw_input('please input the dbname:')
    tbname=raw_input('please input the tbname:')
    dblook(dbname,tbname)
