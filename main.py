#! usr/bin/python
# coding=utf-8

import os
import requests
from bs4 import BeautifulSoup



def main():
    originalUrl = 'http://jandan.net/ooxx/page-'
    for i in range(100):
        rest = req(originalUrl, str(i))
        downloadImg(rest,str(i))


def req(url, pageIndex):
    resp = requests.get(url + pageIndex)
    ass = []
    if resp.status_code == 200:
        content = resp.content
        soup = BeautifulSoup(content, "html.parser")
        links = soup.find_all('a', 'view_img_link')
        length = len(links)
        print(length)
        for i in range(length):
            ass.append('http:' + links[i].attrs['href'])
    return ass


def downloadImg(urls,pageIndex):
    index = 0
    for url in urls:
        print("下载:", url)
        # 未能正确获得网页 就进行异常处理
        try:
            res = requests.get(url)
            if res.status_code != 200:
                print('未下载成功：', url)
                continue
        except Exception as e:
            print('未下载成功：', url)

        filename = os.path.join('imgs', str(pageIndex)+'-'+str(index) + '.jpg')
        with open(filename, 'wb') as f:
            f.write(res.content)
            print('下载完成\n')
            index += 1
        print("下载结束，一共下载了 %s 张图片" % (index - 1))

if __name__ == '__main__':
    main()
