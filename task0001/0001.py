#!/usr/bin/env python

import random, string

def rand_str(num,length):
    f = open('randomnum.txt','wb')
    for i in range(num):
        chars = string.letters + string.digits
        s = [random.choice(chars) for i in range(length)]
        f.write(''.join(s)+'\n')
    f.close()

if __name__== 'main':
    rand_str(200,4)
