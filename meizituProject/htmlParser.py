#coding=utf-8
import re
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        # print html_cont
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(soup)
        img_srcs = self.get_img_data(soup)
        return new_urls, img_srcs

    def get_new_urls(self, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"http://iyangzi.com/\?p=\d+$"))
        for link in links:
            new_urls.add(link['href'])
        return new_urls

    def get_img_data(self, soup):
        img_srcs = []
        all_img = soup.find('div', class_='post-content').find_all('img')
        for img in all_img:
            img_srcs.append(img)
        return img_srcs