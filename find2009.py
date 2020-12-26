# -*- coding: utf-8 -*-

import pandas as pd
title='专利'
subtrain = pd.read_excel('data/2019.xlsx',sheet_name=[title])
xingming = []
xuehao = []
index=-1
indes=[]


for side in subtrain[title].所有发明人:
    index+=1
    for ss in side.split(";"):
        print (ss)
        if '（学）' in ss:
            xuehao.append(ss[:-3])
            indes.append(index)
for side in subtrain[title].奖励人:
    xingming.append(side)
new=[]
for xing in indes:
    new.append(xingming[xing])
print(new)



f = pd.ExcelFile('./data/student.xls')
f.sheet_names  # 获取工作表名称
data = pd.DataFrame()
yao = []
teachername=[]
for i in f.sheet_names[:-1]:
    try:
        print (i)
        student = pd.read_excel('data/student.xls',header = [1],sheet_name=i)
        for name in student.姓名:
            yao.append(name)
        if '导师姓名' in student:
            for teacher in student.导师姓名:
                # print (teacher)
                teachername.append(teacher)
        if '备注' in student:
            for teacher in student.备注:
                # print (teacher)
                teachername.append(teacher)
    except Exception as e:
        continue
print (len(teachername))
print (len(yao))
count  =0
for key,value in at.items():
    if key in yao:
        print ("=============<<<", key, value)
        count +=1
        print ("find")
print (float(count),len(yao))
