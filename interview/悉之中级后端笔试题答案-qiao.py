#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
from typing import cast


class XiziTest:

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


    def str2dict(self, datastr):
        """ 将字符串转换为字典

        Input:
        string1 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'

        Output:
        obj1 = {
            "ITEM0001": 1,
            "ITEM0013": 2,
            "ITEM0022": 1,
        }
        """
        datadict = {}
        datalists = json.loads(datastr)
        for dataitem in datalists:
            data = dataitem.split('x')
            if data[0].strip() not in datadict:
                datadict[data[0].strip()] = data[1].strip()
            else:
                datadict[data[0].strip()] += data[1].strip()
        return datadict

    def calc_cost(self, datastr, isdiscount=False):
        """ 根据输入的商品个数，查询单价计算总消费，如果商品不存在，返回ITEM不合法

        Input:
        string1 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'

        Output:
        80


        Input:
        string1 = '["ITEM0006 x 1"]'

        Output:
        "ITEM 不合法！"
        """
        cost = 0
        datadict = self.str2dict(datastr)
        for item, number in datadict.items():
            if item not in self.ITEM_PRICE:
                return {"message": "ITEM 不合法"}
            else:
                cost += self.ITEM_PRICE_DISCOUNT[item] * int(number) if isdiscount else self.ITEM_PRICE[item] * int(number)
        return cost

    def discount_cost(self, datastr):
        """获取优惠后消费和优惠方式

        Input:
        string1 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'

        Output:
        60
        "优惠 1"

        Input:
        string1 = '["ITEM0001 x 1", "ITEM0013 x 3", "ITEM0022 x 1"]'

        Output:
        70
        "优惠 2"

        """
        cost1, cost2 = 0, 0
        discounttype = None
        datadict = self.str2dict(datastr)
        if "message" in datadict:
            return datadict
        # 获取未优惠的消费总计
        cost = self.calc_cost(datastr)
        
        if 'ITEM0001' in datadict and 'ITEM0022' in datadict:  # 优惠方式1
            cost1 = self.calc_cost(datastr, isdiscount=True)
            discounttype = "优惠1"
        if cost >= 100:  # 优惠方式2
            cost -= (cost // 100) * 30
            discounttype = "优惠2"

        if cost1 and cost1 < cost:
            return cost1, discounttype
        else:
            return cost, discounttype


if __name__ == '__main__':
    test = XiziTest()
    datastr1 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'
    print('str2dict====1====', test.str2dict(datastr1))
    datastr2 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'
    datastr3 = '["ITEM0006 x 1"]'
    print('str2dict====2====', test.calc_cost(datastr2))
    print('str2dict====3====', test.calc_cost(datastr3))
    datastr4 = '["ITEM0001 x 1", "ITEM0013 x 2", "ITEM0022 x 1"]'
    datastr5 = '["ITEM0001 x 1", "ITEM0013 x 3", "ITEM0022 x 1"]'
    print('str2dict====4====', test.discount_cost(datastr4))
    print('str2dict====5====', test.discount_cost(datastr5))

