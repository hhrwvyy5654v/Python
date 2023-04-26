# -*- encoding: utf-8 -*-
'''
@File    :   Data_process.py
@Time    :   2022/05/25 15:24:01
@Author  :   HuangRongQuan 
@Version :   1.0
@Contact :   huang_rongquan@outlook.com
'''
import os  # 文件操作
import re   # 正则表达式
import xlrd  # 打开excel表格读取数据
import jieba  # 分词
import numpy as np  # 数组处理
import matplotlib.pyplot as plt  # 基础绘图
from PIL import Image  # 读取图片
from wordcloud import WordCloud, ImageColorGenerator  # 词云制作


class Normalize:
    """_数据规范化处理_
    """
    # 定义文件地址

    def __init__(self, file_path):
        self.file_path = file_path

    # 提取中文字符
    def find_chinese(self):
        pattern = re.compile(r'[^\u4e00-\u9fa5]')
        chinese = re.sub(pattern, '', self.file_path)
        return chinese

    # 提取非中文字符
    def find_unchinese(self):
        pattern = re.compile(r'[\u4e00-\u9fa5]')
        unchinese = re.sub(pattern, "", self.file_path)
        return unchinese

    # 提取数字字符
    def find_digit(self):
        digit = re.findall(r"\d+\.?\d*", self.file_path)
        return digit

    # 获取数字字符长度
    def len_digit(self):
        digit = re.findall(r"\d+\.?\d*", self.file_path)
        return len(digit)

    # 规范化经验要求
    def get_experience(self):
        digit = self.find_digit()
        digit_int = list(map(int, digit))
        chinese = self.find_chinese()
        unchinese = self.find_unchinese()
        digit_size = self.len_digit()
        experience1 = "0-1年"
        experience2 = "1-3年"
        experience3 = "3-5年"
        experience4 = "5-10年"
        experience5 = "10-20年"

        if "不限经验" in chinese or "应届毕业生" in chinese:
            experience = chinese
        else:
            if digit_size == 1:
                if "以上" in chinese:
                    num1 = digit_int[0]
                    if num1 >= 1 and num1 <= 2:
                        experience = experience2
                    elif num1 >= 3 and num1 <= 4:
                        experience = experience3
                    elif num1 >= 5 and num1 <= 9:
                        experience = experience4
                    elif num1 >= 10:
                        experience = experience5
                    else:
                        experience = "其他"

                elif "以下" in chinese:
                    num2 = digit_int[0]
                    if num2 <= 1:
                        experience = experience1
                    elif num2 > 1 and num2 <= 3:
                        experience = experience2
                    elif num2 > 3 and num2 <= 5:
                        experience = experience3
                    elif num2 > 5 and num2 <= 10:
                        experience = experience4
                    elif num2 > 10:
                        experience = experience5
                    else:
                        experience = "其他"

                else:
                    num1 = digit_int[0]
                    if num1 >= 0 and num1 < 1:
                        experience = experience1
                    elif num1 >= 1 and num1 < 3:
                        experience = experience2
                    elif num1 >= 3 and num1 < 5:
                        experience = experience3
                    elif num1 >= 5 and num1 < 10:
                        experience = experience4
                    elif num1 >= 10 and num1 < 20:
                        experience = experience5
                    else:
                        experience = "其他"

            elif digit_size == 2:
                num1 = digit_int[0]
                num2 = digit_int[1]
                if num1 >= 0 and num2 <= 1:
                    experience = experience1
                elif num1 >= 1 and num2 <= 3:
                    experience = experience2
                elif num1 >= 3 and num2 <= 5:
                    experience = experience3
                elif num1 >= 5 and num2 <= 10:
                    experience = experience4
                elif num1 >= 10 and num2 <= 20:
                    experience = experience5
                else:
                    experience = "其他"

        return experience

    # 规范化薪资待遇
    def get_salary(self):
        digit = self.find_digit()
        digit_int = list(map(float, digit))
        chinese = self.find_chinese()
        unchinese = self.find_unchinese()
        salary = ""
        if "面议" in chinese:
            return chinese
        else:
            if "千" in chinese or "K" in unchinese or "k" in unchinese:
                digit_int[0] *= 1000
                digit_int[1] *= 1000
            elif "万" in chinese or "W" in unchinese or "w" in unchinese:
                digit_int[0] *= 10000
                digit_int[1] *= 10000
            if "年" in chinese:
                digit_int = [round(x/12.0) for x in digit_int]
            digit_int = (round(i) for i in digit_int)
            salary += "-".join(str(i) for i in digit_int)
            return salary

    # 规范化浏览量
    def get_page_views(self):
        digit = self.find_digit()
        digit_int = list(map(float, digit))
        chinese = self.find_chinese()
        page_views = ""
        if "万" in chinese:
            digit_int[0] *= 10000
        elif "千" in chinese:
            digit_int[0] *= 1000
        digit_int = (round(i) for i in digit_int)
        page_views = "".join(str(i) for i in digit_int)
        return page_views

    # 规范化公司规模
    def get_company_size(self):
        digit = self.find_digit()
        digit_int = list(map(int, digit))
        chinese = self.find_chinese()
        unchinese = self.find_unchinese()
        digit_size = self.len_digit()
        company_size = ""
        company_size1 = "1-49人"
        company_size2 = "50-99人"
        company_size3 = "100-499人"
        company_size4 = "500-999人"
        company_size5 = "1000-4999人"
        company_size6 = "5000-9999人"
        company_size7 = "10000-19999人"
        if len(self.str) == 0:
            company_size = '无'
        if digit_size == 1:
            if "以上" in chinese:
                num1 = digit_int[0]
                if num1 >= 1 and num1 <= 49:
                    company_size = company_size1
                elif num1 >= 50 and num1 <= 99:
                    company_size = company_size2
                elif num1 >= 100 and num1 <= 499:
                    company_size = company_size3
                elif num1 >= 500 and num1 <= 999:
                    company_size = company_size4
                elif num1 >= 1000 and num1 <= 4999:
                    company_size = company_size5
                elif num1 >= 5000 and num1 <= 9999:
                    company_size = company_size6
                elif num1 >= 10000 and num1 <= 19999:
                    company_size = company_size7
                else:
                    company_size = "其他"

            elif "少于" in chinese:
                num2 = digit_int[0]
                if num2 <= 50:
                    company_size = company_size1
                elif num2 <= 100:
                    company_size = company_size2
                elif num2 <= 500:
                    company_size = company_size3
                elif num2 <= 1000:
                    company_size = company_size4
                elif num2 <= 5000:
                    company_size = company_size5
                elif num2 <= 10000:
                    company_size = company_size6
                elif num2 <= 20000:
                    company_size = company_size7
                else:
                    company_size = "其他"

        elif digit_size == 2:
            num1 = digit_int[0]
            num2 = digit_int[1]
            if num1 >= 1 and num2 <= 49:
                company_size = company_size1
            elif num1 >= 50 and num2 <= 99:
                company_size = company_size2
            elif num1 >= 100 and num2 <= 499:
                company_size = company_size3
            elif num1 >= 500 and num2 <= 999:
                company_size = company_size4
            elif num1 >= 1000 and num2 <= 4999:
                company_size = company_size5
            elif num1 >= 5000 and num2 <= 9999:
                company_size = company_size6
            elif num1 >= 10000 and num2 <= 20000:
                company_size = company_size7
            else:
                company_size = "其他"

        return company_size

    # 规范化更新时间
    def get_update_time(self):
        update_time = self.str[-10:]
        return update_time


class Word_cloud:
    """_制作和保存词云_
    """

    # 设置文本和素材路径
    def __init__(self, fname_text, fname_stop, fname_mask, fname_font):
        self.fname_text = fname_text
        self.fname_stop = fname_stop
        self.fname_mask = fname_mask
        self.fname_font = fname_font

    # 显示词云图片
    def show(self, x, wc=None, show=True):
        if wc is None:
            fig, wc = plt.subplots()
        wc.imshow(x)
        wc.axis("off")
        if show:
            plt.show()
        return wc

    # 统计词频
    def count_frequencies(self, word_list):
        frequency = dict()
        for word in word_list:
            if word not in frequency.keys():
                frequency[word] = 1
            else:
                frequency[word] += 1
        return frequency

    # 制作词云
    def Generate(self):
        # 以UTF-8的格式读取文本
        text = open(self.fname_text, encoding='utf8').read()
        # 设置中文停用词表
        STOPWORDS_CH = open(self.fname_stop, encoding='utf8').read().split()
        # 处理文本：剪切单词、删除非索引字和单字符
        word_list = [
            word for word in jieba.cut(text)
            if word not in STOPWORDS_CH and len(word) > 1
        ]
        frequency = self.count_frequencies(word_list)
        im_mask = np.array(Image.open(self.fname_mask))
        # 用ImageColorGenerator从中提取颜色后得到一个颜色生成器, 依照每个词所占的矩形区域的颜色平均来确定改词最终的颜色
        im_colors = ImageColorGenerator(im_mask)
        # 为中文生成词云
        word_cloud = WordCloud(font_path=self.fname_font,
                               background_color='white',
                               mode="RGBA",
                               mask=im_mask,
                               )
        word_cloud.generate_from_frequencies(frequency)  # 为英文生成词云
        word_cloud.recolor(color_func=im_colors)  # 重新对每个词染色
        wc = self.show(word_cloud,)  # 可视化
        head, tail = os.path.split(self.fname_text)
        file_name = os.path.splitext(tail)[0]
        wc.figure.savefig(
            './visualisation/[词云]'+file_name+'.png', bbox_inches='tight', dpi=150)


class Data_clean:
    """_数据清洗_
    """

    def __init__(self, experience_txt, salary_txt, page_views_txt, company_size_txt, update_time_txt):
        self.experience_txt = experience_txt
        self.salary_txt = salary_txt
        self.page_views_txt = page_views_txt
        self.company_size_txt = company_size_txt
        self.update_time_txt = update_time_txt

    # 清洗经验要求
    def clean_experience(self):
        file = open(self.experience_txt)
        lines = file.readlines()
        file.close()
        for line in lines:
            rs = line.rstrip('\n')
            normalize = Normalize(rs)
            new_name = rs.replace(rs, normalize.get_experience())
            head, tail = os.path.split(self.experience_txt)
            new_file = open('./after_clean/[已清洗]'+tail, 'a')
            new_file.write(new_name+'\n')
        new_file.close()

    # 清洗薪资待遇
    def clean_salary(self):
        file = open(self.salary_txt)
        lines = file.readlines()
        file.close()
        for line in lines:
            rs = line.rstrip('\n')
            normalize = Normalize(rs)
            new_name = rs.replace(rs, normalize.get_salary())
            head, tail = os.path.split(self.salary_txt)
            new_file = open('./after_clean/[已清洗]'+tail, 'a')
            new_file.write(new_name+'\n')
        new_file.close()

    # 清洗浏览量
    def clean_page_views(self):
        file = open(self.page_views_txt)
        lines = file.readlines()
        file.close()
        for line in lines:
            rs = line.rstrip('\n')
            normalize = Normalize(rs)
            new_name = rs.replace(rs, normalize.get_page_views())
            head, tail = os.path.split(self.page_views_txt)
            new_file = open('./after_clean/[已清洗]'+tail, 'a')
            new_file.write(new_name+'\n')
        new_file.close()

    # 清洗公司规模
    def clean_company_size(self):
        file = open(self.company_size_txt)
        lines = file.readlines()
        file.close()
        for line in lines:
            rs = line.rstrip('\n')
            normalize = Normalize(rs)
            new_name = rs.replace(rs, normalize.get_company_size())
            head, tail = os.path.split(self.company_size_txt)
            new_file = open('./after_clean/[已清洗]'+tail, 'a')
            new_file.write(new_name+'\n')
        new_file.close()

    # 清洗更新时间
    def clean_update_time(self):
        file = open(self.update_time_txt)
        lines = file.readlines()
        file.close()
        for line in lines:
            rs = line.rstrip('\n')
            normalize = Normalize(rs)
            new_name = rs.replace(rs, normalize.get_update_time())
            head, tail = os.path.split(self.update_time_txt)
            new_file = open('./after_clean/[已清洗]'+tail, 'a')
            new_file.write(new_name+'\n')
        new_file.close()

    # 清洗所有数据
    def clean_together(self):
        self.clean_experience()
        self.clean_salary()
        self.clean_page_views()
        self.clean_company_size()
        self.clean_update_time()


class Pie_chart:
    """_读取excel表格制作饼状图_
    """

    def __init__(self, xlsx_path, name, start, end, save_path):
        self.xlsx_path = xlsx_path
        self.name = name
        self.start = start
        self.end = end
        self.save_path = save_path

    # 绘制饼状图
    def cartography(self):
        data = xlrd.open_workbook(self.xlsx_path)  # 打开表格文件
        table = data.sheets()[8]  # 选择工作表
        rows = self.end - self.start  # 行数
        item = []  # 标签
        count = []  # 计数

        # 获取标签
        for x in range(self.start, self.end):
            value1 = []
            row = table.row_values(x)
            for j in range(0, 1):
                value1.append(row[j])
            item.append(value1[0])

        # 获取计数
        for y in range(self.start, self.end):
            value2 = []
            row = table.row_values(y)
            for i in range(1, 2):
                value2.append(row[i])
            count.append(value2[0])

        # 绘制饼状图
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
        fig, ax = plt.subplots()
        plt.suptitle(self.name, fontsize=20)
        ax.pie(count, autopct='%1.1f%%',shadow=False, startangle=90)
        ax.axis('equal')
        plt.legend(item)
        plt.savefig(self.save_path+self.name+".png")  # 保存图片
        plt.show()


if __name__ == "__main__":
    stop_words_path = "./stop_words/hit_stop_words.txt"
    font_path = "./SourceHanSerifK-Light.otf"
    title_word_cloud = Word_cloud(
        './pending/岗位名称.txt', stop_words_path, './image/Firefox.jpg', font_path)
    title_word_cloud.Generate()
    industry_word_cloud = Word_cloud(
        './pending/所属行业.txt', stop_words_path, './image/Chrome.png', font_path)
    industry_word_cloud.Generate()
    responsibilities_word_cloud = Word_cloud(
        './pending/岗位职责.txt', stop_words_path, './image/Edge.png', font_path)
    responsibilities_word_cloud.Generate()

    file_path = ["经验要求.txt", "薪资待遇.txt", "浏览量.txt", "公司规模.txt", "更新时间.txt"]
    for file in file_path:
        if os.path.exists("./after_clean/[已清洗]/"+file):
            os.remove("./after_clean/[已清洗]/"+file)
    dc = Data_clean("./pending/经验要求.txt", "./pending/薪资待遇.txt",
                    "./pending/浏览量.txt", "./pending/公司规模.txt", "./pending/更新时间.txt")
    dc.clean_together()

    experience = Pie_chart("./save/招聘信息.xlsx", "经验要求",
                           1, 9, "./visualisation/")
    experience.cartography()
    education = Pie_chart("./save/招聘信息.xlsx", "学历要求",
                          11, 18, "./visualisation/")
    education.cartography()
    salary = Pie_chart("./save/招聘信息.xlsx", "薪资待遇", 20, 30, "./visualisation/")
    salary.cartography()
    company_size = Pie_chart("./save/招聘信息.xlsx", "公司规模",
                             32, 40, "./visualisation/")
    company_size.cartography()
    source_website = Pie_chart(
        "./save/招聘信息.xlsx", "来源网站", 42, 49, "./visualisation/")
    source_website.cartography()
