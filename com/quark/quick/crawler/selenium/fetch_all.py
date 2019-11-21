import time
import uuid
from urllib.request import urlretrieve

from selenium import webdriver


# selenium 小用例


# 爬取网页下所有图片
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


if __name__ == '__main__':
    fetch_all().img_download()
