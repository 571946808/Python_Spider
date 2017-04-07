#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

#页面下载模块

import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        #伪造user agent
        req = urllib2.Request(url)
        req.add_header('Referer', 'http://www.sijitao.net/')
        req.add_header('User-Agent',
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")

        response = urllib2.urlopen(req)
        if response.getcode() != 200:
            return None
        return response.read()
