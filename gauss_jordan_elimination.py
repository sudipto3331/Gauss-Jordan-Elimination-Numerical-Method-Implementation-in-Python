#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:44:27 2023

@author: sudipto3331
"""

import xlrd
import numpy as np
from xlrd import open_workbook
from xlutils.copy import copy

workbook = xlrd.open_workbook('read.xls')
sheet = workbook.sheet_by_index(0)

arr = np.zeros((sheet.nrows, sheet.ncols))
arr2 = np.zeros((sheet.nrows, sheet.ncols))


# Taking excel data into numpy array

for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        arr[i][j] = sheet.cell_value(i,j)
        arr2[i][j] = sheet.cell_value(i,j)
        
# Calculate Echolon Matrix FOrward

for k in range(0, sheet.ncols):
    for i in range(k+1, sheet.nrows):
        temp = arr2[k][k]/arr2[i][k];
        for j in range(k, sheet.ncols):
            arr2[i][j] = (temp)*arr2[i][j]
            arr2[i][j] = arr2[i][j] - arr2[k][j]

for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        print(arr2[i][j]);

print("\n")

# Calculate Echolon Matrix Backward

for k in range(0, sheet.ncols):
    for i in range(k+1, sheet.nrows):
        print(arr2[i][i], arr2[k][i]);
        temp = arr2[i][i]/arr2[k][i];
        print(temp);
        for j in range(0, sheet.ncols):
            arr2[k][j] = (temp)*arr2[k][j]
            print(arr2[k][j])
            arr2[k][j] = arr2[k][j] - arr2[i][j]
            print(arr2[k][j])
        print("\n")

# Calculate Identity

for i in range(sheet.nrows):
    temp = arr2[i][i];
    for j in range(sheet.ncols):
        print("Divition:", arr2[i][j],"/", temp)
        arr2[i][j] = arr2[i][j]/temp;
        
# wb = Workbook()
rb = open_workbook("read.xls")
# sheet1 = wb.add_sheet('Sheet 1')
wb = copy(rb)
sheet1 = wb.get_sheet(1)

# Clearing all data of excel

for i in range(100):
    for j in range(100):
        sheet1.write(i,j, '');
        

for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        print(arr2[i][j]);
        sheet1.write(i,j,arr2[i][j])
    
wb.save('read.xls')
