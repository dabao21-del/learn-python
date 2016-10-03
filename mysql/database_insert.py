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
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()
