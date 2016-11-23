#!/bin/env python3
# coding=utf-8
# Date        : 2016-11-22 19:43:42
# Author      : Statby
# Description : 

import random
import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import sys
import re

        
#!/bin/env python3
# coding=utf-8
# Date        : 2016-11-22 19:43:42
# Author      : Statby
# Description :

import random
import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import sys



def randomheader():
    # 随机返回http请求头
    headers=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]
    return random.choice(headers)

def contents(url,timeout=4,encoding='gbk2312'):
    r = requests.get(url,headers=randomheader(),timeout=timeout)
    r.encoding = encoding
    content = r.text
    return content


def lianjia_totalpage(content):
    # 返回链接子页面下的总页数
    soup = BeautifulSoup(content,'lxml') 
    totalpage_tag  = soup.find(attrs={"class":"page-box house-lst-page-box"})
    return (eval(totalpage_tag.get("page-data"))["totalPage"])
    

def lianjia_perpage_info(page):

    conn = sqlite3.connect(db)

    url = 'http://gz.lianjia.com/ershoufang/pg{page}'.format(page=page)
    content = contents(url)
    soup = BeautifulSoup(content,'lxml')
    allhouse = soup.find_all('li',attrs={"class":"clear"})

    for perhouse in allhouse:
            perhouseinfo = {}
#        try:
            url = perhouse.find("a",attrs={"data-el":"ershoufang"}).get('href')
            title = perhouse.find("img",attrs={"class":"lj-lazy"}).get('alt')

            houseIcon = perhouse.find(attrs={"class":"houseInfo"}).text
            district = houseIcon.split('|')[0].strip(" ")
            types= houseIcon.split('|')[1].strip(" ")
            size = re.findall('\d+\.?\d+?',houseIcon.split('|')[2].strip(" "))[0]
            face = houseIcon.split('|')[3].strip(" ") 
            decoration = houseIcon.split('|')[4].strip(" ") 

            positionInfo =  re.split(' +',perhouse.find(attrs={"class":"positionInfo"}).text.strip('\n'))
            floor = positionInfo[0].split('(')[0]
            totalfloor = re.findall('\d+',positionInfo[0])[0]
            try:
                area = positionInfo[3]
            except:
                area = None
            try:
                buildtime = re.findall('\d+',positionInfo[1])[0]
            except:
                buildtime = None

            followInfo = re.split(' / ',perhouse.find(attrs={"class":"followInfo"}).text)
            attention = re.findall('\d+',followInfo[0])[0]
            show = re.findall('\d+',followInfo[1])[0]
            publishtime = followInfo[2]
            
            tag = perhouse.find(attrs={"class":"tag"}).text.strip(" ").strip('\n').split('\n')[0]

            totalprice = re.findall('\d+',perhouse.find(attrs={"class":"totalPrice"}).text)[0]
            unitprice = re.findall('\d+',perhouse.find(attrs={"class":"unitPrice"}).text)[0]

    
            perhouseinfo['url'] = url
            perhouseinfo['title'] = title
            perhouseinfo['district'] = district
            perhouseinfo['types'] = types
            perhouseinfo['size'] = size
            perhouseinfo['face'] = face
            perhouseinfo['decoration'] = decoration
            perhouseinfo['floor'] = floor
            perhouseinfo['totalfloor'] = totalfloor
            perhouseinfo['area'] = area
            perhouseinfo['buildtime'] = buildtime
            perhouseinfo['attention'] = attention
            perhouseinfo['show'] = show
            perhouseinfo['publishtime'] = publishtime
            perhouseinfo['tag'] = tag
            perhouseinfo['totalprice'] = totalprice
            perhouseinfo['unitprice'] = unitprice



#            print (json.dumps(perhouseinfo,indent=1,ensure_ascii=False))
#            格式化输出每个房源的所有信息
    

#            insertsql = 'INSERT INTO {tablename} (title,url,totalfloor,flood,houseinfo,addres,unitprice,totalprice,district,types,size,face,decoration,buildtime) \
#                        VALUES ("{title}","{url}","{followinfo}","{flood}","{houseinfo}","{addres}","{unitprice}","{totalprice}","{district}","{types}","{size}","{face}","{decoration}","{buildtime}")'\
#                        .format(tablename=TABLENAME,title=str(perhouseinfo["title"]),url=str(perhouseinfo["url"]),totalfloor=perhouseinfo["fotalfloor"],\
#                        flood=perhouseinfo['flood'],houseinfo=perhouseinfo['houseinfo'],addres=perhouseinfo['addres'],unitprice=perhouseinfo['unitprice'],\
#                        totalprice=perhouseinfo['totalprice'],district=perhouseinfo['district'],types=perhouseinfo['types'],size=perhouseinfo['size'],face=perhouseinfo['face'],decoration=perhouseinfo['decoration'],buildtime=perhouseinfo['buildtime'])
#            conn.execute(insertsql)
#        conn.commit()

            insertsql = 'INSERT INTO {tablename} (url,title,district,types,size,face,decoration,floor,totalfloor,area,buildtime,attention,show,publishtime,tag,totalprice,unitprice) \
                        VALUES ("{url}","{title}","{district}","{types}","{size}","{face}","{decoration}", \
                        "{floor}","{totalfloor}","{area}","{buildtime}","{attention}","{show}","{publishtime}", \
                        "{tag}","{totalprice}","{unitprice}") ' \
                        .format(tablename=tablename,url=str(perhouseinfo["url"]),title=str(perhouseinfo["title"]),district=perhouseinfo['district'],\
                        types=perhouseinfo['types'],size=perhouseinfo['size'],face=perhouseinfo['face'],decoration=perhouseinfo['decoration'],\
                        floor=perhouseinfo['floor'],totalfloor=perhouseinfo["totalfloor"],area=perhouseinfo['area'],\
                        buildtime=perhouseinfo['buildtime'],attention=perhouseinfo['attention'],show=perhouseinfo['show'],\
                        publishtime=perhouseinfo['publishtime'],tag=perhouseinfo['tag'],unitprice=perhouseinfo['unitprice'],\
                        totalprice=perhouseinfo['totalprice'])
#            print(insertsql)
            conn.execute(insertsql)
            conn.commit()
            
#        except Exception as e:
#            print(e)
#            pass


def createtable(db,tablename):
    try:
        conn = sqlite3.connect(db)
    except Exception as e:
        print ("Error: ",e)
        sys.exit(1)
    
    droptablesql = 'drop table  if exists {tablename}'.format(tablename=tablename)
#    createsql = 'create table {tablename} (title char, url char,followinfo char,flood char,houseinfo char,addres char,unitprice int,totalprice int,district char,type char,size int,face char,decoration char,buildtime char);'.format(tablename=TABLENAME)

#    create_ershoulianjia_sql = 'create table {tablename} (url char, title char,district char,\
#                types char,size int,face char,decoration char,floor int,\
#                totalfloor int,position char,buildtime int,attention int,\
#                show int,publishtime char,tag char, totalprice int,unitprice int);'\
#                .format(tablename=tablename)


    create_table_sql = 'create table {tablename} (url char, title char, district char, area char, road char, \
                types char,size int,face char,decoration char,floor int,\
                totalfloor int,position char,buildtime int,attention int,\
                show int,publishtime char,tag char, totalprice int,unitprice int);'\
                .format(tablename=tablename)


    conn.execute(droptablesql)
    conn.execute(create_table_sql)
#    conn.execute(insertsql)
    conn.commit()



def fangdd_perpage_info(page):

    conn = sqlite3.connect(db)

#    url = 'http://gz.lianjia.com/ershoufang/pg{page}'.format(page=page)
    url = 'http://esf.fangdd.com/guangzhou/list/pa{page}'.format(page=page)
    content = contents(url)
    soup = BeautifulSoup(content,'lxml')
    allhouse = soup.find_all(attrs={"class":"list-item clearfix"})
#    print(allhouse)

    for perhouse in allhouse:
            perhouseinfo = {}
#        try:
            try:
                left__tag = perhouse.find(attrs={"class":"orange left__top"}).text
            except:
                left__tag = None

            url = perhouse.find("a",attrs={"target":"_blank"}).get('href')
            name_title  = perhouse.find(attrs={"class":"name-title clearfix"}).text.strip(" ").strip('\n').split('\n')
            district = name_title[0]
            types = name_title[1]
            size = re.findall('\d+\.?\d+?',name_title[2])[0]

            detail_untreated = perhouse.find(attrs={"class":"detail"}).text.replace("\n",'').replace(" ",'').replace("\xa0",'|').split('|')
#            detail = detail_untreated.replace("\n",'').replace(" ",'')
            district = detail_untreated[0]
            area = detail_untreated[1]
            road = detail_untreated[3]
            floor = detail_untreated[5].split('/')[0]
            totalfloor = detail_untreated[5].split('/')[1]
            if re.findall('人预约看房',detail_untreated[-1]):
                show = re.findall('\d+',detail_untreated[-1])[0]
            else:
                show = None

            tag_untreated = perhouse.find(attrs={"class":"tag-group"}).text.strip().split('\n')
            tag = ','.join(tag_untreated)

            try:
                station = perhouse.find(attrs={"class":"stationNo"}).text.strip()
            except:
                station = None
            try:
                station_distance_untreated = perhouse.find("p",attrs={"class":"info-content pull-left"}).text.replace(" ",'').split('\n')
                station_distance = station_distance_untreated[7] + station_distance_untreated[9]
            except:
                station_distance = None
            
            price_untreated = perhouse.find(attrs={"class":"price-panel pull-right"}).text.replace("\n",'').replace("\ue68e\ue68f","").split(' ')
            unitprice = re.findall('\d+',price_untreated[1])[0]
            totalprice = re.findall('\d+',price_untreated[0])[0]
        
            perhouseinfo['url'] = url
            perhouseinfo['district'] = district
            perhouseinfo['area'] = area
            perhouseinfo['road'] = road
            perhouseinfo['types'] = types
            perhouseinfo['size'] = size
#            perhouseinfo['face'] = face
#            perhouseinfo['decoration'] = decoration
            perhouseinfo['floor'] = floor
            perhouseinfo['totalfloor'] = totalfloor
#            perhouseinfo['position'] = position
#             perhouseinfo['buildtime'] = buildtime
#             perhouseinfo['attention'] = attention
            perhouseinfo['show'] = show
#             perhouseinfo['publishtime'] = publishtime
            perhouseinfo['tag'] = tag
            perhouseinfo['totalprice'] = totalprice
            perhouseinfo['unitprice'] = unitprice


#            print (json.dumps(perhouseinfo,indent=1,ensure_ascii=False))
#            格式化输出每个房源的所有信息

            insertsql = 'INSERT INTO {tablename} (url,district,area,road,types,size,floor,totalfloor,show,tag,totalprice,unitprice) \
                        VALUES ("{url}","{district}","{area}","{road}","{types}","{size}", \
                        "{floor}","{totalfloor}","{show}", \
                        "{tag}","{totalprice}","{unitprice}") ' \
                        .format(tablename=tablename,url=str(perhouseinfo["url"]),district=perhouseinfo['district'],area=perhouseinfo['area'],\
                        road=perhouseinfo['road'],types=perhouseinfo['types'],size=perhouseinfo['size'],\
                        floor=perhouseinfo['floor'],totalfloor=perhouseinfo["totalfloor"],\
                        show=perhouseinfo['show'],\
                        tag=perhouseinfo['tag'],unitprice=perhouseinfo['unitprice'],\
                        totalprice=perhouseinfo['totalprice'])
#            print(insertsql)
            conn.execute(insertsql)
            conn.commit()
            
#        except Exception as e:
#            print(e)
#            pass


if __name__ == '__main__':
#    print(lianjia_totalpage(contents('http://gz.lianjia.com/ershoufang/')))
#    for i in list(lianjia_perpage_info(3).keys()):
#     print( [i for i in list(lianjia_perpage_info(3).keys())])
#     print('insertsql = INTO {tablename} (i for i in list(lianjia_perpage_info(3).keys()))')

    db = 'guangzhou.db'
    tablename = 'lianjiaershou'
    createtable(db,tablename)
    
    for page in range(101):
        lianjia_perpage_info(page)
        print("spider {} page".format(page))
        
    db = 'guangzhou.db'
    tablename = 'fangddershou'
    createtable(db,tablename)
#    fangdd_perpage_info(3)
    for page in range(21):
        fangdd_perpage_info(page)
        print("spider {} page".format(page))
    
