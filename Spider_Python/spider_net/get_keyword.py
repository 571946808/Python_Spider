#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
import html_outputer
import html_outputer_template
import html_outputer_bbs
import html_outputer_add
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():return redirect(url_for('main'))

@app.route('/main', methods=['GET', 'POST'])
def main():
    list = html_outputer.HtmlOutputer().output_html('', '全国', '不限', '不限')
    return render_template('main.html', list = list, keyword ='', location ='全国', rule ='不限', school ='不限')

@app.route('/search', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    list = html_outputer.HtmlOutputer().output_html(request.form['keyword'], request.form['location'], request.form['rule'], request.form['school'])
    return render_template('main.html', list = list, keyword = request.form['keyword'], location = request.form['location'], rule = request.form['rule'], school = request.form['school'])

@app.route('/template', methods=['GET'])
def template():
    # 需要从request对象读取表单内容：
    list = html_outputer_template.HtmlOutputerTemplate().output_html()
    return render_template('template.html', list = list)

@app.route('/bbs', methods=['GET'])
def bbs():
    # 需要从request对象读取表单内容：
    list = html_outputer_bbs.HtmlOutputerBbs().output_html()
    return render_template('bbs.html', list = list)

@app.route('/login', methods=['GET'])
def login():
    # 跳转登录页：
    return render_template('login.html')

@app.route('/admin', methods=['POST'])
def admin():
    # 如果失败跳转登录页并显示提示信息：
    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        list = html_outputer_bbs.HtmlOutputerBbs().output_html()
        return render_template('admin.html', list = list)
    else:
        return render_template('login.html', tip = '登录失败，请重新输入！')

@app.route('/add', methods=['POST'])
def add():
    # 如果失败跳转登录页并显示提示信息：
    if request.form.getlist('order') != '' and (request.form['title'] == '' or request.form['comment'] == ''):
        html_outputer_add.HtmlOutputerAdd().output_html_delete(request.form.getlist('order'))
        list = html_outputer_bbs.HtmlOutputerBbs().output_html()
        return render_template('admin.html', list = list)
    elif request.form['title'] != '' and request.form['comment'] != '':
        html_outputer_add.HtmlOutputerAdd().output_html_insert(request.form['title'], request.form['comment'])
    list = html_outputer_bbs.HtmlOutputerBbs().output_html()
    return render_template('admin.html', list = list)

if __name__ == '__main__':
    app.run()   #debug=True, host='127.0.0.1', port=80