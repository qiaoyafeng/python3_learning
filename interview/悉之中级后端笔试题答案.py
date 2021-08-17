# -*- coding: utf-8 -*-
# @Date    : 2021/6/3 13:23
# @Author  : Duxiaolong
# @File    : demo.py
import json
from typing import Union, Optional, Tuple, Dict
from collections import defaultdict
import datetime

from mongoengine import *

class Test:

    ITEM_PRICE = {
        'ITEM0001': 10,
        'ITEM0013': 20,
        'ITEM0022': 30,
    }

    ITEM_PRICE_DISCOUNT = {
        'ITEM0001': 5,
        'ITEM0013': 20,
        'ITEM0022': 15,
    }

    @staticmethod
    def is_number(num: str) -> bool:
        try:
            int(num)
            return True
        except ValueError:
            return False

    @classmethod
    def first_question(cls, info: str) -> dict:
        """
        Input:
            string1 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'
        :return:
        obj1 = {
            "ITEM0001": 1,
            "ITEM0013": 2,
            "ITEM0022": 1,
        }
        """
        result = defaultdict(int)
        try:
            info_json = json.loads(info)
            if not isinstance(info_json, list):
                return {"msg": "Input error"}
        except TypeError:
            return {"msg": "Input error"}
        for value in info_json:
            tmp = value.split('x')
            if len(tmp) == 2 and cls.is_number(tmp[1].strip()):
                if tmp[0].strip() not in result:
                    result[tmp[0].strip()] = tmp[1].strip()
                else:
                    result[tmp[0].strip()] += tmp[1].strip()
            else:
                return {"msg": "Input error"}
        return dict(result)

    def second_question(self, info: str, discount: bool = False) -> Union[int, dict]:
        """
        ITEM 指的是商品：
        ITEM0001 的价格 为 10；
        ITEM0013 的价格 为 20；
        ITEM0022 的价格 为 30。

        Input:
            string1 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'
        Output:
            80
        Input:
            string1 = '["ITEM0006 x 1"]'
        Output:
            "ITEM 不合法！"
        """
        result = 0
        first_info = self.first_question(info)
        if "msg" in first_info:
            return first_info
        for item, num in first_info.items():
            if item not in self.ITEM_PRICE:
                return {"msg": "ITEM 不合法"}
            else:
                result += self.ITEM_PRICE_DISCOUNT[item] * int(num) if discount else self.ITEM_PRICE[item] * int(num)
        return result

    def third_question(self, info: str) -> Union[dict, Tuple[Union[dict, Dict[str, str], int], Optional[str]]]:
        """
        优惠 1：
            同时购买 ITEM0001 和 ITEM0022，则该商品半价
        优惠 2：
            满 100 减 30
        优惠只能选一种。自动计算多种优惠的结果，并输出最优结果。
        """
        first_info = self.first_question(info)
        if "msg" in first_info:
            return first_info
        discount, total1 = None, None
        if 'ITEM0001' in first_info and 'ITEM0022' in first_info:
            # 优惠1
            total1 = self.second_question(info, discount=True)
            discount = "优惠2"
        # 没有折扣的总价
        total = self.second_question(info)
        if total >= 100:
            total -= (total // 100) * 30
            discount = "优惠2"
        if total1 is not None and total1 < total:
            return total1, discount
        else:
            return total, discount


class UserForm(Document):
    user_id = StringField(unique=True, required=True, verbose_name='用户id')
    name = StringField(required=True, verbose_name='用户名')


class GoodsForm(Document):
    """
    仅对当前题目进行设计，商品属性涵盖太多东西, 比如(spu, sku)
    如果要展开设计需要多张表，并且具有管理关系，不建议用非关系数据库来做
    """
    name = StringField(required=True, verbose_name='商品名称')
    price = IntField(default=0, verbose_name='商品价格')
    create_time = DateField(default=datetime.datetime.now(), verbose_name='创建时间')


class OrderForm(Document):
    """
    针对该题目设计, 收货地址、支付方式、商品信息等信息不做处理
    """
    order_id = StringField(required=True, verbose_name='订单id')
    user = ReferenceField(UserForm, verbose_name='下单用户')
    total_amount = IntField(default=0, verbose_name='订单金额')
    discount = StringField(required=True, verbose_name='折扣方案')


if __name__ == '__main__':
    obj = Test()
    info1 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'
    print(obj.first_question(info1))
    info2 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'
    info3 = '["ITEM0006 x 1"]'
    print(obj.second_question(info2))
    print(obj.second_question(info3))
    info4 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'
    info5 = '["ITEM0001 x 1", "ITEM0013 x 3", "ITEM0022 x 1"]'
    print(obj.third_question(info4))
    print(obj.third_question(info5))

