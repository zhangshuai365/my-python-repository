# -*- coding: utf-8 -*-


"""
【程序27】
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
程序分析：运用递归思想，每次将字符串作为参数调用函数并取出最后一位，再用余下的字符串去调用该函数。若不使用递归，使用循环语句一样可以完成该内容。
"""

str1 = list(input('input a string:'))
str2 = []


def newstr(s):
    if len(s) != 0:
        str2.append(s[-1])
        s.pop()
        newstr(s)
    else:
        pass

'''
def newstr(s):
    for i in range(len(s), 0, -1):
        str2.append(s[i - 1])


'''


newstr(str1)
str3 = ''.join(x for x in str2)
print(str3)
