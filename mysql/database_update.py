#!/usr/bin/pyton
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

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()
