#! /usr/bin/env python  
# -*- coding: UTF-8 -*-  
import smtplib
from email.mime.text import MIMEText

mailto_list = ['ZhenpengLu@quarkfinance.com']  # 收件人(列表)
mail_host = "smtp.163.com"  # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_postfix = "163.com"  # 邮箱的后缀，网易就是163.com


def send_mail(to_list, sub, content):
    me = "hello" + "<" + "looper" + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)  # 将收件人列表以‘；’分隔
    try:
        # local_hostname  '70K5DF2VD6AVSSS.DHCP HOST'
        # 问题出在计算机名称设置上，这是由于某些smtp服务器不允许计算机名含有非ASCII字符。在TCP / IP设置中，你的计算机名字应该是简单的英文名
        # 字，例如abc等等，然后dns的后缀和你的所在dns域相同即可。改变一下计算机名称，马上就可以解决这个问题。注意，计算机名称不能使用中文、不要使
        # 用不常用的符号，而且应该包括完整的dns后缀。
        # (500, b'Error: bad syntax')
        server = smtplib.SMTP('192.168.194.128',25)
        server.login("root", "root")  # 登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__ == '__main__':
    if send_mail(mailto_list, "您的 Apple ID 被用于在 Web 浏览器上登录 iCloud", "网易邮箱给qq邮箱的一封信"):  # 邮件主题和邮件内容
        # 这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
        print("done!")
    else:
        print("failed!")
