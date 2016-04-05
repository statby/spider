#!/bin/env python3
# coding=utf-8
# Filename    : get_global_site_ranking.py
# Date        : 2016-03-30 23:28:28
# Author      : Statby
# Description : 

import requests
from bs4 import BeautifulSoup

def get_area_url():
    #获取所有未过滤所有地区url列表
    data = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',}
    site = 'http://alexa.chinaz.com/Country/index.html'
    req = requests.get(site, headers=headers)
    req.encoding = 'utf-8'
    status = req.status_code
    soup = BeautifulSoup(req.text, 'lxml')
    urls = soup.select(' div > div > a ')
    return urls
    
print (get_area_url())
       
def get_urls(): 
    #获得所有地区request url
    sum = []
    for area_name in get_area_url():
        sum.append(area_name.get('href'))
    filter = [f for f in sum if 'index' in f] 
    # 过滤非国家列表
    return filter

def get_area_names():
    #获得所有地区requests url最后一段
    names = [a.split('/')[2] for a in get_urls() if '/' in a]
    return names

#print(get_area_names())


area_urls='''
/Country/index_CN.html
/Country/index_US.html
/Country/index_FR.html
/Country/index_FR.html
/Country/index_DE.html
/Country/index_JP.html
/Country/index_KR.html
/Country/index_SE.html
/Country/index_CH.html
/Country/index_HK.html
/Country/index_MO.html
/Country/index_TW.html
/Country/index_TH.html
/Country/index_BH.html
/Country/index_BR.html
/Country/index_CL.html
/Country/index_DK.html
/Country/index_EG.html
/Country/index_GH.html
/Country/index_GR.html
/Country/index_IS.html
/Country/index_IN.html
/Country/index_FI.html
/Country/index_JO.html
/Country/index_MM.html
/Country/index_IR.html
/Country/index_NO.html
/Country/index_OM.html
/Country/index_NL.html
/Country/index_PE.html
/Country/index_PL.html
/Country/index_ZA.html
/Country/index_VN.html
/Country/index_YE.html
/Country/index_AR.html
/Country/index_AT.html
/Country/index_BA.html
/Country/index_BE.html
/Country/index_KH.html
/Country/index_CA.html
/Country/index_HU.html
/Country/index_IQ.html
/Country/index_IE.html
/Country/index_IL.html
/Country/index_IT.html
/Country/index_JM.html
/Country/index_KE.html
/Country/index_KW.html
/Country/index_MA.html
/Country/index_NP.html
/Country/index_NZ.html
/Country/index_LT.html
/Country/index_LU.html
/Country/index_PA.html
/Country/index_PY.html
/Country/index_MK.html
/Country/index_MT.html
/Country/index_MX.html
/Country/index_PH.html
/Country/index_PT.html
/Country/index_QA.html
/Country/index_SG.html
/Country/index_RU.html
/Country/index_TN.html
/Country/index_TR.html
/Country/index_UA.html
/Country/index_UY.html
/Country/index_ES.html
/Country/index_AM.html
/Country/index_AU.html
/Country/index_AZ.html
/Country/index_BD.html
/Country/index_BB.html
/Country/index_BY.html
/Country/index_BO.html
/Country/index_BG.html
/Country/index_CO.html
/Country/index_HR.html
/Country/index_CY.html
/Country/index_EC.html
/Country/index_SV.html
/Country/index_SV.html
/Country/index_GT.html
/Country/index_HN.html
/Country/index_GE.html
/Country/index_MY.html
/Country/index_LV.html
/Country/index_NI.html
/Country/index_NG.html
/Country/index_MQ.html
/Country/index_MU.html
/Country/index_MD.html
/Country/index_PK.html
/Country/index_PS.html
/Country/index_PR.html
/Country/index_RE.html
/Country/index_RO.html
/Country/index_VE.html
/Country/index_RS.html
/Country/index_SK.html
/Country/index_LK.html
/Country/index_AL.html
/Country/index_DZ.html
/Country/index_CR.html
/Country/index_CZ.html
/Country/index_GP.html
/Country/index_ID.html
/Country/index_KZ.html
/Country/index_MG.html
/Country/index_ME.html
/Country/index_SA.html
/Country/index_SI.html
/Country/index_KG.html
/Country/index_UZ.html
/Country/index_DO.html
/Country/index_TT.html
/Country/index_AE.html
/Country/index_BA.html
'''


