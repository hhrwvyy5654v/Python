import re
from selenium import webdriver

driver = webdriver.Edge()
city = input('请输入要查询的城市：').lower()
driver.get(r'http://openweathermap.org/find?q={0}'.format(city))
content = driver.page_source.lower()
driver.quit()
matchResult = re.search(r'<a href="(.+?)">\s+'+city+'.+?]', content)
if matchResult:
    print(matchResult.group(0))
else:
    print('查不到，请检查城市名字。')
