#!/bin/env python3
# coding=utf-8
# Filename    : readexel.py
# Date        : 2016-04-01 10:52:15
# Author      : Statby
# Description : 

import xlrd

rb = xlrd.open_workbook('test_excel.xls')
table = rb.sheets()[0]
table = rb.sheet_by_index(0)
rows = table.nrows
ncols = table.ncols
for rownum in range(1,table.nrows):
    print (table.row_values(rownum))
