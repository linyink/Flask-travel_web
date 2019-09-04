# encoding: utf-8

from functools import wraps
from flask import session, redirect, url_for


# 登录限制的装饰器
# 未登录不能点击发布问答功能
# 不是很理解
def login_required(func):
    @wraps(func)
    def limit(*args, **kwargs):
        # 如果获取到了user_id，就解除限制
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            # 如果没有获取到user_id,就返回登录界面
            return redirect(url_for('login'))
    return limit