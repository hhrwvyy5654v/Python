# -*- encoding: utf-8 -*-
'''
@File    :   Jobui_crawler.py
@Time    :   2022/05/25 15:24:01
@Author  :   HuangRongQuan 
@Version :   1.0
@Contact :   huang_rongquan@outlook.com
'''
import os  # 文件操作
import time  # 设置休眠时间
import random  # 随机选择
import pandas  # excel读写
import requests  # 处理url
from bs4 import BeautifulSoup  # 从网页抓取数据
from lxml import etree  # 将element对象转化为字符串


class Website:
    """_获取网站url和虚拟user-agent_

    user-agent:User-Agent中文名为用户代理,简称 UA,是一个特殊字符串头,
    使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、
    浏览器渲染引擎、浏览器语言、浏览器插件等。网站可以通判断 UA 来给不
    同的操作系统、不同的浏览器发送不同的页面,对于爬虫来说,UA就是标明身
    份的第一层标识。 
    """

    def __init__(self):
        # 初始化方法中保存需要爬取的网站名称和地址
        self.__url_list = {
            'zhiyou': 'https://www.jobui.com',
        }

        # 一直使用同一个User-Agent很容易被网站识别为通过相同浏览器频繁访问而识别为爬虫程序,一般通过使用多个User-Agent随机调用的方式,避免一个请求头长时间访问。
        self.__user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
            "Opera/8.0 (Windows NT 5.1; U; en)",
            "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Macintosh; U; IntelMac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

    # 使用random的方式随机调用浏览器信息列表中的User-Agent，可以有效避免同一个请求头访问网站
    def get_headers(self):
        return {'User-Agent': random.choice(self.__user_agent_list)}

    # 获取职友集url
    def get_zhiyou(self):
        return self.__url_list['zhiyou']


class Recruit:
    """_招聘信息_
    """

    def __init__(self):
        self.title = ''  # 岗位名称
        self.experience = ''  # 经验要求
        self.education = ''  # 学历要求
        self.salary = ''  # 薪资待遇
        self.company = ''  # 公司名称
        self.page_views = ''  # 浏览量
        self.industry = ''  # 所属行业
        self.company_size = ''  # 公司规模
        self.responsibilities = ''  # 岗位职责
        self.source_website = ''  # 来源网站
        self.update_time = ''  # 更新时间
        self.logo_information = ''  # logo信息

    # 简单规格化爬虫信息:移除字符串头尾指定的字符(默认为空格或换行符)
    def format(self, info):
        self.title = info[0].strip()
        self.experience = info[1].strip()
        self.education = info[2].strip()
        self.salary = info[3].strip()
        self.company = info[4].strip()
        self.page_views = info[5].strip()
        self.industry = info[6].strip()
        self.company_size = info[7].strip()
        self.city = info[8].strip()
        self.responsibilities = info[9].strip()
        self.source_website = info[10].strip()
        self.update_time = info[11].strip()
        self.logo_information = info[12].strip()

    # 返回一行以逗号分割的字符串(7个主要信息)
    def get_main_str(self):
        s = r''
        s += str(self.title) + ','
        s += str(self.experience) + ','
        s += str(self.education) + ','
        s += str(self.salary) + ','
        s += str(self.company) + ','
        s += str(self.page_views) + ','
        s += str(self.city) + '\n'
        return s


class File_operation:
    """_文件操作_
    """

    def __init__(self):
        self.job_col = ['岗位名称', '经验要求', '学历要求', '薪资待遇', '公司名称', '浏览量', '所属行业',
                        '公司规模', '城市', '岗位职责', '来源网站', '更新时间', 'logo信息']
        self.job_content = {'岗位名称': [], '经验要求': [], '学历要求': [], '薪资待遇': [], '公司名称': [], '浏览量': [], '所属行业': [],
                            '公司规模': [], '城市': [], '岗位职责': [], '来源网站': [], '更新时间': [], 'logo信息': []}

    # 添加一个job信息到txt
    def save_job_txt(self, file_path, job):
        content = [job.get_main_str()]
        Txt_process().append_file(file_path, content)

    # 从txt中读取jobs信息
    def load_jobs_txt(self, file_path):
        info_list = Txt_process().read(file_path)
        return info_list

    # 一次写入jobs信息到txt
    def save_jobs_txt(self, file_path, jobs):
        content = []
        for job in jobs:
            content.append(job.get_main_str())
        Txt_process().write(file_path, content)

    # 从excel中读取jobs信息
    def load_jobs_excel(self, file_path):
        jobs = []
        df = Excel_process().read_excel(file_path)
        for item in df.values:
            job = Recruit()
            job.title = item[0]
            job.experience = item[1]
            job.education = item[2]
            job.salary = item[3]
            job.company = item[4]
            job.page_views = item[5]
            job.industry = item[6]
            job.company_size = item[7]
            job.city = item[8]
            job.responsibilities = item[9]
            job.source_website = item[10]
            job.update_time = item[11]
            job.logo_information = item[12]
            jobs.append(job)
        return jobs

    # 一次写入jobs信息到excel
    def save_jobs_excel(self, file_path, jobs):
        col = self.job_col
        content = self.job_content
        for job in jobs:
            content['岗位名称'].append(job.title)
            content['经验要求'].append(job.experience)
            content['学历要求'].append(job.education)
            content['薪资待遇'].append(job.salary)
            content['公司名称'].append(job.company)
            content['浏览量'].append(job.page_views)
            content['所属行业'].append(job.industry)
            content['公司规模'].append(job.company_size)
            content['城市'].append(job.city)
            content['岗位职责'].append(job.responsibilities)
            content['来源网站'].append(job.source_website)
            content['更新时间'].append(job.update_time)
            content['logo信息'].append(job.logo_information)
        Excel_process().create_excel(file_path, content, col)

    # 添加一个job信息到excel
    def save_job_excel(self, file_path, job):
        if not os.path.exists(file_path):
            Excel_process().create_excel(file_path, self.job_content, self.job_col)
        content = self.job_content
        content['岗位名称'] = job.title
        content['经验要求'] = job.experience
        content['学历要求'] = job.education
        content['薪资待遇'] = job.salary
        content['公司名称'] = job.company
        content['浏览量'] = job.page_views
        content['所属行业'] = job.industry
        content['公司规模'] = job.company_size
        content['城市'] = job.city
        content['岗位职责'] = job.responsibilities
        content['来源网站'] = job.source_website
        content['更新时间'] = job.update_time
        content['logo信息'] = job.logo_information
        Excel_process().append_excel(file_path, content)


class Txt_process:
    """_txt文件处理_
    """

    def __init__(self):
        self.file_content = ''

    # 读取文件 file_path 文件路径
    def read(self, file_path):
        with open(file_path, 'r', encoding='utf8') as file:
            self.file_content = file.readlines()
        return self.file_content

    # 保存文件 file_path 文件路径 content内容列表
    def write(self, file_path, content):
        with open(file_path, 'w', encoding='utf8') as file:
            file.writelines(content)

    # 添加模式 file_path 文件路径 content内容列表
    def append_file(self, file_path, content):
        with open(file_path, 'a', encoding='utf8') as file:
            file.writelines(content)

    # 获取以逗号分割的信息列表
    def get_list_by_comma(self, file_path):
        self.read(file_path)
        info = ''
        for item in self.file_content:
            info += ''.join(item).strip()
        return info.replace(',', ',').strip().split(',')


class Excel_process:
    """_excel表格处理_
    """
    # 创建excel表

    def create_excel(self, file_path, content, col):
        df = pandas.DataFrame(content, columns=col)
        df.to_excel(file_path, index=False)

    # 读取excel表
    def read_excel(self, file_path):
        df = pandas.read_excel(file_path)
        return df

    # 向Excel表中添加数据
    def append_excel(self, file_path, content):
        df = self.read_excel(file_path)
        df = df.append(content, ignore_index=True)
        df.to_excel(file_path, index=False)

    # 获取Excel某一列数据
    def get_list_by_column(self, file_path, col_idx):
        df = pandas.read_excel(file_path, usecols=[col_idx])
        content = []
        for item in df.values:
            content.append(item[0])
        return content


class Reptile:
    """_爬虫_
    """

    def __init__(self, url='', headers={'User-Agent': ''}, sleep_time=3):
        self.url = url
        self.headers = headers
        self.sleep_time = sleep_time

    # 获取lxml的etree
    def get_lxml_etree(self):
        while True:
            self.headers = Website().get_headers()
            resp = requests.get(self.url, headers=self.headers)
            time.sleep(self.sleep_time)
            if resp.status_code == 200:
                context = resp.text
                return etree.HTML(context)

    # 获取bs4的soup
    def get_bs4_soup(self):
        while True:
            self.headers = Website().get_headers()
            resp = requests.get(self.url, headers=self.headers)
            time.sleep(self.sleep_time)
            if resp.status_code == 200:
                context = resp.text
                return BeautifulSoup(context, 'html.parser')


class Crawlers(Reptile):
    """_爬取招聘信息_
    """

    def __init__(self, view_pages=1):
        Reptile.__init__(self)
        # 爬取页面总数
        self.view_pages = view_pages
        self.jobs = []
        self.try_count = 0
        self.error_info = []

    # 获取爬取的url列表
    def get_url_list(self):
        self.url = Website().get_zhiyou()
        city_list = Txt_process().get_list_by_comma(
            Filepath().get_filepath(Filepath().read_city_txt))
        title_list = Txt_process().get_list_by_comma(
            Filepath().get_filepath(Filepath().read_title_txt))
        pages_count = self.view_pages
        url_list = []
        # 遍历搜索关注岗位、热门城市
        for title in title_list:
            for city in city_list:
                for i in range(pages_count):
                    # 访问网页，比如www.jobui.com/jobKw=java&cityKw=深圳&n=1
                    url = self.url + \
                        '/jobs?jobKw={}&cityKw={}&n={}'.format(
                            title, city, i + 1)
                    url_list.append(url)
        return url_list

    # 使用lxml从职友集爬取信息
    def get_info_by_lxml(self):
        url_list = self.get_url_list()
        info_list = []
        for url in url_list:
            lists = []
            flag = 0
            city = [url[url.find('cityKw='):url.find('&n=')].lstrip('cityKw=')]
            while len(lists) == 0 and flag < 5:
                flag += 1
                reptile = Reptile(url)
                my_etree = reptile.get_lxml_etree()
                lists = my_etree.xpath('//div[@class="c-job-list"]')
            for item in lists:
                self.try_count += 1
                # 两个url可能会出错
                try:
                    info = [item.xpath('./div[@class="job-content-box"]/div[@class="job-content"]/div[1]/a/h3'),  # 岗位名称
                            item.xpath(
                                './div[@class="job-content-box"]/div[@class="job-content"]/div[2]/div/span[1]'),  # 经验要求
                            item.xpath(
                                './div[@class="job-content-box"]/div[@class="job-content"]/div[2]/div/span[2]'),  # 学历要求
                            item.xpath(
                                './div[@class="job-content-box"]/div[@class="job-content"]/div[2]/div/span[3]'),  # 薪资待遇
                            item.xpath(
                                './div[@class="job-content-box"]/div[@class="job-content"]/div[3]/a'),  # 公司名称
                            item.xpath('./div[@class="job-content-box"]/div[@class="job-content"]/div[4]/span')]  # 浏览量
                    url1 = self.url + \
                        item.xpath(
                            './div[@class="job-content-box"]/div[@class="job-content"]/div[1]/a/@href')[0]
                    self.get_info2_by_lxml(url1, info, city)

                    # 对爬取的信息进行切片处理
                    for i in range(len(info)):
                        if len(info[i]) == 0:
                            info[i] = ''
                        elif isinstance(info[i][0], str):
                            info[i] = info[i][0]
                        else:
                            info[i] = info[i][0].xpath('string(.)')
                    info_list.append(info)

                    job = Recruit()
                    job.format(info)
                    File_operation().save_job_txt(Filepath().get_filepath(
                        Filepath().write_salary_copy_txt), job)
                    File_operation().save_job_excel(Filepath().get_filepath(
                        Filepath().write_salary_copy_xlsx), job)

                except Exception as e:
                    self.error_info.append(e)
        return info_list

    # 爬取第2个网页的信息
    def get_info2_by_lxml(self, url, info, city):
        lists = []
        flag = 0
        my_etree = None
        while len(lists) == 0 and flag < 5:
            flag += 1
            reptile = Reptile(url)
            my_etree = reptile.get_lxml_etree()
            lists = my_etree.xpath(
                '//div[@id="navTab"]')[0].xpath('./div[@class="cfix banner-nav-box"]/a[1]/@href')
        url1 = self.url + lists[0]
        self.get_info3_by_lxml(url1, info)

        info.append(city)  # 城市
        info.append(my_etree.xpath(
            '//div[@class="hasVist cfix sbox fs16"]'))   # 岗位职责
        info.append(my_etree.xpath('//dl[@class="JI-so fs16"]/dd/a'))   # 来源网站
        info.append(my_etree.xpath('//span[@class="fs16 gray9"]'))  # 更新时间
        info.append(my_etree.xpath(
            '//img[@class="company-banner-logo"]/@src'))  # logo信息

    # 爬取第3个网页的信息
    def get_info3_by_lxml(self, url, info):
        reptile = Reptile(url)
        my_etree = reptile.get_lxml_etree()
        info.append(my_etree.xpath('//div[@class="m-container"]/div[@class="intro"]/div[@class="cfix fs16"]/'
                                   'div[@class="j-edit hasVist dlli mb10"]/div[3]/span'))  # 所属行业
        info.append(my_etree.xpath('//div[@class="m-container"]/div[@class="intro"]/div[@class="cfix fs16"]/'
                                   'div[@class="j-edit hasVist dlli mb10"]/div[1]/div[@class="company-worker"]'))  # 公司规模

    # 从爬下来的info中获取job列表
    def get_jobs(self):
        info_list = self.get_info_by_lxml()
        for info in info_list:
            job = Recruit()
            job.format(info)
            self.jobs.append(job)


class Filepath:
    """_使用到的文件路径_

    爬取网页过多时，爬虫效果不稳定，每次运行结果均保存在“副本”中，最新一次的结果保存于原文件中
    """
    # 需要读取的文件，统一存放于read目录下
    read_city_txt = ('热门城市.txt', os.getcwd() + os.sep + 'read')
    read_title_txt = ('关注岗位.txt', os.getcwd() + os.sep + 'read')

    # 需要写入的文件，统一存放于save目录下
    write_salary_txt = ('薪资数据.txt', os.getcwd() + os.sep + 'save')
    write_salary_xlsx = ('薪资数据.xlsx', os.getcwd() + os.sep + 'save')

    # 副本文件统一存放于temp目录下
    write_salary_copy_txt = ('薪资数据(副本).txt', os.getcwd() + os.sep + 'temp')
    write_salary_copy_xlsx = ('薪资数据(副本).xlsx', os.getcwd() + os.sep + 'temp')

    # 获取文件路径
    def get_filepath(self, file):
        if not os.path.exists(file[1]):
            os.makedirs(file[1])
        return file[1] + os.sep + file[0]


if __name__ == "__main__":
    crawlers = Crawlers()
    crawlers.get_jobs()
    File_operation().save_jobs_excel(File_path().get_filepath(
        File_path().write_salary_xlsx), crawlers.jobs)
