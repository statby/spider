#!/bin/env python3
# coding=utf-8
# Filename    : get_different_area_site_ranking.py
# Date        : 2016-03-30 23:28:28
# Author      : Statby
# Description : Get top 500 site from different area ,and write in excel.

import requests
from bs4 import BeautifulSoup
import xlsxwriter
from get_area_url import get_urls


def get_data(page, area='index_CN'):
    #获取单页网站排名信息
    data = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',}
    if page == 1:
         site = 'http://alexa.chinaz.com/Country/{}.html'.format(area)
    else:
         site = 'http://alexa.chinaz.com/Country/{}_{}.html'.format(area,page)
#    return(site)
#    site = 'http://alexa.chinaz.com/Country/index_SE.html'
    try:
        req = requests.get(site, headers=headers)
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
    except:
        print('Some Error!')
        pass

#print(get_data(1,area='index_SE'))
#get_data(1,area='index_SE')

def get_more_page(start, stop, area='index_CN'):
    sum = []
    try:
        for pages in range(start, stop+1):
            sum += get_data(pages,area=area)
        return sum
    except:
        print('Some Error!')
        pass

def write_txt(start, stop, area='index_CN'):
    # 写成txt格式文件
    try:
        with open('{}.txt'.format(area), 'w') as f:
            for i, j in enumerate(get_more_page(start, stop, area=area)):
                f.write('\n')
                for x in j:
                    f.write(x+' ')
    except:
        print('Some Error!')
        pass


def write_excel_xlsxwriter(start, stop, area='index_CN',excel_name='index_CN'):
    # xlsxwriter该库写入xlsx文件,实测无错误
    workbook = xlsxwriter.Workbook('{}.xlsx'.format(excel_name))
    worksheet = workbook.add_worksheet(excel_name)
    for line_num, lines in enumerate(get_more_page(start, stop, area=area)):
        worksheet.write(line_num, 0, lines[0])
        worksheet.write(line_num, 1, lines[1])
        worksheet.write(line_num, 2, lines[2])
    workbook.close()
    
def write_all_area_excel():
    #把所有地区的网站排名都写在单独的excel
     for name,urls in get_urls().items():
       write_excel_xlsxwriter(1, 20, area=urls, excel_name=name) 

#write_all_area_excel()

def write_all_area_in_one_excel():
    #把所有地区的网站排名都写在同一个文件内
    workbook = xlsxwriter.Workbook('all_area.xlsx')
    for name,urls in get_urls().items():
        worksheet = workbook.add_worksheet(name)
        for line_num, lines in enumerate(get_more_page(1, 20, area=urls)):
            worksheet.write(line_num, 0, lines[0])
            worksheet.write(line_num, 1, lines[1])
            worksheet.write(line_num, 2, lines[2])
    workbook.close()

write_all_area_in_one_excel()

#write_excel_xlsxwriter(1, 20, area='index_HK', excel_name='香港')
