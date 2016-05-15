#!/usr/bin/env python
import string,random,redis
def redisran(length,num):
    s = string.letters + string.digits
    r = redis.StrictRedis(host='localhost', port=6379)
    for i in range(num):
        rd = [random.choice(s) for m in range(length)]
        save = ''.join(rd)
        r.set('key_id'+str(i),save)
    for i in range(num):
        print(r.get("key_id"+str(i)))

if __name__ == '__main__':
    redisran(7,200)
