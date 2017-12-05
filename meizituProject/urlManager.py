# coding=utf-8

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 新增加的待爬取的url集合
        self.crawed_urls = set()  # 已爬取的url集合

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.crawed_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        # 爬取一个url时将该url添加到已访问的url集合中表示该url已经访问过
        new_url = self.new_urls.pop()
        self.crawed_urls.add(new_url)
        return new_url