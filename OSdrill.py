import os
import datetime


path = os.path.abspath('C:\\Users\\austi\\Documents\\Coding\\python\\OSdrill')

fileList = os.listdir(path)

for i in fileList:
    absPath = os.path.join(path, i)
    if absPath.endswith('.txt'):
        print('Text file found: {}'.format(i))
        mTime = round(os.path.getmtime(absPath),0)
        modifyDate = datetime.datetime.fromtimestamp(mTime)
        print('Last edit: {}'.format(modifyDate))







