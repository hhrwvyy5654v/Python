from os import listdir
from random import randint

# 网页头部信息
head = '''<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>{}</title>
	</head>
	<body><br/><br/><br/>\n'''.format('第7章 文件操作')

# 创建HTML5网页文件，写入信息
with open('chapter7.html', 'w', encoding='utf8') as fp:
    # 写入网页文件头部信息
    fp.write(head)
    # 获取当前文件夹中所有JPG图片文件名称
    fns = [fn for fn in listdir() if fn.endswith('.jpg')]
    # 按文件名序号升序排序
    fns.sort(key=lambda fn: int(fn[3:fn.rindex('.')]))
    for fn in fns:
        # 写入每个图片文件的信息
        pic = r'''		<div align="center">
		    <figure>
			    <img src="{}" border="1"
			     style="transform: rotate({}deg);"/>
			    <figcaption>{}</figcaption>
		    </figure>
		</div>'''.format(fn,
                           randint(1, 16)-8,
                           fn[:fn.rindex('.')])
        fp.write(pic)
    # 所有图片均已导入，闭合body和html标签
    fp.write('''	</body>\n</html>''')
