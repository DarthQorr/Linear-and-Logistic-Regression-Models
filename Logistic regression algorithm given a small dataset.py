# -*- coding: utf-8 -*-
"""
Created on Sat May 31 14:05:42 2025

@author: USER
"""

X = [[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]]
Y = [0, 0, 0, 1, 1, 1]

w1 = 0
w2 = 0
b = 0
e = 2.7182818284590452353602874713527
alpha = 200
m = len(X)
count = 0
rounds = int(input("Enter number of iterations to be trained on: "))

for k in range(rounds):
    count += 1
    diffw1 = 0
    diffw2 = 0
    diffb = 0
    j = 0
    
    # Calculting Gradient Descent
    for i in range(m):
        x1 = X[i][0]
        x2 = X[i][1]
        y = Y[i]
        
        f = w1*x1 + w2*x2 + b
        g = 1/(1+e**(-f))
        
        diffw1 += (g - y)*x1
        diffw2 += (g - y)*x2
        diffb += (g - y)
    

    
    # Calculating Cost Function
    for i in range(m):
        x1 = X[i][0]
        x2 = X[i][1]
        y = Y[i]
        
        f = w1*x1 + w2*x2 + b
        g = 1/(1+e**(-f))
        
        j += (g - y)**2

    print("Sl. W1   W2  b   Cost")
    print(count,w1,w2,b,j)
    print()        
    
    w1 = w1 - alpha*diffw1/m
    w2 = w2 - alpha*diffw2/m
    b = b - alpha*diffb/m
    j = j/(2*m)

