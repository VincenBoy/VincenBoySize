# encoding:utf-8
#模块初始化文件，Flask 程序对象的创建必须在 __init__.py 文件里完成， 然后我们就可以安全的导入引用每个包
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from  flask_bootstrap import Bootstrap

db = SQLAlchemy()


def create_app(config_name):
    # 创建项目对象
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    bootstrap = Bootstrap(app)

    #注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
