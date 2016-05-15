#!/usr/bin/env python

import string,random

def random_factory(num,length):
    f = open('rd','wr')
    for i in range(num):
        s = string.letters + string.digits
        n = [random.choice(s) for i in range(length)]
        f.write(''.join(n)+'\n')
    f.close()

if __name__ == '__main__':
    random_factory(200,6)

