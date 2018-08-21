import time
import urllib
import uuid
from urllib import request
from urllib.request import urlretrieve

import os
from selenium import webdriver
# selenium 小用例
from selenium.webdriver.common.keys import Keys


# 从百度图库下载
class fetch_from_baidu():
    name = "mySpider"
    baidu_img_url = "http://image.baidu.com/"
    driver = webdriver.Firefox()
    driver.get(baidu_img_url)

    # 图片下载(从当前页面开始抓取  无限抓取下去)
    def start_fetch(self):
        driver = self.driver
        # 放入搜索关键词后
        driver.find_element_by_id("kw").send_keys("LOL", Keys.ENTER)
        time.sleep(2)
        # 判断当imgs_item的数量不再增加时 退出循环
        flag = True
        # 下载列表长度
        imgs_download_len = 0
        while True:
            # 控制滚动条向下滑动
            driver.execute_script("window.scrollBy(0,10000);")
            time.sleep(2)
            # 图片  img src
            # 如果class之间有空格 不能直接写入参数中  selenium默认会把空格前后的值当成两个class name 来处理
            imgs_item = driver.find_elements_by_class_name("imgitem")
            # 跳转链接 href
            # 拼接规则  url+后缀
            imgs_downloads = []
            # 图片扩展名BMP、JPG、JPEG、PNG、GIF
            pic_suffix_list = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
            # 图片
            for img in imgs_item:
                pic_url = img.get_attribute("data-objurl")
                # 判断非空
                if pic_url:
                    for pic_suffix in pic_suffix_list:
                        if str(pic_url).find(pic_suffix) is not -1:
                            imgs_downloads.append(str(pic_url) + pic_suffix)
            # pic download
            # 判断非空
            if imgs_downloads:
                for pic in imgs_downloads[imgs_download_len:]:
                    # 目录
                    base_dir = "F:\\imgs"
                    file_name = str(uuid.uuid1()) + pic[pic.rfind("."):]
                    whole_path = base_dir + "\\" + file_name
                    open(whole_path, "wb")
                    my_url = pic[:pic.rfind(".")]
                    try:
                        # 自带的下载方法 超时时间太长  （不推荐）
                        # urlretrieve(my_url, whole_path)
                        response = urllib.request.urlopen(my_url,timeout=2)
                        cat_img = response.read()
                        with open(whole_path, 'wb') as f:
                            f.write(cat_img)
                    except  Exception as e:
                        # 处理无效、超时链接
                        print("下载出错"+str(e))
                        #删除建立的临时文件
                        os.remove(whole_path)
                        continue
            # 记录下载列表长度 下次从结束的地方下载
            imgs_download_len = imgs_downloads.__len__()

if __name__ == '__main__':
    fetch_from_baidu().start_fetch()