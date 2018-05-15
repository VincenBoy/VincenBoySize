# encoding=utf-8
from flask import render_template
#导入蓝本
from . import main

#注册路由
@main.route('/index')
def index():
    return render_template('Repairing.html')

@main.route('/user/<name>')
def user(name):
    return  render_template('user.html',name=name)
