import os
import os.path
import sys
from functools import reduce

from com.quark.quick.start import HelloWorld


# 1）如果不是txt文件，建议用wb和rb来读写。通过二进制读写，不会有换行问题。
# 2）如果需要明文内容，请用rU来读取（强烈推荐），即U通用换行模式（Universal new line mode）。
# 该模式会把所有的换行符（\r \n \r\n）替换为\n。只支持读入，但是也足够了。这是Python 提供给我们的最好的选择，没有之一。


class MyClass:
    """一个简单的类实例"""
    i = 666666

    def f(self):
        return 'hello world'


# 继承的类放在当前类的参数位置（继承类的类名），多继承就是多个参数
class MyError(Exception):
    error_no = 123

    # 类似于java的构造方法

    def __init__(self, value):
        self.value = value

    # 子类重写父类的方法
    def __str__(self):
        print("exception occurred in MyError")
        return repr(self.value)


class SelfTest:
    # 类中的方法和普通方法的区别 （默认第一个参数是是自己类的实例 参数名随意）
    # < __main__.SelfTest  object at 0x00000159627A74A8 >
    # < class '__main__.SelfTest'>
    # 私有方法
    __weight = 100

    def __private_method(self):
        print("this is a private method")

    def print_self(self):
        print(self)
        print(self.__class__)
        # 如何访问本类的私有成员变量 格式： self.变量名
        # 外部访问私有变量/方法会报错 ： object has no attribute '变量/方法'
        print(self.__weight)
        # 访问私有方法 self.方法名
        self.__private_method()


# 运算符重载(对类的专有方法进行重载)
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 自定义实例化Vector类后返回的结果
    def __str__(self):
        return 'Vector(%d,%d)' % (self.a, self.b)

    # 两个vector对象之间使用加号时 会按照自定义算法来计算
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


# 判断是否为数字
def is_number(a):
    try:
        float(a)
        return True
    except:
        pass
    return False


def exception_handler():
    try:
        f = open('C:\\Users\\Administrator\\Desktop\\1.txt')
        s = f.readline()
        i = int(s.strip())
    # 程序抓取到第一个异常后会退出
    except OSError as err:
        print("OS error: {0}".format(err))
    # except ValueError:
    #     print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        # 再次把异常抛出
        raise MyError('mistake')
    # 放在所有的except语句之后 并且在try没有任何异常的情况下执行
    # 可以抓取并且处理try没有捕获的异常
    else:
        print("have no exception!!")
    # 清理行为
    finally:
        print("finally will execute finally code")


# 实例化类(包括了当前文件和其他文件 不加括号)
x = MyClass
y = HelloWorld
# 如果实例的类中有init函数 需要在定义的时候初始化init函数中的参数 不然会报错
z = MyError(1 * 2)


def directory_iterator(url):
    try:
        dir_list = os.listdir(url)
        for dir in dir_list:
            absolute_path = os.path.join(url, dir)
            if os.path.isdir(absolute_path):
                directory_iterator(absolute_path)
            elif absolute_path.endswith(".py"):
                print(absolute_path)
    # 多个异常用元组包装
    except (RuntimeError, TypeError, NameError):
        print("exception occurred!!")


if __name__ == '__main__':
    # url = input("输入路径后回车")
    # url = "H:\pycharm workspace"
    # directory_iterator("H:\pycharm workspace")
    # 设置文件的打开方式
    # file01 = open("C:\\Users\\Administrator\\Desktop\\1.txt", 'r')
    # 获取文件的权限（和文件的打开方式权限区分 这里是文件创建时候赋的权限）
    # os.chmod("C:\\Users\\Administrator\\Desktop\\1.txt",S_IWUSR)
    # print(os.access("C:\\Users\\Administrator\\Desktop\\1.txt",os.W_OK))
    # fd = os.open("C:\\Users\\Administrator\\Desktop\\1.txt",os.O_RDWR|os.O_CREAT)
    # fd2 = os.dup(fd)
    # 使用复制的文件描述符写入文件
    # os.write(fd2, b"This is test")
    # 关闭文件
    # os.closerange(fd, fd2)
    # 一定要关闭流
    # exception_handler()
    # 预定义的清理行为.
    # with open("C:\\Users\\Administrator\\Desktop\\1.txt") as f:
    #     for line in f:
    #         print(line, end="")
    # print(x.i)
    # print(z.error_no)
    # print(HelloWorld.function1("helloworld funcation1"))
    # test = SelfTest()
    # test.print_self()
    # __*代表类中的私有属性 在类的外部无法直接访问
    # print(test.__weight)
    # v1 = Vector(1,2)
    # 返回结果：Vector(5,7)
    # v2 = Vector(4,5)
    # vector类中的add函数进行重新定义 以得出自己想要的结果
    # 结果 ：Vector(5,7)
    # print(v1.__add__(v2))
    # 加号会自动映射成类的专有方法__add__()
    # print(v1+v2)
    # python 标准库
    # 返回当前工作目录
    # os.getcwd()
    # 切换到指定工作目录
    # os.chdir("C:\\Users\\Administrator\\Desktop")
    # 执行系统命令（指的是当前系统）
    # os.system("mkdir monday")
    # 拷贝、并且移动文件的功能（原文件不会消失）
    # shutil.copy("C:\\Users\\Administrator\\Desktop\\1.txt","C:\\Users\\Administrator\\Desktop\\1_copy.txt")
    # 移动文件（原文件会消失）
    # shutil.move("C:\\Users\\Administrator\\Desktop\\1.txt","C:\\Users\\Administrator\\Desktop\\friday")
    # windows 系统的删除文件夹以及下子文件的命令
    # os.system("RD /S friday")
    # 查看os文件的目录结构
    # print(dir(os))
    # print(help(os))
    # 可以从指定路径下根据自定义规则搜索文件组成列表
    # print(glob.glob("*.py"))
    # stdout 被重定向后 可以使用stdin、stdout、stderr 来显示警告和错误信息
    # sys.stderr.write("Warning, log file not found starting a new one\n")
    # 程序终止
    # sys.exit()
    # re 模块为字符串处理提供了大量的工具  \b 在字符串中表示退格  在正则中表示单词间隔
    # print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
    # math 提供了底层为c的函数库
    # print(math.log(1024,2))
    # print(random.choice(["test","test1","test2","test4","test5"]))
    # 访问网页
    # for line in urllib.request.urlopen('https://www.cnblogs.com/liqforstudy/p/5652517.html'):
    #     line = line.decode('utf-8')  # Decoding the binary data to text.
    #     if 'test' in line or 'zero' in line:  # look for Eastern Time
    #      print(line)
    # 时间日期处理
    # print(date.today())
    # print(date.today().strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
    # date arithmetic support
    # print((date.today()-date(1992,3,12)))
    # s = '压缩类测试压缩类测'
    # s_encode = s.encode("utf-8",errors='strict')
    # print(len(s_encode))
    # 后面的参数表示压缩度和压缩效率的数值 从0-9  压缩速度降低 但是压缩度上升 0 表示不压缩 -1 默认 取的是效率和度的适中值 6
    # 压缩时的数据量不宜过小 不然压缩后的值反而变大 原因：压缩的原理是把相同的值放在同一个位置，并同时给该位置一个标识符，
    # 当数据量过小时，多出的标识符占有的空间超过了减少的空间 从而导致文件反而变大了
    # s_com = zlib.compress(s_encode,-1)
    # print(len(s_com))
    # print(len(s_com))
    # print(zlib.decompress(zlib.compress(s_encode)).decode("utf-8",errors='strict'))
    # 代码性能测试类
    # 参数说明 stmt：执行语句  setup ：需要导入的模块 repeat ：重复测试的次数  number ：每个测试中执行语句的次数
    # print(Timer('date.today()','from datetime import date').timeit(3))
    # print(is_number(341414))
    # reduce + lambda 表达式实现阶乘1*2*3
    # reduce 用法: 会对sequence(包括 列表 、元组、range())中的每一个元素依次进行lambda表达式中的操作
    print(reduce(lambda x, y: x * y, range(1, 4)))
    print(reduce(lambda x, y: x * y, [1, 2, 3]))
    print(reduce(lambda x, y: x * y, (1, 2, 3)))
