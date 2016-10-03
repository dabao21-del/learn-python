#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.Connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        db = 'test',
        charset = 'utf8'
        )

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data =cursor.fetchone()

print "Database version : %s " % data

cursor.close()
db.close()
