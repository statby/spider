#!/bin/env python3
# coding=utf-8
# Filename    : writeexel.py
# Date        : 2016-03-31 21:08:44
# Author      : Statby
# Description : 

import xlwt
font = xlwt.Font()

wb = xlwt.Workbook()
ws = wb.add_sheet('page1')

ws.write(0,0,'test')
wb.save('test_excel.xls')
