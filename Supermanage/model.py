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
    res = User.objects.filter(username=username, password=password).first()
    if res:
        return res.user_level
    else:
        return 2


# 添加商品种类, 返回：1-成功添加， 0-失败
def addGoodsType(typename):
    res = GoodsType.objects.filter(goods_type=typename).first()
    try:
        if res:
            return 0
        type_add = GoodsType(goods_type=typename)
        type_add.save()
        return 1
    except:
        return 0


# 列表返回所有商品种类
def getGoodsType():
    res = GoodsType.objects.all()
    type_list = []
    for var in res:
        type_list.append(var.goods_type)

    return type_list


# 添加商品信息， 加到库存表中, 返回：1-成功，0-失败, 2-编号重复
def addGoods(goods_id, goods_type, goods_name, unit, quantity, buying_price, price, lowest_quantity):
    res = Stock.objects.filter(goods_id=goods_id).first()
    if res:
        return 2
    try:
        goods_add = Stock(goods_id=goods_id, goods_type=goods_type, goods_name=goods_name, unit=unit, quantity=quantity,
                          buying_price=buying_price, price=price, lowest_quantity=lowest_quantity)
        goods_add.save()
        return 1
    except:
        return 0


# 列表返回所有库存信息
def getStock():
    res = Stock.objects.all()
    goods_list = []
    for var in res:
        goods_list.append(var)
    return goods_list
