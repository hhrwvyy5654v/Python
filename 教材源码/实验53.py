import re
import os
import os.path
import time
from urllib.request import urlopen

# 创建用来存放爬取结果文件的文件夹
dstDir = 'YuanShi'
if not os.path.isdir(dstDir):
    os.mkdir(dstDir)

# 爬取起始页面
startUrl = r'http://www.cae.cn/cae/html/main/col48/column_48_1.html'
# 读取网页内容
with urlopen(startUrl) as fp:
    content = fp.read().decode()

# 提取并遍历每位大牛链接
pattern = r'<li class="name_list"><a href="(.+)"'\
           +' target="_blank">(.+)</a></li>'
result = re.findall(pattern, content)

# 爬取每位院士的简介和照片
for item in result:
    perUrl, name = item
    print('正在爬取{}...'.format(perUrl))
    name = os.path.join(dstDir, name)
    perUrl = r'http://www.cae.cn/' + perUrl
    with urlopen(perUrl) as fp:
        content = fp.read().decode()
    # 抓取照片并保存为本地图片文件
    pattern = r'<img src="/cae/admin/upload/(.+)" style='
    result = re.findall(pattern, content, re.I)
    if result:
        picUrl = r'http://www.cae.cn/cae/admin/upload/{0}'
        picUrl = picUrl.format(result[0].replace(' ', r'%20'))
        with open(name+'.jpg', 'wb') as pic:
            pic.write(urlopen(picUrl).read())            
    # 抓取简介并写入本地文本文件
    pattern = r'<p>(.+?)</p>'
    result = re.findall(pattern, content)
    if result:
        intro = re.sub('(<a.+</a>)|(&ensp;)|(&nbsp;)',
                       '',
                       '\n'.join(result))
        with open(name+'.txt', 'w', encoding='utf8') as fp:
            fp.write(intro)
