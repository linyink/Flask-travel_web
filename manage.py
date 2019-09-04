"""
这是程序的入口
"""
# encoding: utf-8
# 没有用manage.py的主要原因是在测试阶段，不太方便
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
# from views import app
# from exts import db
#
# from models import User, Question, Answer
# # 这两句话不写又要报错
# ##################################
# import pymysql
# pymysql.install_as_MySQLdb()
# ##################################
#
# manager = Manager(app)
#
# # 使用Migrate绑定app和db
# migrate = Migrate(app, db)
#
# # 添加迁移脚本的命令到manager中
# manager.add_command('db', MigrateCommand)
#
# if __name__ == '__main__':
#     manager.run()




# python manage.py runserver