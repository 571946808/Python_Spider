# spider_baike
抓取百度百科关于Python词条下1000个链接页面的数据，并输出到output.html文件。Python2.7的版本

# 需要的运行环境：
- Ubuntu14.04、Python2.7、BeautifulSoup4、urllib2等

# 爬虫调度端

## URL管理器：
管理待抓取URL集合和已抓取URL集合，防止重复抓取和循环抓取。

- 添加新的URL到待爬取集合中
- 判断待添加URL是否在容器中
- 获取待爬取URL
- 判断是否还有待爬取URL
- 将URL从待爬取移动到已爬取

```
实现方式：
内存：Python内存。set()
关系数据库：MySQL。urls(url, is_crawled)
缓存数据库：Redis。set()
```

## 网页下载器：
- urllib2（本例的实现方式）
```
urllib2：3种下载网页方法
- 最简洁方法：urllib2.urlopen(url)
- 添加data，httpheaders等：(url、data、headers) ->urllib2.Request -> urllib2.urlopen(Request)
- 添加特殊情况的处理器：
    1.  HTTPcookieProcessor、ProxyHander、HTTPSHander、HTTPRedireHander
    2.  opener = urllib2.build_opener(hander)
    3.  urllib2.install_opener(opener)
    4.  urllib2.urlopen(url)或者urllib2.urlopen(Request)

```
- requests

## 网页解析器：
- 正则表达式（模糊匹配）
- html.parser（结构化解析）
- BeautifulSoup（结构化解析）
- lxml（结构化解析）
```
  结构化解析DOM树：[文档对象模型]（英语：Document Object Model，缩写DOM），是W3C组织推荐的处理可扩展置标语言的标准编程接口。

  BeautifulSoup语法：
  创建BeautifulSoup对象 -> 搜索节点（find_all或find）-> 访问节点（名称、属性、文本）
```

## 一个简单的爬虫实例：
- 确定目标：
- 分析目标：URL格式、数据格式、网页编码
- 编写代码：
- 执行代码：
