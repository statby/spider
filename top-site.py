#!/bin/env python3
# coding=utf-8
# Filename    : top-site.py
# Date        : 2016-03-30 23:28:28
# Author      : Statby
# Description : get top 500 site

import requests
from bs4 import BeautifulSoup
import time
data = []
def get_data(page):
    site = 'http://alexa.chinaz.com/Global/index_{}.html'.format(page)
    req = requests.get(site)
    req.encoding = 'utf-8'
    status = req.status_code
    soup = BeautifulSoup(req.text, 'lxml')
    # print(soup)
    # print(req.encoding)
    
    rankings = soup.select('div > div > ul > li > div.count')
    introduces = soup.select('div > div > ul > li > div > p')
    urls = soup.select(' div > div > ul > li > div > h3 > span ')
    
    for ranking, introduce, url in zip(rankings, introduces, urls):
        data.append([ranking.text, introduce.text, url.text])
    return(data)

#print (get_data(4))
def get_more_page(start,stop):
    sum = []
    for pages in range(start,stop+1):
        sum += get_data(pages)
    return sum

#print(get_more_page(2,20))
with open('top-site.txt', 'w+') as f:
    f.write(str(get_more_page(2,20)))


'''

for ranking in rankings:
    print (ranking.text)
for introduce in introduces:
    print (introduce.text)
for url in urls:
    print (url.text)

'''
