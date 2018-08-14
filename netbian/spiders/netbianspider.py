# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy import Request
from lxml import etree
from netbian._header import getHeaders  #将_header.py 中的getHeader引入
import re                               #正则
import os
from netbian import Color


class NetbianSpider(scrapy.Spider):
    name = 'netbianspider'                                  #名字
    #allowed_domains = ['http://pic.netbian.com']           #限制爬虫
    index = 'http://pic.netbian.com'                        #构造url使用得主页url
    start_urls = ['http://pic.netbian.com/index_250.html']  #开始爬去链接
    storePath = r'E:\picture'                               #保存路径
    next_page = ''                                          #保存下一页得url
    page_num = 0                                            #保存爬取页码数

    #请求并返回网页源码
    def getHTMLText(self,url):
        headers =getHeaders()                               #获得一个header  函数位于 _header.py 文件中
        try:
            r = requests.get(url,headers=headers, timeout=2)
            r.raise_for_status()
            return r.content
        except:
            #print('\n'+ url, 'requests error...\n')
            Color.printRed(u"\n{0}:requests error...\n".format(url))
            #打印错误信息     printRed函数位于Color.py文件中

    #传入图片的url、名字、类别
    #请求并保存图片
    def pictureStore(self,picture_url,picture_name,picture_class):
        picture_name = re.sub(r'[\/\\\:\*\?\"\<\>\|]', ' ', picture_name)
        #用正则去掉非法命名符号
        url = self.index + picture_url      #构造图片url
        html_content = self.getHTMLText(url)
        if html_content is not None:          #判断requests返回是否为空
            if not os.path.exists(self.storePath +'\{0}'.format(str(picture_class))):
                os.mkdir(self.storePath +'\{0}'.format(str(picture_class)))
                #判断图片类别是否存在
            with open('{0}\{1}\{2}{3}'.format(self.storePath, str(picture_class), picture_name,'.jpg'), 'wb') as f:
                f.write(html_content)
                #保存图片

    def parse(self, response):
        html_content = etree.HTML(response.text)
        html_url = html_content.xpath("//ul[@class='clearfix']/li/a[@target='_blank']/@href")
        #从主页中切出图片单独所在的页面的url   返回一个list
        self.next_page = self.index + html_content.xpath("//a[contains(text(), '下一页')]/@href")[0]
        #切出下一页的url
        count = re.findall(r'index_(\d*).html', self.next_page)
        #获得页码数
        #print("当前进度：{:.2f}%'.format(int(count[0]) * 100 / 1035)\n")
        Color.printYellowRed(u"\n当前进度：{0:.2f}%    第 {1:} 页\n".format(int(count[0]) * 100 / 1035,int(count[0])))
        #打印进度  printYellowRed 函数位于 Color.py
        for url in html_url:                            #遍历list
            url = self.index + url                      #构造图片单独所在的页面的url
            html_PicturePage = self.getHTMLText(url)    #获得网页源码
            if html_PicturePage is not None:            #判断是否为空

                html_content = etree.HTML(html_PicturePage)   #etree处理

                #切出图片的url、名字、类别
                picture_url = html_content.xpath("//div/a[@target='_blank']/img/@src")[0]
                picture_name = html_content.xpath("//div/a[@target='_blank']/img/@title")[0]
                picture_class = html_content.xpath("//div/span/a/text()")[1]

                self.pictureStore(picture_url, picture_name, picture_class)
                #保存
            else:
                html_url.append(url)                  #为空时再次加入list

        #print(self.next_page)
        if self.next_page is not None:
            yield Request(self.next_page, headers=getHeaders(), callback=self.parse)
            #callback自身  当next_page为空时结束爬取
        else:
            print('爬取结束')

