"""
这是配置
"""
# encoding: utf-8


DEBUG = True
# 安全密码一定要是字符串类型
SECRET_KEY = '123456'
# 在数据库迁移时遇到一个问题，SQLALCHEMY_DATABASE_URI中的值报错
SQLALCHEMY_DATABASE_URI = "mysql://username:password@localhost/web_travel"  # 需要改成你自己的
SQLALCHEMY_TRACK_MODIFICATIONS = False
