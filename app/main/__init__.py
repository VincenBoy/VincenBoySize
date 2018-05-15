# encoding=utf-8
from flask import Blueprint
#实例化 Blueprint 类，两个参数分别为蓝本的名字和蓝本所在包或模块，第二个通常填 __name__ 即可
main = Blueprint('main', __name__)

#之所以写在最后是因为避免循环导入依赖，因为接下来在 main 文件夹下 创建的 views.py 和 errors.py 都要导入蓝本 main
from . import views, errors
