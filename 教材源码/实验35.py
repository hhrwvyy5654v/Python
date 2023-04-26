import os
import os.path
import pptx

total = 0
def pptCount(path):
    global total
    for subPath in os.listdir(path):
        subPath = os.path.join(path, subPath)
        if os.path.isdir(subPath):
            pptCount(subPath)
        elif subPath.endswith('.pptx'):
            print(subPath)
            presentation = pptx.Presentation(subPath)
            total += len(presentation.slides)

pptCount('F:\\教学课件\\Python程序设计（第二版）')
print(total)
