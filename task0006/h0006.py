#-*-coding:utf-8
import os,re
path = 'diaries'
thefile = os.listdir(path)

def get_words(words):
    dic = {}
    max_word = ''
    maxtime = 0
    for word in words:
        if dic.has_key(word) is False:
            dic[word] = 1
        else:
            dic[word] = dic[word]+1
    for key,value in dic.items():
        if dic[key]>maxtime:
            maxtime = dic[key]
            max_word = key
    print(max_word,maxtime)

for f in thefile:
    with open(os.path.join(path,f))as diary:
        words = re.findall("[a-zA-Z]+-*[a-zA-Z]*[^to]",diary.read())
        get_words(words)


