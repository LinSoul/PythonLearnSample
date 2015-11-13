#!/usr/bin/python
# coding: UTF-8

__author__ = 'Magic'

# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天

year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

def da_month(y):
    return 31

def xiao_month(y):
    return 30

def run_month(y):
    if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
        return 29
    return 28


monthDays = {
    1: da_month,
    2: run_month,
    3: da_month,
    4: xiao_month,
    5: da_month,
    6: xiao_month,
    7: da_month,
    8: da_month,
    9: xiao_month,
    10: da_month,
    11: xiao_month,
    12: da_month
}

daySum = 0

for x in range(month-1):
    daySum += monthDays[x+1](year)

daySum += day

print daySum
