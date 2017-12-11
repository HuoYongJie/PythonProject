
#coding=utf-8  //使用中文注释必须加在最上边
import os  #引入系统库
import urllib2  #引入系统网络库--->添加系统库流程
from  bs4 import BeautifulSoup  #引入网络解析框架


#Python2.7   爬取妹子图，单网页

# root_url = 'http://iyangzi.com/?p=173'
root_url = 'http://iyangzi.com/?p=173'

try:
    response = urllib2.urlopen(root_url)  #返回一个网络请求
    if response.getcode() == 200:
        girl_dir = '/Users/huoyongjie/Desktop/girl'    #文件夹地址，mac和windows地址写法有区别
        if not os.path.exists(girl_dir):
            os.mkdir(girl_dir)
        os.chdir(girl_dir)    #如果不存在，就创建文件夹
        soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')
        all_img = soup.find('div', class_='post-content').find_all('img') #find_all 返回一个数组,find()返回第一个tag
        count = 1
        for img in all_img:
            src = img['src']
            # print src
            name = 'iyangzi' + str(count)
            with open(name + '.jpg', 'ab') as img_object:
                img_content = urllib2.urlopen(src).read()
                img_object.write(img_content)
                img_object.flush()
            count += 1
except urllib2.URLError, e:
    print
    e