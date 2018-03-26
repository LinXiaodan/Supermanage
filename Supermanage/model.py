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


def reduce_stock(reduce_set, username, now_time, user_level):
    """
        销售-减少库存，添加销售库记录
        返回: {
            'status': 'success'/'fail',
            0:{id, quantity, price, tot_price},
            1:.....
            'total': 总额,
            'sale_id': 销售单号,
            'time': now_time
        }
    """
    sale_id = now_time + user_level    # 销售单号：时间戳+用户等级
    total = 0
    return_set = {
        'sale_id': sale_id,
        'time': now_time
    }

    try:
        for key in reduce_set:
            goods_id = reduce_set[key]['id']
            goods_quantity = int(reduce_set[key]['quantity'])
            stock_object = Stock.objects.get(goods_id=goods_id)
            db_quantity = stock_object.quantity     # 库存数量
            Stock.objects.filter(goods_id=goods_id).update(quantity=db_quantity-goods_quantity)  # 减少库存
            return_set.update({     # 商品金额
                key: {'goods_id': goods_id,
                      'goods_quantity': goods_quantity,
                      'price': stock_object.price,
                      'tot_price': stock_object.price*goods_quantity}
            })
            total += stock_object.price*goods_quantity  # 计算总额
            sale = Sale(sale_id=sale_id, time=now_time, goods_id=goods_id,
                        goods_quantity=goods_quantity, username=username)
            sale.save()
        return_set.update({
            'status': 'success',
            'total': total
        })
        return return_set
    except Exception as e:
        return {
            'status': 'fail'
        }
