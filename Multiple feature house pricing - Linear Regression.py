# -*- coding: utf-8 -*-
"""
Created on Sat May 31 13:54:46 2025

@author: USER
"""

import csv

def optimised():
    with open("C:/Users/USER/Downloads/ML/Size vs price data.csv", "r") as f:
        rounds = int(input("Enter number of iterations the data must be trained on: "))
        data_raw = csv.reader(f)
        data = list(data_raw)
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
        
        for j in range(rounds):
            diff_w1 = 0
            diff_w2 = 0
            diff_w3 = 0
            diff_w4 = 0
            diff_w5 = 0
            diff_b = 0
            
            j_sum = 0
            count += 1
            alpha = 0.000000001
            
            # Calculating gradient Descent per iteration
            for i in data:
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
            for i in data:
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
        
        return w1,w2,w3,w4,w5,b


lis = optimised()
test = [2150,3,2,1710,14000]

f = lis[0]*test[0] + lis[1]*test[1] + lis[2]*test[2] + lis[3]*test[3] + lis[4]*test[4] + lis[5]
print("$",f,"is the price of the house!")