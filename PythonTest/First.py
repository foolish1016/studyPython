#-*- coding:utf-8 -*-
import re
import requests
import os
def dowmloadPic(html,keyword):
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    print '找到关键词:'+keyword+'的图片，现在开始下载图片...'
    for k in range(0,60):
        each = pic_url[k]
        print '正在下载第'+str(i+1)+'张图片，图片地址:'+str(each)
        try:
            pic= requests.get(each, timeout=30)
        except requests.exceptions.ConnectionError:
            print '【错误】当前图片无法下载'
            continue
        currentpath =  os.getcwd()
        print  currentpath
        string = currentpath+'/'+ 'picture'+'/'+ 'doutu'+str(i) + '.jpg'
        fp = open(string,'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
if __name__ == '__main__':
    word = raw_input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    result = requests.get(url)
    dowmloadPic(result.text,word)

