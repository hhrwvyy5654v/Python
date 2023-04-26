import re
from docx import Document

doc = Document('测试文件.docx')
for para in doc.paragraphs:
    text = para.text
    pattern = r'(([\u4e00-\u9fa5])\2([\u4e00-\u9fa5])\3)'
    r = re.findall(pattern, text)
    if r:
        for word in r:
            print(word[0])
