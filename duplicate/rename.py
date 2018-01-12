# coding:utf-8
import os


def rename():
     i=0
     path='/Users/huoyongjie/Desktop/girl11/'
     if os.path.isdir(path) == True:

         filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
         for files in filelist:#遍历所有文件
            i=i+1
            Olddir=os.path.join(path,files)#原来的文件路径
            if os.path.isdir(Olddir):#如果是文件夹则跳过
                    continue
            filename=os.path.splitext(files)[0]#文件名
            filetype=os.path.splitext(files)[1]#文件扩展名
            Newdir=os.path.join(path,'插图-'+str(i+60)+filetype)#新的文件路径
            os.rename(Olddir,Newdir) #重命名
     else:
           print("没有该文件")



if __name__ == '__main__':
     rename()