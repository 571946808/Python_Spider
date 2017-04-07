#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

# 页面解析模块：产生新的URL链接，获取词条名称和信息

from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class LagouHtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        print soup.original_encoding
        new_data = self._get_new_data(soup)
        return new_data
    
    # 本地方法获取数据：company, salary, location的信息
    def _get_new_data(self, soup):
        data = []
        items = soup.find_all('li', class_="con_list_item")

        for item in items:
            res_data = {}
            res_data['url'] = item.find('a')['href']
            res_data['position'] = item.find('h2').get_text()
            res_data['link'] = item.find('div', class_="company_name").find('a')['href']
            res_data['company'] = item.find('div', class_="company_name").find('a').get_text()
            salary = item.find('span', class_="money")
            res_data['salary'] = salary.get_text()
            salary.extract()
            res_data['location'] = item.find('span', class_="add").find('em').get_text().strip()
            res_data['rule'] = item.find('div', class_="p_bot").get_text().split('/')[0].strip()
            res_data['school'] = item.find('div', class_="p_bot").get_text().split('/')[1].strip()
            res_data['other'] = item.find('div', class_="li_b_r").get_text().replace('“', '').replace('”', '')
            res_data['description'] = item.find('div', class_="industry").get_text().strip()
            # res_data['source'] = '拉勾网'
            data.append(res_data)

        print data
        return data

class LiepinHtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        print soup.original_encoding
        new_data = self._get_new_data(soup)
        return new_data

    # 本地方法获取数据：company, salary, location的信息
    def _get_new_data(self, soup):
        data = []
        items = soup.find('ul', class_="sojob-list").find_all('li')

        for item in items:
            res_data = {}
            res_data['url'] = item.find('a')['href']
            res_data['position'] = item.find('a').get_text().strip()
            res_data['link'] = item.find('p', class_="company-name").find('a').get('href')  #['href']
            res_data['company'] = item.find('p', class_="company-name").find('a').get_text()
            res_data['salary'] = item.find('span', class_="text-warning").get_text()
            res_data['location'] = item.find('p', class_="condition").find('a', class_="area").get_text()
            res_data['school'] = item.find('span', class_="edu").get_text()
            res_data['description'] = item.find('p', class_="field-financing").get_text().replace('\n', '').strip()
            res_data['rule'] = item.find('p', class_="condition").find_all('span')[2].get_text()
            if item.find('div', class_="company-info").find('p', class_="temptation"):
                res_data['other'] = item.find('div', class_="company-info").find('p', class_="temptation").get_text().replace('\n', ' ').strip()
            else:
                res_data['other'] = "暂无信息！"
            # res_data['source'] = '猎聘网'
            data.append(res_data)

        print data
        return data

class GanjiHtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        print soup.original_encoding
        new_data = self._get_new_data(soup)
        return new_data

    # 本地方法获取数据：company, salary, location的信息
    def _get_new_data(self, soup):
        data = []
        items = soup.find_all('dl', class_="job-list")

        for item in items:
            res_data = {}
            res_data['url'] = item.find('a')['href']
            res_data['position'] = item.find('a').get_text()
            res_data['link'] = item.find('div', class_="new-dl-company").find('a')['href']
            res_data['company'] = item.find('div', class_="new-dl-company").find('a').get_text()
            res_data['salary'] = item.find('div', class_="new-dl-salary").get_text().strip()
            res_data['location'] = soup.find('a', class_="fc-city").get_text() + item.find('dd', class_="pay").get_text() #.strip()
            res_data['rule'] = item.find('div', class_="s-butt").find_all('li')[2].get_text()
            res_data['school'] = item.find('div', class_="s-butt").find_all('li')[3].get_text()
            res_data['other'] = item.find('div', class_="new-dl-tags").get_text().strip()
            res_data['description'] = item.find('div', class_="s-butt").find_all('li')[5].get_text().strip()
            # res_data['source'] = '赶集网'
            data.append(res_data)

        print data
        return data

class Job51HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb18030')
        print soup.original_encoding
        new_data = self._get_new_data(soup)
        return new_data

    # 本地方法获取数据：company, salary, location的信息
    def _get_new_data(self, soup):
        data = []
        count = True
        items = soup.find('div', class_="dw_table").find_all('div', class_="el")

        for item in items:
            res_data = {}
            if count:
                count = False
                continue
            res_data['url'] = item.find('a').get('href')
            res_data['position'] = item.find('a').get_text().strip()
            res_data['link'] = item.find('span', class_="t2").find('a')['href']
            res_data['company'] = item.find('span', class_="t2").find('a').get_text()
            res_data['salary'] = item.find('span', class_="t4").get_text()  #.strip()
            res_data['location'] = item.find('span', class_="t3").get_text()
            res_data['rule'] = ""
            res_data['school'] = ""
            res_data['other'] = "暂无信息！"
            res_data['description'] = ""
            # res_data['source'] = "51Job"
            data.append(res_data)

        print data
        return data

class YingcaiHtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        print soup.original_encoding
        new_data = self._get_new_data(soup)
        return new_data

    # 本地方法获取数据：company, salary, location的信息
    def _get_new_data(self, soup):
        data = []
        items = soup.find('div', class_="resultList").find_all('div', class_="jobList")

        for item in items:
            res_data = {}
            res_data['url'] = item['data-url']
            res_data['position'] = item.find('span', class_="e1").get_text()
            res_data['link'] = item.find('span', class_="e3").find('a')['href']
            res_data['company'] = item.find('span', class_="e3").find('a').get_text()
            res_data['salary'] = item.find_all('span', class_="e2")[1].get_text()
            res_data['location'] = item.find_all('span', class_="e1")[1].get_text().split()[0]
            res_data['rule'] = item.find_all('span', class_="e1")[1].get_text().split()[1].split('/')[0]
            res_data['school'] = item.find_all('span', class_="e1")[1].get_text().split()[1].split('/')[1]
            res_data['other'] = "暂无信息！"
            res_data['description'] = item.find_all('span', class_="e3")[1].get_text().replace('\n', '').replace(' ', '').strip()
            # res_data['source'] = '英才网'
            data.append(res_data)

        print data
        return data

class ZhilianHtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        print soup.original_encoding
        new_data = self._get_new_data(soup)
        return new_data

    # 本地方法获取数据：company, salary, location的信息
    def _get_new_data(self, soup):
        data = []
        soup.find('table', class_="newlist").extract()
        items =soup.find_all('table', class_="newlist")

        for item in items:
            res_data = {}

            res_data['url'] = item.find('a')['href']
            res_data['position'] = item.find('a').get_text().strip()
            res_data['link'] = item.find('td', class_="gsmc").find('a')['href']
            res_data['company'] = item.find('td', class_="gsmc").find('a').get_text()
            res_data['salary'] = item.find('td', class_="zwyx").get_text()
            res_data['location'] = item.find('td', class_="gzdd").get_text()
            res_data['rule'] = ""    #.strip()
            res_data['school'] = ""
            res_data['other'] = "暂无信息！"
            res_data['description'] = ""
            # res_data['source'] = "智联网"
            data.append(res_data)

        print data
        return data

class JiaobuHtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        print soup.original_encoding
        new_data = self._get_new_data(soup)
        return new_data

    # 本地方法获取数据：company, salary, location的信息
    def _get_new_data(self, soup):
        data = []
        items = soup.find('ul', class_="clearfix").find_all('li')

        for item in items:
            res_data = {}
            res_data['url'] = item.find('a')['href']
            res_data['img'] = item.find('img')['src']
            res_data['text'] = item.find('span', class_="wztitle").get_text()
            res_data['source'] = '脚步网'
            data.append(res_data)

        print data
        return data

class GerenjianliHtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb18030')
        print soup.original_encoding
        new_data = self._get_new_data(soup, page_url)
        return new_data

    # 本地方法获取数据：company, salary, location的信息
    def _get_new_data(self, soup, page_url):
        data = []
        items = soup.find('table', id="dlNews").find_all('tr')

        for item in items:
            res_data = {}
            res_data['url'] = page_url + item.find('a')['href']
            res_data['img'] = page_url + item.find('img')['src']
            res_data['text'] = item.find('a').get_text()
            res_data['source'] = '个人简历网'
            data.append(res_data)

        print data
        return data

class WubaidingHtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
        print soup.original_encoding
        new_data = self._get_new_data(soup)
        return new_data

    # 本地方法获取数据：company, salary, location的信息
    def _get_new_data(self, soup):
        data = []
        items = soup.find_all('li', class_="resumeList")

        for item in items:
            res_data = {}
            res_data['url'] = item.find('a', class_="title")['href']
            res_data['img'] = item.find('div', class_="img").find('img')['src']
            res_data['text'] = item.find('a', class_="title").get_text()
            res_data['source'] = '五百丁'
            data.append(res_data)

        print data
        return data