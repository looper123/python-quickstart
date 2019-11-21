# python 基础教程 http://www.runoob.com/python3/python3-string.html
# python3.0 以上版本无需指定编码 默认为utf-8
# python中单双引号用法完全相同


def function():
    # print("你好python\n");
    # 在字符串前添加R 或者r 对后面的字符串进行转义
    print(R"你好python\n")
    print(r"你好python\n")
    # 在字符串前添加U 或者u 可以打印unicode 字符串
    print("this is an unicode字符串")


def function1(name):
    return('name',name)
    print('name', name)


def function2(name, age):
    print('name', name)
    print('age', 25)


# main方法只在当前模块运行
if __name__ == '__main__':
    function()
    function1('looper')
    function2('looper', 25)
else:
    print("import----helloword----main-----")
