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
from .model import *


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
    user_level = request.COOKIES.get('user_level')

    if user_level == '0' or user_level == '1':
        context = {
            'username': username
        }
        stock_list = getStock()
        if user_level == '0':
            context.update({
                'info_list': ['编号', '种类', '名称', '单位', '库存量', '进货价（元）', '售价（元）', '最低库存']
            })
            show_list = []
            for var in stock_list:
                show_list.append([var.goods_id, var.goods_type, var.goods_name, var.unit, var.quantity,
                                  var.buying_price, var.price, var.lowest_quantity])
            context.update({
                'show_list': show_list
            })
        return render(request, 'stock.html', context)
    else:
        return redirect('/login')


# 添加商品种类
def add_type(request):
    if request.COOKIES.get('user_level') is None:
        return redirect('/login')
    if int(request.COOKIES.get('user_level')) is not 0:     # 非管理员/未登录
        return redirect('/stock')

    ctx = {
        'username': request.COOKIES.get('username')
    }
    if request.method == 'POST':
        if addGoodsType(request.POST.get('type')) == 1:
            ctx.update({
                'msg': '添加种类成功！'
            })
        else:
            ctx.update({
                'msg': '添加种类失败！'
            })

    return render(request, 'add_type.html', ctx)


# 添加商品信息
def add_goods(request):
    if request.COOKIES.get('user_level') is None:
        return redirect('/login')
    if int(request.COOKIES.get('user_level')) is not 0:     # 非管理员/未登录
        return redirect('/stock')

    ctx = {
        'username': request.COOKIES.get('username')
    }
    type_list = getGoodsType()
    ctx.update({
        'goodstype_list': type_list
    })

    if request.method == 'GET':
        return render(request, 'add_goods.html', ctx)

    else:
        goods_id = request.POST.get('goods_id')
        goods_type = request.POST.get('goods_type')
        goods_name = request.POST.get('goods_name')
        unit = request.POST.get('unit')
        buying_price = request.POST.get('buying_price')
        price = request.POST.get('price')
        lowest_quantity = request.POST.get('lowest_quantity')
        res = addGoods(goods_id, goods_type, goods_name, unit, 0, buying_price, price, lowest_quantity)
        if res == 1:
            ctx.update({
                'msg': '添加商品成功！'
            })
        elif res == 0:
            ctx.update({
                'msg': '添加商品失败！'
            })
        else:
            ctx.update({
                'msg': '商品编号重复！'
            })
        return render(request, 'add_goods.html', ctx)


# 销售
def sale(request):
    if request.COOKIES.get('user_level') is None:
        return redirect('/login')
    if int(request.COOKIES.get('user_level')) is not 0:     # 非管理员/未登录
        return redirect('/stock')

    ctx = {
        'username': request.COOKIES.get('username')
    }

    if request.method == 'GET':
        return render(request, 'sale.html', ctx)
    else:
        print request.body
        return HttpResponse('销售成功')


# 销售单页面
def sale_list(request):
    return HttpResponse('销售')