#json类型与各个类型间的转换
import json


# convert dic to json and repalce
import time

# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

class  JsonConverter():
    def dict_to_json(self):
        data = {
            'no': 1,
            'name': 'Runoob',
            'url': 'http://www.runoob.com'
        }
        print("after convert to json 数据{}/类型{}".format(json.dumps(data),type(json.dumps(data))))
        print("after convert to dict 数据{}/类型{}".format(json.loads(json.dumps(data)),type(json.loads(json.dumps(data)))))


class TimeConverter():
    def time_to_str(self):
        # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        print(type(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))

    def str_to_time(self):
        a = "Sat Mar 28 22:24:24 2016"
        time_data = time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
        print(time_data)
        print(type(time_data))


if __name__ == '__main__':
    # JsonConverter().dict_to_json()
    # 第一次调用返回运行的实际时间
    ctime = time.time()
    print("第一次调用",time.clock(),ctime)
    TimeConverter().str_to_time()
    TimeConverter().time_to_str()
    # 第二次以及以后的调用会返回和第一次调用之间的时间差 比time.time()更为精确
    print("第二次调用",time.clock(),time.time()-ctime)
    print("第三次调用",time.clock(),time.time()-ctime)
