import pymysql
import scrapy
from scrapy.http import Request
import web
import time


# mysql+ python 连接测试
def connect_mysql_test():
    db = pymysql.connect("192.168.194.128", "root", "root", "TESTDB")

    # 使用 cursor() 方法创建一个操作游标对象
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 预处理语句
    # sql = """CREATE TABLE EMPLOYEE_COPY (
    #      FIRST_NAME  CHAR(20) NOT NULL,
    #      LAST_NAME  CHAR(20),
    #      AGE INT,
    #      SEX CHAR(1),
    #      INCOME FLOAT )"""
    first_name = 'lzp'
    age = 22
    # sql = "select * from EMPLOYEE where first_name ='%s' and age ='%d'"%(first_name,age); #sql-1
    # sql = "select * from EMPLOYEE where first_name ='%s' and age ='%d'" #sql-2
    sql = "select * from EMPLOYEE "\
          "where first_name ='{}' and age ='{}'"  # sql-3
    try:
        # 使用 fetchone() 方法获取单条数据.
        # data = cursor.fetchone()
        # data_create = cursor.execute(sql%(first_name,age))
        data_create = cursor.execute(sql.format(first_name, age))  # 对应sql-3
        # 获取多条数据
        employ_list = cursor.fetchall();
        print(type(employ_list))  # 多条数据以元组的形式返回
        for employ in employ_list:
            print(type(employ))  # 元组里的每一条数据的各个字段的组成也是元组
            print(employ)
        # 如果执行增删改操作 需要提交事务
        db.commit()
        # 关闭数据库连接
        db.close()
    except:
        # 异常回滚
        db.rollback()


if __name__ == '__main__':
    connect_mysql_test()
