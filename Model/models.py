# -*- coding: utf-8 -*-
"""
    数据库表信息
"""
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 用户信息表
class User(models.Model):
    user_level = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=100)


# 进货表
class Buy(models.Model):
    buy_id = models.IntegerField()  # 进货编号
    buy_year = models.IntegerField()
    buy_month = models.IntegerField()
    buy_day = models.IntegerField()
    goods_id = models.CharField(max_length=10)   # 商品编号
    good_quantity = models.IntegerField()   # 商品数量


# 库存商品表
class Stock(models.Model):
    goods_id = models.CharField(max_length=10)  # 商品编号
    goods_type = models.CharField(max_length=10)     # 商品种类
    goods_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)   # 商品单位
    quantity = models.IntegerField()    # 库存数量
    buying_price = models.FloatField()  # 进货价
    price = models.FloatField()         # 售价
    lowest_quantity = models.IntegerField()


# 商品种类表
class GoodsType(models.Model):
    goods_type = models.CharField(max_length=10)
