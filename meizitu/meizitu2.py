#coding=utf-8

import re
import os
import urllib2
from bs4 import BeautifulSoup

root_url = 'http://iyangzi.com/?p=21'
new_urls = set()  # 新增加的url集合
crawed_urls = set()  # 已经爬取的url的集合
count = 1

#爬取多个网页上的图片
girl_dir = '/Users/huoyongjie/Desktop/girl_more'
if not os.path.exists(girl_dir):
    os.mkdir(girl_dir)
os.chdir(girl_dir)

new_urls.add(root_url)  # 添加待爬取的起始url
while len(new_urls) != 0:
    new_url = new_urls.pop()
    crawed_urls.add(new_url)
    print new_url
    try:
        response = urllib2.urlopen(new_url)
        if response.getcode() == 200:
            soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')

            # 找到该页指向其它页面的且是新出现的url，添加到new_urls集合中供下一轮爬取
            urls = soup.find_all('a', href=re.compile(r"http://iyangzi.com/\?p=\d+$"))
            for url in urls:
                # print url['href']
                if url['href'] not in new_urls and url['href'] not in crawed_urls:
                    new_urls.add(url['href'])

            all_img = soup.find('div', class_='post-content').find_all('img')
            for img in all_img:
                src = img['src']
                # print src
                name = 'iyangzi_' + str(count)
                with open(name + '.jpg', 'ab') as img_object:
                    img_content = urllib2.urlopen(src).read()
                    img_object.write(img_content)
                    img_object.flush()
                count += 1

    except urllib2.URLError, e:
        print e