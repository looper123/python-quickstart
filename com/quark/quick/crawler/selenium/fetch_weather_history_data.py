from selenium import webdriver
from selenium.webdriver.common.by import By


# 爬取天气数据作为hadoop测试数据
class fetch_weather_data():
    url = "http://www.tianqihoubao.com/"
    driver = webdriver.Firefox()
    driver.get(url)

    def fetch_data(self):
        # if not os.path.exists("C:\\Users\\zhenpenglu\\Desktop\\1.txt"):
        #     os.mkdir("C:\\Users\\zhenpenglu\\Desktop\\1.txt")
        # url_files = open("C:\\Users\\zhenpenglu\\Desktop\\1.txt", 'w+')
        # if os.path.getsize("C:\\Users\\zhenpenglu\\Desktop\\1.txt") ==0:
        driver = self.driver
        all_province_links = driver.find_elements_by_css_selector("a")
        # 所有省份的url 列表
        province_list = []
        # 所有城市的url 列表
        city_list = []
        # 过滤获取所有省份对应的url
        for link in all_province_links:
            href = link.get_attribute("href")
            # 非空 && 格式过滤
            if href:
                if "http://www.tianqihoubao.com/weather/province.aspx?id=" in str(href):
                    province_list.append(href)
        if province_list:
            for province in province_list:
                # print(province)
                driver.get(province)
                all_city_links = self.driver.find_elements_by_css_selector("a")
                for link in all_city_links:
                    href = link.get_attribute("href")
                    # 非空 && 格式过滤
                    if href:
                        if "http://www.tianqihoubao.com/weather/top" in str(href):
                            # print(href)
                            city_list.append(href + '\n')
        # 把所有城市对应的地址写入文件
        # url_files.writelines(province_list)


def test_write():
    driver = webdriver.Firefox()
    url = "http://www.tianqihoubao.com/weather/top/anqing.html"
    driver.get(url)
    # 找出所有指定table下的所有tr
    table_tr_list = driver.find_element(By.CLASS_NAME, "b").find_elements(By.TAG_NAME, "tr")


if __name__ == '__main__':
    fetch_weather_data().fetch_data()
    # test_write()。
