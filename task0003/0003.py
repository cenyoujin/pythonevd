#!/usr/bin/env python
import string,random,redis

def random_creater(num,length):
    f = open('randomdic.txt','wb')
    s = string.letters + string.digits
    for i in range(num):
        randomnum = [random.choice(s) for m in range(length)]
        f.write(''.join(randomnum)+'\n')
    f.close()

def redis_save(filename,length):
    r = redis.StrictRedis(host='localhost', port=6379)
    with open(filename,'r') as f:
        keys = f.readlines()
        i = 0;
        for key in keys:
            if(i<(length+1)):
                r.set('id'+str(i),key.strip())
                i+=1
    for i in range(length):
        print r.get('id'+str(i))


if __name__ == '__main__':
    random_creater(200,7)
    redis_save('randomdic.txt',200)
