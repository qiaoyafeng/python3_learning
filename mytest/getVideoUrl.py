# @File  : getVideoUrl.py
# @Author: Qiao
# @Date  : 2019/2/28
# @Desc  :


import re
import requests


respose = requests.get('https://venturewell.org/i-corps/llpvideos/')
# print(respose.status_code) # 响应的状态码
# print(respose.content)   #返回字节信息
# print(respose.text)   #返回文本内容

mytext = """
<h2><a href="https://venturewell.org/i-corps/llpvideos/mentor-training/" target="_blank" rel="noopener">Mentor Training</a></h2>
"""
patternstr1 = "<h2>.+href=(\"http.+).+target.+>(.+).+</a></h2>"
# patternstr1 = r"<a .*?>(.*?)</a>"
pattern = re.compile(patternstr1)

url_namelist = pattern.findall(respose.text, re.S)
print('1111111111111111111111111111111')
print(url_namelist)


"""


content = '''
<td>
<a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
<a href="https://www.baidu.com//articles/gz.html" title="贵州省">贵州省主题介绍</a>
</td>
'''

# 获取<a href></a>之间的内容
print(u'获取链接文本内容:')

res = r'<a .*?>(.*?)</a>'
mm = re.findall(res, content, re.S | re.M)
for value in mm:
    print(value)

# 获取所有<a href></a>链接所有内容
print(u'\n获取完整链接内容:')
urls = re.findall(r"<a.*?href=.*?<\/a>", content, re.I | re.S | re.M)
for i in urls:
    print(i)

# 获取<a href></a>中的URL
print('\n获取链接中URL:')
res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
link = re.findall(res_url, content, re.I | re.S | re.M)
print(link)
for url in link:
    print(url)

print urls

print len(urls)

for url in urls:
    print url
    print '==================================='

urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)   #re.S 把文本信息转换成1行匹配
url=urls[5]
result=requests.get(url)
mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]

video=requests.get(mp4_url)

with open('D:\\a.mp4','wb') as f:
    f.write(video.content)

"""
