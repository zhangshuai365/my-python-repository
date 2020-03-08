# -*- coding: utf-8 -*-

"""
【程序17】
题目： 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为’\n’.
"""

s = input('input a string:\n')
letters_num = 0
space_num = 0
digit_num = 0
others_num = 0
for c in s:
    if c.isalpha():
        letters_num += 1
    elif c.isspace():
        space_num += 1
    elif c.isdigit():
        digit_num += 1
    else:
        others_num += 1
print('char = %d,space = %d,digit = %d,others = %d' % (letters_num, space_num, digit_num, others_num))
