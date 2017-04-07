#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import my_db
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 页面数据输出模块：将抓取的信息以utf-8格式输出

class HtmlOutputerAdd(object):

    def __init__(self):
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def output_html_insert(self, title, comment):
        self.sql = "INSERT INTO bbs(title, comment) VALUES ('%s','%s')" %(title, comment)

        results = self.MyDb.execute_db(self.sql)

    def output_html_delete(self, order):
        for item in order:
            self.sql = "DELETE from bbs WHERE id = '%s'" %item
            #print self.sql

            self.MyDb.execute_db(self.sql)