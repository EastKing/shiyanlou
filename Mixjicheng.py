#当前目录
import os
def searchfile(path,str):
    dirs=os.path.abspath(path)
    # print('当前目录->>>>',dirs)           #当前目录
    for subpath in os.listdir(dirs): #当前目录的子目录
        # print("当前目录下的子目录->>>>",subpath)
        full_path=os.path.join(dirs,subpath)
        if os.path.isdir(subpath):  #判断是否是目录
            searchfile(full_path,str)  #递归调用函数
        else:
            if str in subpath:
                print(full_path)
if __name__ == '__main__':

    searchfile('.','.py')




