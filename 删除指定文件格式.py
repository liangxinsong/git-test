import os

def del_files(path, extendName):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(extendName):       #指定要删除的格式，这里是jpg 可以换成其他格式
                os.remove(os.path.join(root, name))
                print ('Delete File: ' + os.path.join(root, name))

if __name__ == '__main__':
    path = input('输入指定路径：')
    extendName = input('输入指定要删除的格式，如".jpg" ')
    del_files(path, extendName)