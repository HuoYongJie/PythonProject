#coding=utf-8

import os
import urllib2
from   urllib2 import URLError
import urlManager, htmlDown, htmlParser

class SpiderMain(object):
    def __init__(self):
        self.urls = urlManager.UrlManager()
        self.downloader = htmlDown.HtmlDownloader()
        self.parser = htmlParser.HtmlParser()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        girl_dir = '/Users/huoyongjie/Desktop/girl_4'
        if not os.path.exists(girl_dir):
            os.mkdir(girl_dir)
        os.chdir(girl_dir)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print new_url
                html_cont = self.downloader.download(new_url)
                new_urls, img_srcs = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)  # 将爬取的新的url添加到待爬取的url集合中

                # 保存获取到的妹子图
                for img in img_srcs:
                    src = img['src']
                    # print src
                    name = 'iyangzi' + str(count)
                    with open(name + '.jpg', 'ab') as img_object:
                        img_content = urllib2.urlopen(src).read()
                        img_object.write(img_content)
                        img_object.flush()

                    count += 1
            except URLError, e:
                print 'spider craw failed ', e


if __name__ == "__main__":
    root_url = "http://iyangzi.com/?p=21"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)