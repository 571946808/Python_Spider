#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import my_db
import globalVal

# 页面数据输出模块：将抓取的信息以utf-8格式输出

class CreateDB(object):
    def __init__(self):
        self.MyDb = my_db.MyDb()
        self.sql_empty_job = ""
        self.sql_empty_template = ""
        if self.MyDb.exit_of_table('job'):
            globalVal.TABLE_0 = 'job_copy'
            globalVal.TABLE_1 = 'template_copy'
            globalVal.TABLE_2 = 'job'
            globalVal.TABLE_3 = 'template'
        else:
            globalVal.TABLE_0 = 'job'
            globalVal.TABLE_1 = 'template'
            globalVal.TABLE_2 = 'job_copy'
            globalVal.TABLE_3 = 'template_copy'

    def create_db(self):
        self.MyDb.create_table_job(globalVal.TABLE_0, globalVal.TABLE_1)

class EmptyDB(object):

    def __init__(self):
        self.MyDb = my_db.MyDb()
        self.sql_empty_job = ""
        self.sql_empty_template = ""

    def empty_db(self):
        self.sql_empty_job = "DROP TABLE " + globalVal.TABLE_2
        self.sql_empty_template = "DROP TABLE " + globalVal.TABLE_3
        print self.sql_empty_job
        print self.sql_empty_template
        self.MyDb.execute_db(self.sql_empty_job)
        self.MyDb.execute_db(self.sql_empty_template)

class LagouDB(object):

    def __init__(self):
        self.datas = []
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def lagou_db(self, datas):
        for data in datas:
            self.sql = "INSERT INTO " + globalVal.TABLE_0 + "(position, company, salary, location, url, link, rule, other, school, description) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (data['position'], data['company'], data['salary'], data['location'], data['url'], data['link'], data['rule'], data['other'], data['school'], data['description'])
            print self.sql
            self.MyDb.execute_db(self.sql)

class LiepinDB(object):

    def __init__(self):
        self.datas = []
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def liepin_db(self, datas):
        for data in datas:
            self.sql = "INSERT INTO " + globalVal.TABLE_0 + "(position, company, salary, location, url, link, rule, other, description, school) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (data['position'], data['company'], data['salary'], data['location'], data['url'], data['link'], data['rule'], data['other'], data['description'], data['school'])
            print self.sql
            self.MyDb.execute_db(self.sql)

class GanjiDB(object):

    def __init__(self):
        self.datas = []
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def ganji_db(self, datas):
        for data in datas:
            self.sql = "INSERT INTO " + globalVal.TABLE_0 + "(position, company, salary, location, url, link, rule, other, school, description) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (data['position'], data['company'], data['salary'], data['location'], data['url'], data['link'], data['rule'], data['other'], data['school'], data['description'])
            print self.sql
            self.MyDb.execute_db(self.sql)

class Job51DB(object):

    def __init__(self):
        self.datas = []
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def job51_db(self, datas):
        for data in datas:
            self.sql = "INSERT INTO " + globalVal.TABLE_0 + "(position, company, salary, location, url, link, rule, other, school, description) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (data['position'], data['company'], data['salary'], data['location'], data['url'], data['link'], data['rule'], data['other'], data['school'], data['description'])
            print self.sql
            self.MyDb.execute_db(self.sql)

class YingcaiDB(object):

    def __init__(self):
        self.datas = []
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def yingcai_db(self, datas):
        for data in datas:
            self.sql = "INSERT INTO " + globalVal.TABLE_0 + "(position, company, salary, location, url, link, rule, other, school, description) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (data['position'], data['company'], data['salary'], data['location'], data['url'], data['link'], data['rule'], data['other'], data['school'], data['description'])
            print self.sql
            self.MyDb.execute_db(self.sql)

class ZhilianDB(object):

    def __init__(self):
        self.datas = []
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def zhilian_db(self, datas):
        for data in datas:
            self.sql = "INSERT INTO " + globalVal.TABLE_0 + "(position, company, salary, location, url, link, rule, other, school, description) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (data['position'], data['company'], data['salary'], data['location'], data['url'], data['link'], data['rule'], data['other'], data['school'], data['description'])
            print self.sql
            self.MyDb.execute_db(self.sql)

class JiaobuDB(object):

    def __init__(self):
        self.datas = []
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def jiaobu_db(self, datas):
        for data in datas:
            self.sql = "INSERT INTO " + globalVal.TABLE_1 + "(url, img, text, source) VALUES ('%s','%s','%s','%s')" % (data['url'], data['img'], data['text'], data['source'])
            print self.sql
            self.MyDb.execute_db(self.sql)

class GerenjianliDB(object):

    def __init__(self):
        self.datas = []
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def gerenjianli_db(self, datas):
        for data in datas:
            self.sql = "INSERT INTO " + globalVal.TABLE_1 + "(url, img, text, source) VALUES ('%s','%s','%s','%s')" % (data['url'], data['img'], data['text'], data['source'])
            print self.sql
            self.MyDb.execute_db(self.sql)

class WubaidingDB(object):

    def __init__(self):
        self.datas = []
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def wubaiding_db(self, datas):
        for data in datas:
            self.sql = "INSERT INTO " + globalVal.TABLE_1 + "(url, img, text, source) VALUES ('%s','%s','%s','%s')" % (data['url'], data['img'], data['text'], data['source'])
            print self.sql
            self.MyDb.execute_db(self.sql)


