# 使用chrom 连接需要下载并且安装chromdriver  地址http://npm.taobao.org/mirrors/chromedriver/
# 解压后把 geckodriver.exe放在 script文件夹下
# 火狐浏览器 driver下载 https://github.com/mozilla/geckodriver/releases
# 常见错误  1 没有对应的driver    2 not capablity  驱动和浏览器版本不匹配

# selenium键盘
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
# selenium 小用例
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


# 爬取网页下所有的图片
class fetch_all():

    # name = "mySpider"
    request_url = "https://www.hua.com/flower/?r=0&pg=2"
    driver = webdriver.Firefox()
    driver.get(request_url)

    # 图片下载(从当前页面开始抓取  无限抓取下去)
    def img_download(self):
        driver = self.driver
        # 图片  img src
        imgs = driver.find_elements_by_css_selector("img")
        # 跳转链接 href
        skip_links = driver.find_elements_by_css_selector("a")
        # 拼接规则  url+后缀
        imgs_downloads = []
        # 图片扩展名BMP、JPG、JPEG、PNG、GIF
        pic_suffix_list = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        # 图片
        for img in imgs:
            pic_url = img.get_attribute("src")
            if pic_url:
                for pic_suffix in pic_suffix_list:
                    if str(pic_url).find(pic_suffix) is not -1:
                        imgs_downloads.append(str(pic_url) + pic_suffix)
        # pic download
        # 判断非空
        if imgs_downloads:
            for pic in imgs_downloads:
                # 目录
                base_dir = "F:\\imgs"

                file_name = str(uuid.uuid1()) + pic[pic.rfind("."):]
                whole_path = base_dir + "\\" + file_name
                open(whole_path, "wb")
                # 去除None前缀的图片
                urlretrieve(pic[:pic.rfind(".")], whole_path)
        # 有链接可以跳转
        if skip_links:
            for skip_link in skip_links:
                href = skip_link.get_attribute("href")
                if href:
                    driver.get(href)
                    time.sleep(2)
                    self.img_download()
        else:
            return







 # 从百度图库下载 (小刮刮爬虫)
class fetch_from_baidu():
    name = "mySpider"
    print("请输入关键词")
    # key_word = input()
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

    # 视频下载
    def video_download(self):
        driver = self.driver
        # 跳转链接 href
        skip_links = driver.find_elements_by_css_selector("a")
        # 视频   video src
        vi_links = driver.find_elements_by_css_selector("video embed")
        # 视频或者音频  embed src
        # both_links = driver.find_elements_by_css_selector("embed")
        # 拼接规则  url+后缀
        video_downloads = []
        # 图片扩展名BMP、JPG、JPEG、PNG、GIF
        vi_suffix_list = ['.aiff', '.avi', '.mov', '.mpeg', '.mpg', '.qt', '.ram', '.viv']
        # 视频
        for vi_link in vi_links:
            vi_url = vi_link.get_attribute("src")
            for vi_suffix in vi_suffix_list:
                if str(vi_url).find(vi_suffix):
                    video_downloads.append(str(vi_url) + vi_suffix)
        # pic download
        # 判断非空
        if video_downloads:
            for video in video_downloads:
                # 目录
                base_dir = "F:\\videos"
                file_name = str(uuid.uuid1()) + video[video.rfind("."):]
                whole_path = base_dir + "\\" + file_name
                open(whole_path, "wb")
                urllib.urlopen('http://某piratebay.se/browse/200').read()
                # 去除None前缀的图片
                urlretrieve(video[:video.rfind(".")], whole_path)
        # 有链接可以跳转
        if skip_links:
            for skip_link in skip_links:
                href = skip_link.get_attribute("href")
                if href:
                    driver.get(href)
                    time.sleep(2)
                    self.video_download()
        else:
            return

    # 音频下载
    def music_download(self):
        driver = self.driver
        # 跳转链接 href
        skip_links = driver.find_elements_by_css_selector("a")
        # 音频     audio  src
        mus_links = driver.find_elements_by_css_selector("audio embed")
        # 视频或者音频  embed src
        # both_links = driver.find_elements_by_css_selector("embed")
        # 拼接规则  url+后缀
        music_downloads = []
        # 图片扩展名BMP、JPG、JPEG、PNG、GIF
        # 视频扩展名 aiff  avi  mov  mpeg  mpg qt  ram  viv
        # 音频扩展名 mp3 wma rm wav midi ape flac
        mus_suffix_list = ['.mp3', '.wma', '.rm', '.wav', '.midi', '.ape', '.flac']
        # 音频
        for mus_link in mus_links:
            mus_url = mus_link.get_attribute("src")
            for both_suffix in mus_suffix_list:
                if str(mus_url).find(both_suffix):
                    music_downloads.append((mus_url) + both_suffix)
        # pic download
        # 判断非空
        if music_downloads:
            for music in music_downloads:
                # 目录
                base_dir = "F:\\musics"

                file_name = str(uuid.uuid1()) + music[music.rfind("."):]
                whole_path = base_dir + "\\" + file_name
                open(whole_path, "wb")
                # 去除None前缀的图片
                urlretrieve(music[:music.rfind(".")], whole_path)
        # 有链接可以跳转
        if skip_links:
            for skip_link in skip_links:
                href = skip_link.get_attribute("href")
                if href:
                    driver.get(href)
                    time.sleep(2)
                    self.music_download()
        else:
            return


if __name__ == '__main__':
    # spm_search_func()
    # selenium_spider()
    # fetch_flower_pic()
    # fetch_img_origin()
    #  fetch_all().img_download()
    fetch_from_baidu().start_fetch()

