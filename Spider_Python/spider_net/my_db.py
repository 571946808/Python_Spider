#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
import MySQLdb
import re

class MyDb(object):
    def __init__(self):
        self.conn = MySQLdb.connect("localhost", "root", "root", "library")
        self.cursor = self.conn.cursor()
        self.conn.set_character_set('utf8')
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')

    def exit_of_table(self, table_name):
        sql_show_table = 'SHOW TABLES;'
        self.cursor.execute(sql_show_table)
        tables = [self.cursor.fetchall()]
        table_list = re.findall('(\'.*?\')', str(tables))
        table_list = [re.sub("'", '', each) for each in table_list]
        if table_name in table_list:
            return True
        else:
            return False

    def execute_db(self, sql):
        if sql is None:
            return
        try:
            #执行sql语句
            self.cursor.execute(sql)
            #提交到数据库执行
            self.conn.commit()
            return self.cursor.fetchall()
        except:
            # 发生错误时回滚
            self.conn.rollback()
            print '查询失败!'
        # finally:
            #self.conn.close()

    def execute_update_db(self, sql):
        if sql is None:
            return
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # 发生错误时回滚
            self.conn.rollback()

#sql = "select * from test"

#cursor.execute(sql)

#data = cursor.fetchone()

#print data

#cursor.close()

#conn.close()