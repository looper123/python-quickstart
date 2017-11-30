import re

li = ["a", "b", "mpilgrim", "z", "example"]


if __name__ == '__main__':
     # 负数索引
     # print(li[-1])
     # 增加元素
     # li.append('append')
     # print(li)
     # li.insert(0,'insert')
     # print(li)
     # 注意 如果需要添加的元素没有放在元组中 会被拆分成单个字母放入
     # li.extend(['extends'])
     # print(li)
     # 移除第一个出现的指定元素
     # li.remove('example')
     # print(li)
     # 删除指定索引的元素 默认最后一个
     # print(li.pop(2))
     # print(li)
     #列表运算符
     # 产生了新的对象
     # print( li + ['append','insert'])
     # 没有产生新的对象
     # li += ['append','insert']
     # print(li)
     # 扩大三倍
     # li = li*3
     # print(li)
     #join 连接列表为字符串 生成新的字符串对象
     # li_str = "\\".join("%s" % (row) for row in li)
     # print(li_str)
     # 参数1 分割符  参数2 分割次数  默认到字符串结束 生成一个列表对象
     # print(li_str.split("\\",2))
    #列表映射  （列表推导式）
     # print([ele*2 for ele in [1,2,3]])
     #列表过滤 （列表推导式）
     # print([ele for ele in li if len(ele) >2])
     #正则表达式
     # match 需要在起始位置匹配成功 不然返回none
     # print(re.match("www", 'www.runoob.com').span()) #返回匹配到的字符串的start 和end
     # print(re.match("com", 'www.runoob.com'))
     # line = "Cats are smarter than dogs"
     # print(re.match(r'(.*) are (.*?) .*',line))
     # 匹配任意位置的 字符串
     # print(re.search("com", 'www.runoob.com').span())
     # 替换字符串  参数1 被替换的字符串 参数2 替换的字符串（可以是一个函数） 3 原始数据   4 替换次数
     # print(re.sub("com","cn",'www.runoob.com',1))
     phone = "2004-959-559 #这是一个电话号码"
     # 移除非数字
     # print(re.sub("\D","",phone))
     # 移除注释
     # print(re.sub("#.*$","",phone))
     # 替换以2 开头以4结尾的数据
     # print(re.sub(r"2.*4","",phone))





