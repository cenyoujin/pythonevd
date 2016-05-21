#-*-coding:utf-8
import os,re
path = 'prolist'
files = os.listdir(path)

def get_lines():
    count = 0
    spannum = 0
    zhunum = 0
    for fin in files:
        with open(os.path.join(path,fin)) as f:
            for line in f.readlines():
                count = count+1
                if line =='\n':
                    spannum+=1
                if re.findall("\#+",line):
                    zhunum +=1
    print "一共：%d行\n空行：%d行\n注释：%d行" %(count,spannum,zhunum)

if __name__ == '__main__':
    get_lines()


