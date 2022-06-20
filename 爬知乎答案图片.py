import requests
import json
import jsonpath
import re
import time

cookies = ''
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36',
    'cookie': cookies
}
# 问题链接，改变数字编号就好了
i = 0
num = 0  # 图片名字，自增的数字

# 爬多少个答案
while i <= 50:
    url = 'https://www.zhihu.com/api/v4/questions/537315394/answers?limit=5&offset={0}&platform=desktop&sort_by=default'.format(i)
    res = requests.get(url, headers=header)
    if res.status_code != '200':
        print("error")
    html = json.loads(res.text)  # 转化为json格式
    content = jsonpath.jsonpath(html, "$..content")  # 用jsonpath找出答案目录

    for x in content:
        imgs = re.findall('img src="(.*?)"', x)  # 用re找出图片链接，返回的是一个列表，遍历一遍提取链接

        for vid in range(0, len(imgs), 2):
            loadimg = requests.get(url=imgs[vid], headers=header)
            with open(r'D:\pv\{}.jpg'.format(num), 'wb') as f:
                f.write(loadimg.content)
                f.close()
            num = num + 1
            time.sleep(1)
    i = i + 5

'''<img src="(.*?)" data-rawwidth=".*?" data-rawheight=".*?" data-size=".*?" data-default-watermark-src=".*?" class=".*?" width=".*?" data-original=".*?"/>'''
