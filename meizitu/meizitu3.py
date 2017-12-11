
#coding=utf-8 多线程python

import os
import urllib2
import re
from bs4 import BeautifulSoup
import threading
import time
import random

#抓取所需内容
user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64)", 'Mozilla/5.0 (Windows NT 6.3; WOW64)',
              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
              'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
              'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
              'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
              'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
              'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']




# 将原来的I/O操作放到一个函数saveBeauty中,用来传给Thread类作为回调接口
def saveBeauty(url, count):
    name = 'iyangzi_' + str(count)
    with open(name + '.jpg', 'wb') as img_object:
        img_content = urllib2.urlopen(url).read()
        img_object.write(img_content)
        img_object.flush()


root_url = 'http://www.mzitu.com/61299/'  #加入反扒机制
new_urls = set()  # 新增加的url集合
crawed_urls = set()  # 已经爬取的url的集合
count = 1

girl_dir = '/Users/huoyongjie/Desktop/girl_1'
if not os.path.exists(girl_dir):
    os.mkdir(girl_dir)
os.chdir(girl_dir)

new_urls.add(root_url)  # 添加待爬取的起始url
start_time = time.time()
while len(new_urls) != 0:
    new_url = new_urls.pop()
    crawed_urls.add(new_url)
    print new_url
    try:

        for page in range(1, 20):

            send_headers = {

                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'keep-alive'
            }

            new_url = urllib2.Request(root_url, headers=send_headers)


            # request = urllib2.request_host(url=url, headers={
            #     "User-Agent": random.choice(user_agent)})  # 随机从user_agent列表中抽取一个元素

            time.sleep(random.randrange(1, 4))
        response = urllib2.urlopen(new_url)
        if response.getcode() == 200:
           soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')

            # 找到该页指向其它页面的且是新出现的url，添加到new_urls集合中供下一轮爬取
        urls = soup.find_all('a', href=re.compile(r"http://www.mzitu.com/61299"))
        for url in urls:
                # print url['href']
            if url['href'] not in new_urls and url['href'] not in crawed_urls:
                    new_urls.add(url['href'])

            all_img = soup.find('div', class_='main-image').find_all('img')

        for img in all_img:
                src = img['src']
                # print src
                threading.Thread(saveBeauty(src, count)).start()
                # 将原来的I/O操作放到一个函数saveBeauty中，然后作为回调接口传给Thread作为参数
                '''
                name = 'iyangzi_' + str(count)
                with open(name + '.jpg', 'ab') as img_object:
                    img_content = urllib2.urlopen(src).read()
                    img_object.write(img_content)
                    img_object.flush()
                '''
                count += 1
        time.sleep(random.randrange(1, 10))  # 每抓一页随机休眠几秒，数值可根据实际情况改动
    except urllib2.URLError, e:
        print e
end_time = time.time()
# 打印出程序运行时长
print 'total time is', end_time - start_time