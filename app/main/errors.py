# encoding=utf-8
from flask import render_template
#导入蓝本
from . import main

#定义错误处理
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

