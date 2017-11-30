# 在同一行书写多条语句用分号隔开
# import sys; x="多个句子间用分号隔开"; sys.stdout.write(x+"\n")


# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
expression = 3
a = -6
# if  expression ==1 :
#     print("a")
#     print("b")
# elif expression == 2:
#     # end="" 可以让print的内容不换行
#     print("a",end="")
#     print("b",end="")
# else:
#     input("\n\n按下回车键后退出。")
if __name__ == '__main__':
    print(id(a))
