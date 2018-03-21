#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     view
   Description :    
   Author :       Lerrety
   date：          18-3-21
"""

from django.shortcuts import render
from django.http import HttpResponse
from .model import checkUser


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = checkUser(username, password)
        if check_user == 0:
            return HttpResponse('管理员登录成功')
        elif check_user == 1:
            return HttpResponse('员工登录成功')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})