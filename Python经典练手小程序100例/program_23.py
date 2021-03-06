# -*- coding: utf-8 -*-

"""
【程序22】
题目：打印出如下图案（菱形）

   *
  ***
 *****
*******
 *****
  ***
   *

程序分析：最宽的一行打印7个星号，相邻的两行打印的星号数量相差2。推出公式第n行打印2*abs(abs(n-3)-3)+1,且第n行是从第abs(n-3)列开始,进而推出通项公式。
"""


def rhombus(N):
    for i in range((2 * N + 1)):
        print(' ' * abs(i - N), '*' * (2 * abs(abs(i - N) - N) + 1))


rhombus(6)
