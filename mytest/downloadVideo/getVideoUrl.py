# @File  : getVideoUrl.py
# @Author: Qiao
# @Date  : 2019/2/28
# @Desc  :

import re
import requests


def getRegExlist(patterntest,patternstr):
    pattern = re.compile(patternstr)
    regexlist = pattern.findall(patterntest, re.S)
    return regexlist


def getVideoPageList():
    respose = requests.get('https://venturewell.org/i-corps/llpvideos/')
    # print(respose.status_code) # 响应的状态码
    # print(respose.content)   #返回字节信息
    # print(respose.text)   #返回文本内容

    # "<h2><a href="https://venturewell.org/i-corps/llpvideos/general-discussion/" target="_blank" rel="noopener">General Discussion</a></h2>"
    # patternstr1 = "<h2>.+href=(\"http.+).+target.+>(.+).+</a></h2>"
    patternstr = ".+(http.+\"?)target.+>(.+)</a>"
    videopagelist = getRegExlist(respose.text,patternstr)
    print(videopagelist)
    print(len(videopagelist))
    return videopagelist


myvideopagelist = getVideoPageList()


def getPageVideoList(myvideopagelist):
    for myvideopage in myvideopagelist:
        pageurl = myvideopage(0)
        pagename = myvideopage(1)

        respose = requests.get(pageurl)
        patternstr = ".+(http.+\"?)rel=\"noopener\".+>(.+)</a>"

        videolist = getRegExlist(respose.text, patternstr)
        print(videolist)


    pass


# getPageVideoList(myvideopagelist)
