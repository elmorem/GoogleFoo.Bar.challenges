# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:45:36 2018

@author: marke
"""
def answer(area):
    tmp = area
    res = []
    while area > 0:
        sq = tmp** .5
        if sq == int(sq):
            res.append(tmp)
            area -= tmp
            tmp = area
            continue
        tmp -= 1
    return res