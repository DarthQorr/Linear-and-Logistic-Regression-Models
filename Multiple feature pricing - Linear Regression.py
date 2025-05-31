# -*- coding: utf-8 -*-
"""
Created on Wed May 14 19:11:35 2025

@author: USER
"""

import csv

def optimise():
    with open("C:/Users/USER/Downloads/Size vs price data.csv", "r") as f:
        data_raw = csv.reader(f)
        data = list(data_raw)
        datii = []
        m = len(data)
        w1 = 0
        w2 = 0
        w3 = 0
        w4 = 0
        w5 = 0
        b = 0
        f = 0
        
        j_sum = 0
        diff_w1 = 0
        diff_w2 = 0
        diff_w3 = 0
        diff_w4 = 0
        diff_w5 = 0
        diff_b = 0
        count = 0
        
        avg1 = 0
        avg2= 0
        avg3 = 0
        avg4 = 0
        avg5 = 0
        avgy= 0
        
        std1 = 0
        std2 = 0
        std3 = 0
        std4 = 0
        std5 = 0
        stdy = 0
        
        # Finding mean
        for i in data:
            avg1 += float(i[0])
            avg2 += float(i[1])
            avg3 += float(i[2])
            avg4 += float(i[3])
            avg5 += float(i[4])
            avgy += float(i[5])
        avg1 = avg1/m
        avg2 = avg2/m
        avg3 = avg3/m
        avg4 = avg4/m
        avg5 = avg5/m
        avgy = avgy/m
        
        # Finding Standard Deviation
        for i in data:
            std1 += (float(i[0]) - avg1)**2
            std2 += (float(i[1]) - avg2)**2
            std3 += (float(i[2]) - avg3)**2
            std4 += (float(i[3]) - avg4)**2
            std5 += (float(i[4]) - avg5)**2
            stdy += (float(i[5]) - avgy)**2
        std1 = std1/m
        std2 = std2/m
        std3 = std3/m
        std4 = std4/m
        std5 = std5/m
        stdy = stdy/m
        
        # Datii!        
        for i in data:
            datii.append([(float(i[0])-avg1)/std1, (float(i[1])-avg2)/std2,
                          (float(i[2])-avg3)/std3, (float(i[3])-avg4)/std4,
                          (float(i[4])-avg5)/std5, (float(i[5])-avgy)/stdy])
                        
        # Updating Parameters!

        for j in range(10000):
            diff_w1 = 0
            diff_w2 = 0
            diff_w3 = 0
            diff_w4 = 0
            diff_w5 = 0
            diff_b = 0
            
            j_sum = 0
            count += 1
            alpha = 0.4
            
            # Calculating gradient Descent per iteration
            for i in datii:
                x1 = float(i[0])
                x2 = float(i[1])
                x3 = float(i[2])
                x4 = float(i[3])
                x5 = float(i[4])
                y = float(i[5])   
                f = w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + b
                
                diff_w1 += (f - y)*x1
                diff_w2 += (f - y)*x2
                diff_w3 += (f - y)*x3
                diff_w4 += (f - y)*x4
                diff_w5 += (f - y)*x5
                diff_b += (f - y)
            
            w1 = w1 - alpha*(1/m)*diff_w1
            w2 = w2 - alpha*(1/m)*diff_w2
            w3 = w3 - alpha*(1/m)*diff_w3
            w4 = w4 - alpha*(1/m)*diff_w4
            w5 = w5 - alpha*(1/m)*diff_w5            
            b = b - alpha*(1/m)*diff_b
            
            # Calculating Cost function per iteration
            for i in datii:
                x1 = float(i[0])
                x2 = float(i[1])
                x3 = float(i[2])
                x4 = float(i[3])
                x5 = float(i[4])
                y = float(i[5])
                f = w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + b
                
                j_sum += (f - y)**2
                
            cost = 1/(2*m)*(j_sum)
            
            print("Iter","w1","w2","w3","w4","w5","b","Cost")
            print(count, w1,w2,w3,w4,w5,b,cost)
            print()
        
        return [w1,w2,w3,w4,w5,b],[avg1,avg2,avg3,avg4,avg5,avgy],[std1,std2,std3,std4,std5,stdy]


lis,average,stand = optimise()
test = [[4350,3,3,4050,35000]]

for i in test:
    x1 = (i[0] - average[0])/stand[0]
    x2 = (i[1] - average[1])/stand[1]
    x3 = (i[2] - average[2])/stand[2]
    x4 = (i[3] - average[3])/stand[3]
    x5 = (i[4] - average[4])/stand[4]
    
    f = lis[0]*x1 + lis[1]*x2 + lis[2]*x3 + lis[3]*x4 + lis[4]*x5 + lis[5]
    f = (f*stand[5])+average[5]

print("$"+str(f))
