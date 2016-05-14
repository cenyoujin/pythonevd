#!/usr/bin/env python

import string,random,MySQLdb

def ran_creat(num,length):
    f = open('rc.txt','wb')
    for i in range(num):
        s = string.letters + string.digits
        rc = [random.choice(s) for i in range(length)]
        f.write(''.join(rc)+'\n')
    f.close()

def store_mySQL(filepath):
    conn = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = '123456',
        db = 'test',
    )
    cursor = conn.cursor()
    cursor.execute('create table if not exists random (con char(36))')
    with open(filepath,'r') as f:
        keys = f.readlines()
        for key in keys:
            cursor.execute("insert into random VALUES('%s')"%str(key.strip()))
    cursor.close()
    conn.commit()
    conn.close()
    f.close()


if __name__ == '__main__':
    ran_creat(200,6)
    store_mySQL('rc.txt')

