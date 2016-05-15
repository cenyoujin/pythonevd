#!/usr/bin/env python

import random,string

def random_num(num,length):
    f = open('yz.txt','wb')
    for i in range(num):
        characters = string.letters + string.digits
        ran = [random.choice(characters) for i in range(length)]
        f.write(''.join(ran)+'\n')
    f.close()

if __name__ == '__main__':
    num = 200
    length = 5
    random_num(num,length)


