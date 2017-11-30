# 搜索路径在python安装的时候就确定了 dos命令行确认下 ：python -> import sys -> sys.path
import pprint
import sys
import types
# 导入某一模块的指定部分(推荐)  如果有重名就要使用class.method()的方法调用
# from sys import  path
import pickle
from urllib import request

from com.quark.quick.start import Logic
from com.quark.quick.start import HelloWorld


def iterator_num(n):
    it = iter(n)
    # for i in  it:
    #   print(i)
    try:
        while True:
            print(next(it))
    except:
        sys.exit()


def generator_defination():
    for i in range(1,10):
        # 可以单独获取循环中的每一个元素
        #  作用： 把当前函数变成一个生成器 而不是当成一个普通函数，当调用该函数的时候会返回一个iterator对象
        #  执行到yield时 会记录并且返回当前迭代值 ，下一次迭代会从yield 语句的下一行继续执行
        if i == 8:
            return
        yield i


num = 100


# 打印99乘法表
def func_99(n):
    for x in range(1,n):
        for y in range(1,n):
            if y == n - 1 and x != n - 1:
                # 统一向左对齐
                print("".ljust(6))
            else:
                if y > x:
                    # 统一向左对齐
                    print("".ljust(6), end='     ')
                else:
                    # 统一向左对齐
                    print((str(y) + "x" + str(x) + "=" + str(y * x)).ljust(6), end=' ')

# 99乘法表
def func_99_v2(n):
    for i in range(1, n):
            for j in range(1, i+1):
                print('{}x{}={}\t'.format(i, j, i*j), end='')
            print()


def func_99_v3(n):
    for i in range(1,n):
         for j in range(1,i+1):
             # 不换行
             print('%dx%d=%d'%(i,j,i*j),end=" ")
         # 换行
         print()


def num_change():
    # 修改全局变量
    global num
    num +=100


g = lambda x,y: x**2+y**3
# f = generator_defination()


if __name__ == '__main__':
    # list_a = ['a', 'b', 'c']
    # iterator_num(list_a)
   #  每次调用函数都会往 iterator里面添加元素（第一次调用时 iterator中只有一个元素（取第一个），第二次 两个（取第二个元素）。。。。）
   # for i in generator_defination():
   #     # 每次调用生成得到的iterator对象是同一个
   #     print(id(generator_defination()))
   #     print(i)
   #  num_change()
   #  print(num)
   #  判断类型(是否是生成器类型)
   # print(isinstance(generator_defination(),types.GeneratorType))
   # print(isinstance(generator_defination,types.GeneratorType))
   #  print(g(2,3))
   #  print(g(x=2,y=3))
    # 列表推导式
    # print([3*x for x in range(1,10) if  x > 3 ])
    # print([3*x+2*y for x in range(1,3) for y in range(3,6)])
    #嵌套列表
    list_rep = [[1,2,3,4],
                [4,5,6,7],
                [7,8,9,10]]
    #使用列表推导式改变列表的排序结果：
    # [[1, 4, 7],
    # [2, 5, 8],
    # [3, 6, 9],
    # [4, 7, 10]]
    # print([[row[i] for row in list_rep] for i in range(4)])
    #分离两个for
    # list_trans = []
    # for i in range(4):
    #      list_ele = []
    #      for row in list_rep:
    #          list_ele.append(row[i])
    #      list_trans.append(list_ele)
    # print(list_trans)
    #集合定义 无序不重复
    # list_arr = ("a","b")
    # set_a  = set()
    # 可以添加元组 但是不能添加列表
    # set_a.add(list_arr)
    # print(set_a)
    #元组转字典
    # array = (('k1y1','value1'),('k2y1','value2'),('k3y1','value3'))
    # dict_a = dict(array)
    # print(dict_a)
    # 对字典排序
    # sorted参数说明
    # lambdal接收的值
    # key=lambdal表达式
    # reverse 是否反转
    # print( sorted(dict_a.items(),key=lambda a : a[0][3] and a[1][5] ,reverse=True))
    # #dict的遍历
    # for k,v in dict_a.items():
    #     print(k,v)
    # #  借助enumerate迭代出列表的索引
    # for k,v in enumerate(array):
    #     print(k,v)
    # Logic.calculation_feb(20)
    # str_a = 'hello,world'
    # 用户易读的表达式
    # print(str(str_a))
    # 解释器易读的表达式
    # print(repr(str_a))
    # func_99(10)
    # 两种替换方式
    # print("我叫%s,他叫%s,我今年%o岁,他今年%o岁"%('小明','小刚',10,11))
    # {} 中如果没有指定名称 ，format中的参数会默认按照顺序放入
    # print("网站：{name},地址：{site}".format(name="百度",site="www.baidu.com"))
    # file = open("C:\\Users\Administrator\\Desktop\\python_test.txt",mode='r+')
    # file.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
    # for line in file.readlines():
    #         # 去掉空格
    #         print(line.strip())
    # file = open("C:\\Users\\Administrator\\Desktop\\python_01.txt", mode='rb+')
    # file.write(b'0123456789abcdef')
    # 把文件的初始角标移动到指定位置
    # 0：表示从零开始（默认）  1：当前流的位置开始 2 ：表示从流的结尾开始
    # !!!注意：str类型只支持（int，0） 即第二个参数只能为0
    # 0、1支持字节类型的文本内容
    # file.seek(-2,2)
    # print(file.read())
    # file.close()
    # data1 = {'a': [1, 2.0, 3, 4 + 6j],
    #          'b': ('string', u'Unicode string'),
    #          'c': None}
    # output = open('C:\\Users\\Administrator\\Desktop\\1.txt','wb')
    # pickle.dump(data1,output)
    # # 把内部缓冲区的数据立即写入到文件 不需要等到输出缓冲区写入
    # output.flush()
    # # 一定要关闭流
    # output.close()
    # pkl_file = open('C:\\Users\\Administrator\\Desktop\\1.txt', 'rb')
    # data2 = pickle.load(pkl_file)
    # pprint.pprint(data2)
    # 一定要关闭流
    # pkl_file.close()
    # response = request.urlopen("http://www.baidu.com/")  # 打开网站
    # fi = open("C:\\Users\\Administrator\\Desktop\\1.txt", 'w')  # open一个txt文件
    # page = fi.write(str(response.read()))  # 网站代码写入
    # fi.close()
    # num = input("请输入数字")
    # 如果不转换类型默认是str
    # print(int(num)**2)
    # func_99(10)
    # func_99_v2(10)
    func_99_v3(10)
