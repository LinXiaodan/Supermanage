#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File Name：     view
   Description :    
   Author :       Lerrety
   date：          18-3-21
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .model import checkUser
from settings import cookies_salt


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = checkUser(username, password)
        if check_user == 0 or check_user == 1:
            res = redirect('/stock')
            res.set_cookie('username', username, 60*60*24)
            res.set_cookie('user_level', check_user, 60*60*24)
            return res

        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})


# 库存
def stock(request):
    username = request.COOKIES.get('username')
    user_level = int(request.COOKIES.get('user_level'))
    print user_level

    if user_level == 0 or user_level == 1:
        print user_level
        context = {
            'username': username
        }
        return render(request, 'stock.html', context)
    else:
        print 'no'
        return redirect('/login')
