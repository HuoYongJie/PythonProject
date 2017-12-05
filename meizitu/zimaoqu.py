
#coding=utf-8

#爬取开封规划局网站的图片，单网页,这里的图片放的是a标签
import os   #调用系统自带功能
import urllib2 #网络请求类
import re  #正则校验
from  bs4 import BeautifulSoup #网络解析类


new_urls = set()  # 新增加的url集合
crawed_urls = set()  # 已经爬取的url的集合
count = 1
#Python2.7
root_url = 'http://www.kfghj.gov.cn/ghgs/ShowArticle.asp?ArticleID=949'
try:
    response = urllib2.urlopen(root_url)
    if response.getcode() == 200:
        girl_dir = '/Users/huoyongjie/Desktop/自贸区'
        if not os.path.exists(girl_dir):
            os.mkdir(girl_dir)
        os.chdir(girl_dir)
        soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')


        # 找到该页指向其它页面的且是新出现的url，添加到new_urls集合中供下一轮爬取
        urls = soup.find_all('a', href=re.compile("/ghgs/UploadFiles_5282/201710/"))
     
        for img in urls:

            src1 = "http://www.kfghj.gov.cn" + img['href']
            # print src
            name = '自贸区' + str(count)
            with open(name + '.jpg', 'ab') as img_object:
                img_content = urllib2.urlopen(src1).read()
                img_object.write(img_content)
                img_object.flush()
            count += 1
    else:
        print  "qq";
            # print src
except urllib2.URLError, e:
    print
    e

    #这种操作比较耗时，只能一个一个图片进行操作