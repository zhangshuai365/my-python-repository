# -*- coding: utf-8 -*-
# Python 3.x

"""
【程序4】
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天。
"""

day_num_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def check_year(s):
    while True:
        input_year = input(s)
        if input_year.isdigit():
            return int(input_year)
            break
        else:
            print("输入有误，请检查。")


def check_month(s):
    while True:
        input_month = input(s)
        if input_month.isdigit() and 0 < int(input_month) < 13:
            return int(input_month)
            break
        else:
            print("输入有误，请检查。")


def check_day(s):
    while True:
        input_day = input(s)
        if input_day.isdigit() and 0 < int(input_day) <= day_num_month[month - 1]:
            return int(input_day)
            break
        else:
            print("输入有误，请检查。")


year = check_year('year:')

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    day_num_month[1] = 29

month = check_month('month:')
day = check_day('day:')

print("%d年%d月%d日是一年的第%d天。" % (year, month, day, sum(day_num_month[0:month - 1]) + day))
