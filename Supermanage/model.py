#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     model
   Description :    数据库操作
   Author :       Lerrety
   date：          18-3-21
"""
from Model.models import *


# 判断用户， 返回：0-管理员，1-员工，2-用户名或密码错误
def checkUser(username, password):
    print username, password
    res = User.objects.filter(username=username, password=password).first()
    if res:
        return res.user_level
    else:
        return 2
