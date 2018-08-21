# 操作步骤
# 火狐浏览器 driver下载 https://github.com/mozilla/geckodriver/releases
# 解压后把 geckodriver.exe放在 script文件夹下
# 运行错误  1 没有对应的driver    2 not capablity  驱动和浏览器版本不匹配   3 'geckodriver' executable needs to be in PATH  需要把浏览器内核放到本地环境变量
# 谷歌浏览器 driver下载 http://npm.taobao.org/mirrors/chromedriver/

# selenium操作对应的键盘的键位
# send_keys(Keys.SPACE)
# 空格键
# send_keys(Keys.TAB)
# 制表键
# send_keys(Keys.ESPACE)
# 回退键
# send_keys(Keys.ENTER)
# 回车键
# send_keys(Keys.CONTROL, 'a')
# 全选
# send_keys(Keys.CONTROL, 'c')
# 复制
# send_keys(Keys.CONTROL, 'x')
# 剪切
# send_keys(Keys.CONTROL, 'v')
# 粘贴
# send_keys(Keys.F1)
# F1
import time
import urllib
import uuid
from urllib import request
from urllib.request import urlretrieve

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class quick_start:
    def selenium_spider(self):
        little_time_stop = 1
        big_time_stop = 2
        # 默认广告条数
        ads_num_require = 8
        # 链接
        req_url = "http://www.haosou.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=%E9%B2%9C%E8%8A%B1"
        # 打开浏览器
        # browser = webdriver.Chrome()
        browser = webdriver.Firefox()
        # 开始请求
        browser.get(req_url)
        all_ads_li = browser.find_elements_by_css_selector("#e_idea_pp li")
        # 当前广告条数
        ads_num_current = len(all_ads_li)
        print("Has been got %d ads" % (ads_num_current))
        # 如果广告条数与默认不符
        if ads_num_current < ads_num_require:
            print("The number of ads is not enough ( current : %d require: %d)" % (ads_num_current, ads_num_require))
            # exit()
        # 获取顶部连接
        i = 0
        for ads_li in all_ads_li:
            time.sleep(big_time_stop)
            i = i + 1
            print("ads %d :" % i)
            try:
                main = ads_li.find_element_by_css_selector('h3 a')
            except:
                print("\tError: ads %d cann't find" % (i))
            else:
                print("\tReady: visit ads %d" % (i))
                main.click()
                print("\tSucess: visit ads %d" % (i))
                time.sleep(little_time_stop)
            try:
                img_link = ads_li.find_element_by_class_name('e_biyi_img')
            except:
                print("\tError : no img in ads %d " % (i))
            else:
                print("\tReady : visit img_link %d" % (i))
                img_link.click()
                print("\tSuccess : visit img_link %d" % (i))
                time.sleep(little_time_stop)
            try:
                child_div = ads_li.find_element_by_class_name('e_biyi_childLink');
            except:
                print("\tError : no child link in ads %d" % (i))
            else:
                try:
                    child_links = child_div.find_elements_by_css_selector('a')
                except:
                    print("\tError : find child_links error")
                else:
                    num_links = len(child_links)
                    print("\tSuccess : there are %d child_links" % (num_links))
                    j = 0
                    for child_a in child_links:
                        j = j + 1
                        print("\t\tReady : visit child link %d in ads %d" % (j, i))
                        child_a.click()
                        print("\t\tSuccess : visit child link %d in ads %d" % (j, i))

                        time.sleep(little_time_stop)
            print
            ("End and thanks for your using!")
            # 下面代码选择取消注释
            # 延时
            # time.sleep(5)
            # 关闭当前窗口
            # browser.close()
            # 关闭所有已经打开的窗口
            # browser.quit()


class downlaod_img:
    # 下载图片
    def fetch_flower_pic(self):
        # 图片列表
        pic_list = []
        url = "http://www.roseonly.com.cn/list/xianhuameigui.html?ozs=226719-2446"
        driver = webdriver.Firefox()
        driver.get(url)
        # imgs = driver.find_elements_by_class_name("li_img")
        # 定位div 下的img标签
        imgs = driver.find_elements_by_xpath("//div[@class='li_img']//img")
        for img in imgs:
            url = img.get_attribute("data-original")
            pic_list.append(url)
        # 下载
        for pic in pic_list:
            # 目录
            base_dir = "F:\\imgs"
            index = pic.rfind(".")
            pic_suffix = pic[index:]
            file_name = str(time.time()) + pic_suffix
            whole_path = base_dir + "\\" + file_name
            open(whole_path, "wb")
            urlretrieve(pic, whole_path)


class img_origin:
    # selenium获取出图片来源
    def fetch_img_origin(self):
        url = "http://image.baidu.com/"
        driver = webdriver.Firefox()
        driver.get(url)
        # 图片
        pic_base_url = "F:\\imgs"
        pic_name = "7a899e510fb30f2413295570c295d143ad4b0315.jpg"
        whole_url = pic_base_url + "\\" + pic_name
        # 上船图片
        driver.find_element_by_id("stfile").send_keys(whole_url)
        # 保证页面跳转成功
        time.sleep(3)
        # 此时的driver对象已经指向了新页面
        window_url = driver.current_url
        #   div  guess-newbaike-right
        #   div  guess-newbaike-text-link
        #   a  href
        href = driver.find_element_by_xpath(
            "//div[@class='guess-newbaike-right']//div[@class='guess-newbaike-text-link']//a"
        ).get_attribute("href")
        driver.get(href)


















