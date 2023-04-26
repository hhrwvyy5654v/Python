import mechanicalsoup
from selenium import webdriver

br = webdriver.PhantomJS()

# 微信公众号Python小屋文章清单
with open('Python小屋文章清单.txt', encoding='utf8') as fp:
    articles = fp.readlines()
articles = tuple(map(str.strip, articles))

# 模拟打开指定网址，模拟输入并提交输入的关键字
browser = mechanicalsoup.StatefulBrowser()
browser.open(r'http://www.baidu.com')
browser.select_form('#form')
browser['wd'] = 'Python小屋'
browser.submit_selected()

# 获取百度前10页
top10Urls = []
for link in browser.get_current_page().select('a'):
    if link.text in tuple(map(str, range(2, 11))):
        top10Urls.append(r'http://www.baidu.com'+link.attrs['href'])

# 与微信公众号里的文章标题进行比对，如果非常相似就返回True
def check(text):
    for article in articles:
        # 这里使用切片，是因为有的网站在转发公众号文章里标题不完整
        # 例如把“使用Python+pillow绘制矩阵盖尔圆”的前两个字给漏掉了
        if article[2:-2].lower() in text.lower():
            return True
    return False

# 只输出密切相关的链接
def getLinks():
    for link in browser.get_current_page().select('a'):
        text = link.text
        if 'Python小屋' in text or '董付国' in text or check(text):
            br.get(link.attrs['href'])
            print(link.text, '-->', br.current_url)

# 输出第一页
getLinks()
# 处理后面的9页
for url in top10Urls:
    browser.open(url)
    getLinks()    
br.quit()
