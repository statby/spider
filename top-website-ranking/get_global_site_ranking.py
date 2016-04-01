#!/bin/env python3
# coding=utf-8
# Filename    : get_global_site_ranking.py
# Date        : 2016-03-30 23:28:28
# Author      : Statby
# Description : get top 500 site

import requests
from bs4 import BeautifulSoup
import time
import xlwt
import xlsxwriter

def get_data(page, area='Global'):
    #获取单页网站排名信息
    data = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',}
    if page == 1:
        site = 'http://alexa.chinaz.com/{}/index.html'.format(area)
    else:
        site = 'http://alexa.chinaz.com/{}/index_{}.html'.format(area, page)
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

def get_more_page(start, stop):
    sum = []
    try:
        for pages in range(start, stop+1):
            sum += get_data(pages)
        return sum
    except:
        print('Some Error!')
        pass

def write_txt(start, stop):
    # 写成txt格式文件
    try:
        with open('global_top_site_ranking.txt', 'w') as f:
            for i, j in enumerate(get_more_page(start, stop)):
                f.write('\n')
                for x in j:
                    f.write(x+' ')
    except:
        print('Some Error!')
        pass

def write_excel(start, stop):
    # 通过xlwt库写入excel文件,只支持sls格式,而且写入大批量文件时会错线错误,改用xlsxwriter库
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('global')
    try:
        for line_num, lines in enumerate(get_more_page(start, stop)):
            sheet1.write(line_num, 0, lines[0])
            sheet1.write(line_num, 1, lines[1])
            sheet1.write(line_num, 2, lines[2])
        wb.save('global_top_site_ranking.xls')
    except:
        print('Some Error!')
        pass

def write_excel_xlsxwriter(start, stop):
    # xlsxwriter该库写入xlsx文件,实测无错误
    workbook = xlsxwriter.Workbook('global_top_site_ranking_xlsxwriter.xlsx')
    worksheet = workbook.add_worksheet('global')
    for line_num, lines in enumerate(get_more_page(start, stop)):
        worksheet.write(line_num, 0, lines[0])
        worksheet.write(line_num, 1, lines[1])
        worksheet.write(line_num, 2, lines[2])
    workbook.close()
    

#write_excel(7, 20)
#write_txt(1, 20)
#print (get_more_page(1,20))

#write_excel_xlsxwriter(1, 20)
