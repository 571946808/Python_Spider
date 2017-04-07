#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import my_db
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 页面数据输出模块：将抓取的信息以utf-8格式输出

class HtmlOutputerTemplate(object):

    def __init__(self):
        self.MyDb = my_db.MyDb()
        self.sql = ""
        if self.MyDb.exit_of_table('template'):
            self.template = 'template'
        else:
            self.template = 'template_copy'

    def output_html(self):
        self.sql = "SELECT * from "+ self.template
        results = self.MyDb.execute_db(self.sql)
        list = []
        for row in results:
            item = {}
            item['img'] = row[0]
            item['url'] = row[1]
            item['text'] = row[2]
            list.append(item)

        return list
