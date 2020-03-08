# -*- coding: utf-8 -*-
# Python 3.x

"""
【程序2】
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
"""

profit_grade = [0, 100000, 200000, 400000, 600000, 1000000]
bonus_grade = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

bonus_1 = profit_grade[1] * bonus_grade[0]
bonus_2 = bonus_1 + (profit_grade[2] - profit_grade[1]) * bonus_grade[1]
bonus_3 = bonus_2 + (profit_grade[3] - profit_grade[2]) * bonus_grade[2]
bonus_4 = bonus_3 + (profit_grade[4] - profit_grade[3]) * bonus_grade[3]
bonus_5 = bonus_4 + (profit_grade[5] - profit_grade[4]) * bonus_grade[4]


def profit_input():
    profit = input("请输入利润（单位：元）：")
    while True:
        if profit.isdigit():
            return (int(profit))
            break
        else:
            profit = input("输入错误,请重新输入利润（单位：元）：")


profit = profit_input()
if profit <= profit_grade[1]:
    bonus = profit * bonus_grade[0]
elif profit <= profit_grade[2]:
    bonus = bonus_1 + (profit - profit_grade[1]) * bonus_grade[1]
elif profit <= profit_grade[3]:
    bonus = bonus_2 + (profit - profit_grade[2]) * bonus_grade[2]
elif profit <= profit_grade[4]:
    bonus = bonus_3 + (profit - profit_grade[3]) * bonus_grade[3]
elif profit <= profit_grade[5]:
    bonus = bonus_4 + (profit - profit_grade[4]) * bonus_grade[4]
else:
    bonus = bonus_5 + (profit - profit_grade[5]) * bonus_grade[5]
print("bonus:%.2f元" % bonus)
