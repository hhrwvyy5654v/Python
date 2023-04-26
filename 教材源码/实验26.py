import hashlib
import os.path

fileName = input('请输入文件名（包含完整路径）：')
if os.path.isfile(fileName):
    with open(fileName, 'rb') as fp:
        data = fp.read()
        print(hashlib.md5(data).hexdigest())
else:
    print('文件不存在.')
