#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

# 爬虫调度端
import html_downloader, handle_db, html_parser
import url_core
from threading import Thread
from threading import Timer
import time

class CreateDBThread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self):
        Thread.__init__(self)
        self.outputer = handle_db.CreateDB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        self.outputer.create_db()

class EmptyDBThread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self):
        Thread.__init__(self)
        self.outputer = handle_db.EmptyDB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        self.outputer.empty_db()

class LagouThread(Thread):
    
    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self, lagou_url):
        Thread.__init__(self)
        self.lagou_url = lagou_url
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.LagouHtmlParser()
        self.outputer = handle_db.LagouDB()
    
    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        lagou_url = self.lagou_url
        for item in lagou_url:
            html_cont = self.downloader.download(item)
            new_data = self.parser.parse(item, html_cont)
            self.outputer.lagou_db(new_data)

class LiepinThread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self, liepin_spider):
        Thread.__init__(self)
        self.liepin_spider = liepin_spider
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.LiepinHtmlParser()
        self.outputer = handle_db.LiepinDB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        liepin_spider = self.liepin_spider
        for item in liepin_spider:
            html_cont = self.downloader.download(item)
            new_data = self.parser.parse(item, html_cont)
            self.outputer.liepin_db(new_data)

class GanjiThread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self, ganji_spider):
        Thread.__init__(self)
        self.ganji_spider = ganji_spider
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.GanjiHtmlParser()
        self.outputer = handle_db.GanjiDB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        ganji_spider = self.ganji_spider
        for item in ganji_spider:
            html_cont = self.downloader.download(item)
            new_data = self.parser.parse(item, html_cont)
            self.outputer.ganji_db(new_data)

class Job51Thread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self, job51_spider):
        Thread.__init__(self)
        self.job51_spider = job51_spider
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.Job51HtmlParser()
        self.outputer = handle_db.Job51DB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        job51_spider = self.job51_spider
        for item in job51_spider:
            html_cont = self.downloader.download(item)
            new_data = self.parser.parse(item, html_cont)
            self.outputer.job51_db(new_data)

class YingcaiThread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self, yingcai_spider):
        Thread.__init__(self)
        self.yingcai_spider = yingcai_spider
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.YingcaiHtmlParser()
        self.outputer = handle_db.YingcaiDB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        yingcai_spider = self.yingcai_spider
        for item in yingcai_spider:
            html_cont = self.downloader.download(item)
            new_data = self.parser.parse(item, html_cont)
            self.outputer.yingcai_db(new_data)

class ZhilianThread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self, zhilian_spider):
        Thread.__init__(self)
        self.zhilian_spider = zhilian_spider
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.ZhilianHtmlParser()
        self.outputer = handle_db.ZhilianDB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        zhilian_spider = self.zhilian_spider
        for item in zhilian_spider:
            html_cont = self.downloader.download(item)
            new_data = self.parser.parse(item, html_cont)
            self.outputer.zhilian_db(new_data)

class JiaobuThread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self, jiaobu_spider):
        Thread.__init__(self)
        self.jiaobu_spider = jiaobu_spider
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.JiaobuHtmlParser()
        self.outputer = handle_db.JiaobuDB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        jiaobu_spider = self.jiaobu_spider
        for item in jiaobu_spider:
            html_cont = self.downloader.download(item)
            new_data = self.parser.parse(item, html_cont)
            self.outputer.jiaobu_db(new_data)

class GerenjianliThread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self, gerenjianli_spider):
        Thread.__init__(self)
        self.gerenjianli_spider = gerenjianli_spider
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.GerenjianliHtmlParser()
        self.outputer = handle_db.GerenjianliDB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        gerenjianli_spider = self.gerenjianli_spider
        for item in gerenjianli_spider:
            html_cont = self.downloader.download(item)
            new_data = self.parser.parse(item, html_cont)
            self.outputer.gerenjianli_db(new_data)

class WubaidingThread(Thread):

    # 初始化html_downloader、html_parser、html_outputer四个模块
    def __init__(self, wubaiding_spider):
        Thread.__init__(self)
        self.wubaiding_spider = wubaiding_spider
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.WubaidingHtmlParser()
        self.outputer = handle_db.WubaidingDB()

    # 执行爬虫，爬取root_url下相关的链接，并输出到out_put.html
    def run(self):
        wubaiding_spider = self.wubaiding_spider
        for item in wubaiding_spider:
            html_cont = self.downloader.download(item)
            new_data = self.parser.parse(item, html_cont)
            self.outputer.wubaiding_db(new_data)

def TimerRun():

    # 初始化各个爬取网址
    lagou_url = url_core.lagou_url
    liepin_url = url_core.liepin_url
    ganji_url = url_core.ganji_url
    job51_url = url_core.job51_url
    yingcai_url = url_core.yingcai_url
    zhilian_url = url_core.zhilian_url
    jiaobu_url = url_core.jiaobu_url
    gerenjianli_url = url_core.gerenjianli_url
    wubaiding_url = url_core.wubaiding_url

    # 初始化各个线程模块
    create_spider = CreateDBThread()
    lagou_spider = LagouThread(lagou_url)
    liepin_spider = LiepinThread(liepin_url)
    ganji_spider = GanjiThread(ganji_url)
    job51_spider = Job51Thread(job51_url)
    yingcai_spider = YingcaiThread(yingcai_url)
    zhilian_spider = ZhilianThread(zhilian_url)
    jiaobu_spider = JiaobuThread(jiaobu_url)
    wubaiding_spider = WubaidingThread(wubaiding_url)
    gerenjianli_spider = GerenjianliThread(gerenjianli_url)
    empty_spider = EmptyDBThread()

    # 创建数据库与其他线程不能同时进行，其他线程需要等待数据库创建完成后才能进行
    create_spider.start()
    create_spider.join()

    lagou_spider.start()
    liepin_spider.start()
    ganji_spider.start()
    job51_spider.start()
    yingcai_spider.start()
    zhilian_spider.start()
    jiaobu_spider.start()
    gerenjianli_spider.start()
    wubaiding_spider.start()

    lagou_spider.join()
    liepin_spider.join()
    ganji_spider.join()
    job51_spider.join()
    yingcai_spider.join()
    zhilian_spider.join()
    jiaobu_spider.join()
    gerenjianli_spider.join()
    wubaiding_spider.join()

    empty_spider.start()
    empty_spider.join()

    # 创建定时器，每隔24小时爬取

    timer = Timer(1*60*60*24, TimerRun)
    timer.start()

if __name__ == "__main__":

    # 主函数调用

    start = time.clock()

    TimerRun()

    end = time.clock()
    print "read: %f s" % (end - start)
