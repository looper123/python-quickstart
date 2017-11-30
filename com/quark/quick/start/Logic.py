# 斐波那契数列
import random
from time import time

import datetime


def calculation_feb(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


# 0.0010020732879638672
# lambda表达式实现斐波那契数列（递归方式）
def func_feb_lambda(n):
    time_start = time()
    for i in range(0, n):
        print(feb_lambda(i))
    print('使用lambda花时间{}s'.format(time() - time_start))


feb_lambda = lambda n: 0 if n == 0    else 1 if n == 1 else feb_lambda(n - 2) + feb_lambda(n - 1)


# 0.0005016326904296875
# 斐波那契数列 递归式
def func_feb_duplicate(n):
    time_start = time()
    for i in range(0, n):
        print(feb_duplicate(i))
    print("不使用lambda花时间{}s".format(time() - time_start))


def feb_duplicate(n):
    if n < 0:
        print('输入有误')
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return feb_duplicate(n - 2) + feb_duplicate(n - 1)


# 从1加到100
def loop(n):
    total, count = 0, 0
    while count <= n:
        total = total + count
        count += 1
        print(count)
    print(total)


def take_choice():
    x = random.choice(range(1, 100))
    y = random.choice(range(1, 200))
    if x == y:
        print("x+y", x, y)
    elif x > y:
        print("x", x, y)
    else:
        print("y", x, y)


# continue 和break的用法和java一致
def break_continue():
    for i in range(0, 10):
        if i == 4:
            print("continue while i == 4")
            continue
        if i == 8:
            print("break while i == 8")
            break
        print(i)


# pass是空语句 是为了保持程序结构的完整性（当定义一个空函数 可以让程序不报错）
def pass_defination():
    pass


def diff_for_wihle():
    y = 0;
    for i in range(0, 5):
        print(i)
    else:
        print("enter for else" + str(i))
    while y < 5:
        print(y)
        y += 1
    else:
        print("enter while else" + str(y))


# 最大公约数（在1- 较小的数之间查找）
def max_divisor(x, y):
    end = 0
    divisor = 1
    if x > y:
        end = y
    elif x == y:
        return x
    else:
        end = x
    for i in range(1, end):
        if (x % i == 0) and (y % i == 0):
            # 把最大的数字返回
            divisor = i
    return divisor


# 最小公倍数 从较大的数 - 两数积之间查找
def min_mutiple(x, y):
    start = 0
    if x > y:
        start = x
    elif x == y:
        return x
    else:
        start = y
    for i in range(start, x * y):
        if (i % x == 0) and (i % y == 0):
            return i


if __name__ == '__main__':
    # calculation_feb(10)
    # x, y, z = 10, 20, 30
    # 自定义分隔符
    # print(x, y, z, sep='|')
    # for i in range(10):
    #     print(feb_duplicate(i))
    # loop(20)
    # take_choice()
    # break_continue()
    # diff_for_wihle()
    #   Timer('func_feb_lambda(10)','from com.quark.quick.start.Logic import func_feb_lambda').timeit()
    #   Timer('func_feb_duplicate(10)','from com.quark.quick.start.Logic import func_feb_duplicate').timeit()
    # func_feb_lambda(10)
    # func_feb_duplicate(10)
    # print(max_divisor(12, 14))
    # print(min_mutiple(12, 14))
    # 日历类
    # 输出当月的所有日期
    # print(calendar.month(2017,2))
    # 输出指定月份第一天为周几 该月总天数
    # print(calendar.monthrange(2017,12))
    # 该月天数
    # print(calendar.mdays[9])
    # 昨天  timedelta 表示日期差 参数days  month  seconds  hours...
    print(datetime.date.today()-datetime.timedelta(days=1) )
    # str_a = 'calendar.my|title'
    # str_b = 'CALENDARMYTITLE'
    # #字符串转换
    # print(str_a.upper())
    # print(str_b.lower())
    # # 把每个单词的首字母大写 个单词件用任意符号分开
    # print(str_a.title())
