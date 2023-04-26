from PIL import Image, ImageEnhance, ImageFilter

# 打开Lena灰度图像
im = Image.open('lena.jpg')

# 图像细节增强
im.filter(ImageFilter.DETAIL).show()

# 图像边缘增强
im.filter(ImageFilter.EDGE_ENHANCE).show()

# 图像边缘提取
im.filter(ImageFilter.FIND_EDGES).show()

# 图像中值滤波，滤波窗口大小默认为3
im.filter(ImageFilter.MedianFilter).show()
# 图像中值滤波，指定滤波窗口大小
im.filter(ImageFilter.MedianFilter(5)).show()

# 图像锐化
im.filter(ImageFilter.SHARPEN).show()

# 图像平滑
im.filter(ImageFilter.SMOOTH_MORE).show()

# 图像模糊，使用默认参数
im.filter(ImageFilter.BLUR).show()
# 图像模糊，使用自定义参数
myBlur = ImageFilter.BLUR()
myBlur.filterargs = ((3,3), 8, 0, (1,)*9)
im.filter(myBlur).show()

# 图像亮度增强
ImageEnhance.Brightness(im).enhance(1.5).show()

# 图像对比度增强
ImageEnhance.Contrast(im).enhance(1.3).show()

# 图像冷暖色调整
im1 = Image.open('彩色测试图像.jpg')
r, g, b = im1.split()
r = r.point(lambda x:x*0.5)
Image.merge(im1.mode, (r,g,b)).show()
