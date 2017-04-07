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

    #查询表是否存在
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

    #创建表
    def create_table_job(self, job, template):
        try:
            #定义创建表sql语句
            create_tb_job = '''
                    CREATE TABLE IF NOT EXISTS ''' + job +'''
                    ( position VARCHAR (50),
                      company VARCHAR (50),
                      salary VARCHAR (50),
                      location VARCHAR (50),
                      id int (100) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                      rule VARCHAR (100),
                      school VARCHAR (100),
                      url VARCHAR (1000),
                      link VARCHAR (1000),
                      other VARCHAR (100),
                      description VARCHAR (100),
                      source INT (100) DEFAULT 0,
                      time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                '''
            create_tb_template = '''
                    CREATE TABLE IF NOT EXISTS ''' + template +'''
                    ( img VARCHAR (100),
                      url VARCHAR (100),
                      text VARCHAR (100),
                      id int (100) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                      source VARCHAR (100),
                      time TIMESTAMP
                    )
                '''
            #执行sql语句
            self.cursor.execute(create_tb_job)
            self.cursor.execute(create_tb_template)
            #提交到数据库执行
            self.conn.commit()
        except Exception, e:
            # 发生错误时回滚
            self.conn.rollback()
            print repr(e)
            print '创建表失败！'
            return False

    #执行插入语句
    def execute_db(self, sql):
        if sql is None:
            return
        try:
            #执行sql语句
            self.cursor.execute(sql)
            #提交到数据库执行
            self.conn.commit()
        except Exception, e:
            # 发生错误时回滚
            self.conn.rollback()
            print repr(e)
            print '插入失败！'
        # finally:
        #     # 关闭数据库连接
        #     self.conn.close()

        # #执行sql语句
        # self.cursor.execute(sql)
        # #提交到数据库执行
        # self.conn.commit()

# if __name__ == "__main__":
#     db = MyDb();
#     print db.create_table_job('job')