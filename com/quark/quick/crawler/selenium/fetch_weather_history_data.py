import time
import urllib
import uuid
from urllib import request
from urllib.request import urlretrieve

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 爬取天气数据作为hadoop测试数据
class  fetch_weather_data():
    url = "http://www.tianqihoubao.com/"
    driver = webdriver.Firefox()
    driver.get(url)
    def fetch_data(self):
        driver = self.driver
        all_a_links =  driver.find_elements_by_css_selector("a")
        # 过滤
        for link  in all_a_links:
            # weather / province.aspx?id = 340000
            href = link.get_attribute("href")
            if  str(href).find('weather/province.aspx?id =') :
                all_a_links.remove(link)
        for link in all_a_links:
            print(str(link.get_attribute("href")))

if __name__ == '__main__':
    fetch_weather_data().fetch_data()