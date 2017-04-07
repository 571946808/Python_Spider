#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import my_db
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 页面数据输出模块：将抓取的信息以utf-8格式输出

class HtmlOutputerBbs(object):

    def __init__(self):
        self.MyDb = my_db.MyDb()
        self.sql = ""

    def output_html(self):
        self.sql = "SELECT * from bbs ORDER BY id DESC"
        results = self.MyDb.execute_db(self.sql)
        list = []
        for row in results:
            item = {}
            item['title'] = row[0]
            item['comment'] = row[1]
            item['id'] = row[2]
            list.append(item)

        return list
