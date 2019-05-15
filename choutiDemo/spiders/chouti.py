# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChoutiSpider(CrawlSpider):
    name = 'chouti'
    # allowed_domains = ['dig.chouti.com']
    start_urls = ['https://dig.chouti.com/']
    # 实例化了一个连接提取器,用来提取指定的url，allow赋值一个正则表达式，
    # 链接提取器根据正则在页面中提取指定的链接，提取到的链接会全部交给规则解析器
    link = LinkExtractor(allow=r'all/hot/recent/\d+')
    # 实例化了一个规则解析器：
    # 接收链接提取器发送的连接后，（去除重复的链接）会对链接发起请求，获取对应页面数据
    # callback:指定一个解析规则，（方法函数）
    # follow：是否将链接提取器继续作用到提取出来的连接所表示的页面中
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        print(response)
        return i
