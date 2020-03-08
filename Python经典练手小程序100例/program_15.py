# -*- coding: utf-8 -*-

"""
【程序15】
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的
用B表示，60分以下的用C表示。
程序分析：c = a if a>b else b # 先执行中间的if，如果返回True，就是左边，False是右边。
"""

score = int(input('please input score:'))

print("A" if score >= 90 else ("B" if score >= 60 else "C"))
