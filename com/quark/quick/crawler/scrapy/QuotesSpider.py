# import scrapy
# from scrapy import cmdline
#
# #  scrapy实现爬虫
# class QuoteItem(scrapy.Item):
#
#     text = scrapy.Field()
#     author = scrapy.Field()
#     tags = scrapy.Field()
#
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     allowed_domains = ["quotes.toscrape.com"]
#     start_urls = ['http://quotes.toscrape.com/']
#
#     # 获取到相应数据
#     def parse(self, response):
#         quotes = response.css('.quote')
#         for quote in quotes:
#             item = QuoteItem()
#             item['text'] = quote.css('.text::text').extract_first()
#             item['author'] = quote.css('.author::text').extract_first()
#             item['tags'] = quote.css('.tags .tag::text').extract()
#             yield item
#
#         next = response.css('.pager .next a::attr("href")').extract_first()
#         url = response.urljoin(next)
#         # 循环
#         yield scrapy.Request(url=url, callback=self.parse)
#
#     # 父类已经处理 （从start_url 中打开连接） 可以不重写
#     # def start_requests(self):
#     #     pass
#
#
# if __name__ == '__main__':
#     # 按空格切割
#     cmdline.execute("scrapy runspider QuotesSpider.py".split())
