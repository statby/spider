#!/bin/env python3
# coding=utf-8
# Filename    : top-site.py
# Date        : 2016-03-30 23:28:28
# Author      : Statby
# Description : get different country url

import requests
from bs4 import BeautifulSoup
import time
import xlwt



def get_data(page,area='Global'):
    data = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',}
    if page == 1:
        site = 'http://alexa.chinaz.com/{}/index.html'.format(area)
    else:
        site = 'http://alexa.chinaz.com/{}/index_{}.html'.format(area,page)
    req = requests.get(site,headers=headers)
    req.encoding = 'utf-8'
    status = req.status_code
    soup = BeautifulSoup(req.text, 'lxml')
    # print(soup)
    # print(req.encoding)
    
    rankings = soup.select('div > div > ul > li > div.count')
    introduces = soup.select('div > div > ul > li > div > p')
    urls = soup.select(' div > div > ul > li > div > h3 > span ')
    
    for ranking, introduce, url in zip(rankings, introduces, urls):
        data.append([ranking.text, url.text, introduce.text])
    return(data)

def get_more_page(start,stop):
    sum = []
    for pages in range(start,stop+1):
        sum += get_data(pages)
#        sum.append(get_data(pages))
    return sum
#print (get_data(2))


#print(get_more_page(1,3))
#for i,j in enumerate(get_data(4)):
# # ##     print(j)
'''
def write_down(start,stop):
    with open('top-site.txt', 'w') as f:
#        f.write(str(get_more_page(start,stop)))
        for line in get_more_page(start,stop):
            f.write(str(line), '\n')

#write_down(1,3)
'''
#with open('top-site.txt', 'w') as f:
#    for i in range(len(get_more_page(1,1))):
#        f.write(get_more_page(1,1)[i]+'\n')

#for i in range(len(get_more_page(1,1))):
#     print (type(get_more_page(1,1)[i]))

#for i,j in enumerate(get_more_page(1,4)):
#      print(j)

with open('top-site.txt', 'w') as f:
    for i,j in enumerate(get_more_page(1,20)):
        f.write('\n')
        for x in j:
            f.write(x+' ')





    
