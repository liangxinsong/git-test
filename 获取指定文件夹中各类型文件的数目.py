import os

#统计当前目录下每个文件类型的个数
curdir = input('输入目标文件夹：')

all_files = os.listdir(curdir)  #os.listdir(dirname)：列出dirname下的目录和文件
type_dict = dict()

for each_file in all_files:
    if os.path.isdir(each_file):    #os.path.isdir(name)：判断name是不是一个目录，name不是目录就返回false
        type_dict.setdefault('文件夹', 0)
        type_dict['文件夹'] += 1

    else:
        ext = os.path.splitext(each_file)[1]    #os.path.splitext()：分离文件名与扩展名
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件%d个' % (each_type, type_dict[each_type]))
