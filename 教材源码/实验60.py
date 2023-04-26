from os import listdir
from PIL import Image

# 获取当前文件夹中所有PNG图像
ims = [Image.open(fn) for fn in listdir() if fn.endswith('.png')]

# 单幅图像尺寸
width, height = ims[0].size
# 创建空白长图
result = Image.new(ims[0].mode, (width, height*len(ims)))

# 拼接
for i, im in enumerate(ims):
    result.paste(im, box=(0,i*height))

# 保存
result.save('result.png')
