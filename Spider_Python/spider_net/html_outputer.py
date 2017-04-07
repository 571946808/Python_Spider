#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
import my_db
import scseg

# 页面数据输出模块：将抓取的信息以utf-8格式输出

class HtmlOutputer(object):

    def __init__(self):
        self.MyDb = my_db.MyDb()
        self.sql = ""
        self.data_list = []
        if self.MyDb.exit_of_table('job'):
            self.job = 'job'
        else:
            self.job = 'job_copy'

    def output_html(self, key, location, rule, school):
        if location == '全国':
            location = ''
        if rule == '不限':
            rule = ''
        if school == '不限':
            school = ''
        if key != '':
            i = True
            j = True
            k = True
            m = True
            n = True
            key = key.replace(' ', '')
            keywords = scseg.seg_keywords(key)
            self.sql = "SELECT DISTINCT * from "+ self.job +" where "
            print rule
            for keyword in keywords:
                #'select * from job where'+=
                if rule == '1-2年':
                    if i:
                        self.sql += "((position LIKE '%"+keyword+"%' OR company LIKE '%"+keyword+"%' OR location LIKE '%"+keyword+"%') AND location LIKE '%"+location+"%' AND (rule LIKE '%1%' OR rule LIKE '%2%') AND school LIKE '%"+school+"%')"
                        i = False
                    else:
                        self.sql += " OR ((position LIKE '%"+keyword+"%' OR company LIKE '%"+keyword+"%' OR location LIKE '%"+keyword+"%') AND location LIKE '%"+location+"%' AND (rule LIKE '%1%' OR rule LIKE '%2%') AND school LIKE '%"+school+"%')"
                elif rule == '3-5年':
                    if j:
                        self.sql += "((position LIKE '%"+keyword+"%' OR company LIKE '%"+keyword+"%' OR location LIKE '%"+keyword+"%') AND location LIKE '%"+location+"%' AND (rule LIKE '%3%' OR rule LIKE '%4%' OR rule LIKE '%5%') AND school LIKE '%"+school+"%')"
                        j = False
                    else:
                        self.sql += " OR ((position LIKE '%"+keyword+"%' OR company LIKE '%"+keyword+"%' OR location LIKE '%"+keyword+"%') AND location LIKE '%"+location+"%' AND (rule LIKE '%3%' OR rule LIKE '%4%' OR rule LIKE '%5%') AND school LIKE '%"+school+"%')"
                elif rule == '6-10年':
                    if k:
                        self.sql += "((position LIKE '%"+keyword+"%' OR company LIKE '%"+keyword+"%' OR location LIKE '%"+keyword+"%') AND location LIKE '%"+location+"%' AND (rule LIKE '%6%' OR rule LIKE '%7%' OR rule LIKE '%8%' OR rule LIKE '%9%') AND school LIKE '%"+school+"%')"
                        k = False
                    else:
                        self.sql += " OR ((position LIKE '%"+keyword+"%' OR company LIKE '%"+keyword+"%' OR location LIKE '%"+keyword+"%') AND location LIKE '%"+location+"%' AND (rule LIKE '%6%' OR rule LIKE '%7%' OR rule LIKE '%8%' OR rule LIKE '%9%') AND school LIKE '%"+school+"%')"
                elif rule == '10年以上':
                    if m:
                        self.sql += "((position LIKE '%"+keyword+"%' OR company LIKE '%"+keyword+"%' OR location LIKE '%"+keyword+"%') AND location LIKE '%"+location+"%' AND rule LIKE '%10%' AND school LIKE '%"+school+"%')"
                        m = False
                    else:
                        self.sql += " OR ((position LIKE '%"+keyword+"%' OR company LIKE '%"+keyword+"%' OR location LIKE '%"+keyword+"%') AND location LIKE '%"+location+"%' AND rule LIKE '%10%' AND school LIKE '%"+school+"%')"
                else:
                    if n:
                        self.sql += "((position LIKE '%" + keyword + "%' OR company LIKE '%" + keyword + "%' OR location LIKE '%" + keyword + "%') AND location LIKE '%" + location + "%' AND rule LIKE '%" + rule + "%' AND school LIKE '%" + school + "%')"
                        n = False
                    else:
                        self.sql += " OR ((position LIKE '%" + keyword + "%' OR company LIKE '%" + keyword + "%' OR location LIKE '%" + keyword + "%') AND location LIKE '%" + location + "%' AND rule LIKE '%" + rule + "%' AND school LIKE '%" + school + "%')"
        else:
            self.sql = "SELECT * from " + self.job + " where (position LIKE '%" + key + "%' OR company LIKE '%" + key + "%' OR location LIKE '%" + key + "%') AND location LIKE '%" + location + "%' AND rule LIKE '%" + rule + "%' AND school LIKE '%" + school + "%'"
        self.sql += " ORDER BY source DESC"
        print self.sql
        results = self.MyDb.execute_db(self.sql)
        for row in results:
            item = {}
            item['position'] = row[0]
            item['company'] = row[1]
            item['salary'] = row[2]
            item['location'] = row[3]
            item['id'] = row[4]
            item['rule'] = row[5]
            item['school'] = row[6]
            item['url'] = row[7]
            item['link'] = row[8]
            item['other'] = row[9]
            item['description'] = row[10]
            item['source'] = row[11]
            self.data_list.append(item)
            self.MyDb.execute_update_db("UPDATE " + self.job + " SET source = source + 1 WHERE id = '%s'" % item['id'])

        return self.data_list
