# python数字类型
#  int、float、bool、complex（复数）

# python中的6个标准数据类型
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）
# python中规定的布尔类型 0 false  1 True
import builtins
import operator

from com.quark.quick.start.Logic import func_feb_lambda


class A:
    pass


class B(A):
    pass


# a=b=c=1


a, b, c = 1, "测试", 1.3
b = -6

# 内容相同的dictionary 地址不同 （is判断后返回false）
# var1 ={'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
# var2 = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
# 当string 使用了拼接 + * 等符号后 会重新开辟新的地址
var1 = 'www.runoob.comwww.runoob.com'
var2 = 'www.runoob.comwww.runoob.com'

# 可以把字符串 看做一个特殊的元组
d = "springCloud"
# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinyList = [123, 'runoob']
# set成员关系测试  删除重复元素
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
stu1 = set('abcdef')
stu2 = set('abcghi')
# 删除引用后  当print的对象不存在时 NameError: name 'a' is not defined
# del a,b
dicts = {1, 2, 3}
# dict[1] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
tinyDict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
tinyKey = {'name', 'code', 'site'}


# 以*号开头表示是一个可变参数列表
def test(*args):
    print(args)
    return args


# 打印出dict中所有的key和value
def _dict_iterator(dictionary):
    for a in dictionary:
        # print(e, end=':');
        # print(dictionary[e])
        # print(e+':'+dictionary[e]) # can only concatenate str (not "int") to str  因为dictionary（字典类型）无法转换成string类型
        print(a, ':', dictionary[a])


# and连接数字时 当所有都为true 返回最后一个数据  当存在false时 返回第一个false的 值
def _flag_test(x, y, z):
    print(x and y and z)


def _is_same_flag(a, b):
    if a is b:
        print("a和b引用相同对象")
    else:
        print("a和b引用不同对象")


def equals_same_flag(a, b):
    if a == b:
        print("a和b的值相同")
    else:
        print("a和b的值不同")



if __name__ == '__main__':
    # print(a)
    # print(b)
    # print(c)
    # isinstance 和type的区别|
    # isinstance 会认为子类型属于父类型  type则不会
    # print(isinstance(A(),A))
    # print(type(A()) == A)
    # print(isinstance(B(),A))
    # print(type(B()) == A )
    # print(120/100) #除法 包括小数点后的数字
    # print(120//100) #除法 取整数
    # print(120%100) #取余数
    # print(2**5) #乘方2的5次方
    # print(d[0])  #第一个字符
    # print(d[0:-1])  #第一个到倒数第一个字符 从左往右是0 开始 从右往左是从 -1 开始
    # print(d[2:5])  #第三个到第六个字符
    # print(d*2)  #输出当前字符两次
    # print(d+'test') #拼接
    #     python 无法改变已经存在的字符串 如d[0] = t  是无法实现的
    #     print(list)  # 输出完整列表
    #     print(list[0])  # 输出列表第一个元素
    #     print(list[1:3])  # 从第二个开始输出到第三个元素
    #     print(list[2:])  # 输出从第三个元素开始的所有元素
    #     print(tinylist * 2)  # 输出两次列表
    #     print(list + tinylist)  # 连接列表
    #     print(list[0][0])  # 取集合中第一个位置的数据 再从取出的字符串中取第一个字符
    #      if ("Rose" in student):
    #          print("Rose在集合中")
    #      elif ("Rose"  not in student):
    #          print("Rose不在集合中")
    # print(stu1 & stu2) # stu1和stu2中相同元素
    # print(stu1 | stu2) #or
    # print(stu1 - stu2) #去掉相同元素后 stu1的值
    # print(stu1 ^ stu2) #去掉相同元素后 stu1+stu2
    # print(dict['one'])  # 输出键为 'one' 的值
    # print(dict[2])  # 输出键为 2 的值
    # print(tinyDict)  # 输出完整的字典
    # print(tinyDict.keys())  # 输出所有键
    # print(tinyDict.values())  # 输出所有值
    # print(type(test(1,2,3,4))) #结果是一个元组
    # dictIterator(tinyDict)
    # flagTest(10,0,30)
    # print(0b11)  #0b表示二级制
    # print(0o11)  #0o表示10进制 默认
    # print(0x11)  #0x表示16进制
    # isSameFlag(var1,var2)
    # equalsSameFlag(var1,var2)
    # 在同一个类中数值相同（数字类型） 地址一定相同
    # 在不同类中加载 数值在（-5到 256）之间的 数值相同 地址也相同(小整数常量池)
    # print(id(b))
    # 字符串格式化 可用于类型转换  %s= str(s)
    # print("我叫%s今年%o岁"%("小明",10))
    para_str = """这是一个多行字符串的实例
    # TAB ( \t )。
    # 也可以使用换行符 [ \n ]。
    # """
    # print(para_str)
    # encode 的对象必须是string类型
    para_str= para_str.encode("gbk",errors='strict')
    print(para_str)
    # decode的对象必须是bytes
    para_str= para_str.decode("gbk",errors='strict')
    # print(para_str)
    # a="换行符"
    # a.title()
    # print("1".join(a))
    # L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # L[start:end+1:skip]   start从0开始  因为不包含end 所以到end+1结束
    # print(L[0:7:3])
    # for x in L : print(x,end="")
    # 元组 （）
    a = ('b', 'd', 'a', 'c', 'g', 'f', 'e')
    x = ['a', 'b', 'c', ]
    y = ['d', 'e', 'f', 'g']
    # print(type(a))
    # 转化为列表 []
    # 转化后需要重新定义变量来接受
    # b=list(a)
    # print(type(a))
    # 根据角标删除 可以指定范围
    # a = list(a)
    # del(a[0:2])
    # print(a)
    # print(b)
    # 合并集合 ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # print(x+y)
    # 集合增加 ['a', 'b', 'c', ['d', 'e', 'f', 'g']]
    # x.append(y)
    # print(x[3][1])
    # 嵌套列表 [['a', 'b', 'c'], ['d', 'e', 'f', 'g']] 类似java二维数组
    # print([x,y][0][1])
    # 指定插入位置
    # x.insert(3,y)
    # print(x)
    # 删除指定位置元素 返回删除的元素
    # temp= x.pop(0)
    # print(x)
    # 改变list中的元素后地址指向和原来一致
    # students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    # print(id(students))
    # students[0] = ('john1', 'C', '110')
    # print(id(students))
    #lambda表达式中第二个变量要和第一个变量对应
    # student_1 = sorted(students, key=lambda a: a[2],reverse=False)
    # print(student_1)
    # 列表使用了copy后会得到一个新的地址
    # students_copy = students.copy()
    # 和原变量使用同一个地址 （如果改变了值 原变量值也会随之改变）
    # students_1 = students
    # 分配新的地址
    # students_2 = students[:]
    # print(id(students_copy),id(students),id(students_1),id(students_2))
    # students_copy.clear()
    # print(students_copy)
    # 当元组中只有一个元素时 ，需要在元素后加上逗号 不然 括号会被当做运算符
    # 元组中的api和 list、str中大部分类似
    # a =('a')
    # print(type(a)) #会返回元素类型 而不是元组类型
    # b =('a',)
    # 空元组定义
    # b = ()
    # print(type(b))
    # 二维列表定义
    # list_2d = [[0 for col in range(5)]for row in range(7)]
    # print(list_2d)
    # '可变的'tuple
    # tuple_change = ('a', 'b', ['A', 'B'])
    # print(tuple_change)
    # tuple_change[2][0] = 'X'
    # tuple_change[2][1] = 'Y'
    # 打印出来的tuple的值改变了 ？？
    # 原因：tuple指向list的地址没变  但是list是可变的 在不改变地址的情况下 改变了自己存储的元素
    # print(tuple_change)
    # tuple_students1 = (('john', 'A', 215),('looper', 'd', 20))
    # tuple_students2 = (('jane', 'B', 2), ('dave', 'B', 10))
    # print(tuple_students1+tuple_students2)
    # print(sorted(tuple_students1+tuple_students2,key =lambda tuple_student:tuple_student[2]))
    # print((tuple_students1+tuple_students2)[1])
    # print((tuple_students1+tuple_students2)[-1])
    # print(len(tuple_students1+tuple_students2))
    # print(max(tuple_students1+tuple_students2,key=lambda student1:student1[2]))
    # print(min(tuple_students1+tuple_students2,key=lambda studen2:studen2[2]))
    # print(type(tuple(students)))
    # 定义已经存在的key会覆盖 ，不存在的会新建
    # 键不可变 所以只能使用数字、字符串、元组（定义完不可变） 不能使用列表（可变，并且没有hash方法，字典类型存储时底层采用hash算出存储位置）
    dic_1 = {'name':'looper','age':'25','address':'shanghai'}
    dic_2 = {'name':'looper1','age':'125','address':'shanghai1'}
    # dic_1['age'] = 55
    # dic_1['job'] = 'it'
    # print(dic_1)
    # del dic_2['name']
    # print(dic_2)
    # 删除所有元素
    # dic_2.clear()
    # print(dic_2)
    # 删除字典
    # del dic_2
    # print(dic_2)
    # dic_1_copy = dic_1.copy()
    # # print(dic_1_copy)
    # list_a = [1,"a"]
    # dic_1_copy = dic_1.fromkeys(list_a)
    # print(dic_1_copy)
    citys = {
        '北京': {
            '朝阳': ['国贸', 'CBD', '天阶', '我爱我家', '链接地产'],
            '海淀': ['圆明园', '苏州街', '中关村', '北京大学'],
            '昌平': ['沙河', '南口', '小汤山', ],
            '怀柔': ['桃花', '梅花', '大山'],
            '密云': ['密云A', '密云B', '密云C']
        },
        '河北': {
            '石家庄': ['石家庄A', '石家庄B', '石家庄C', '石家庄D', '石家庄E'],
            '张家口': ['张家口A', '张家口B', '张家口C'],
            '承德': ['承德A', '承德B', '承德C', '承德D']
        }
    }
    for i in citys['河北']:
        print(i)
    for i in citys['北京']['怀柔']:
        print(i)




