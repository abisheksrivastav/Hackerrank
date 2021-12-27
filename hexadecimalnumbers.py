# You are given a range [L,R]. 
# You are required to find the number of integers  in the range such that GCD(X,F(X)) >1  where F(X)
#  is equal to the sum of digits of X  in its hexadecimal (or base 16) representation.

#For example F(27) =1 +B = 1+ 11=12(27 in Hexadecimal is written as 1B ),  . You are aksed   T 
# such questions. 

# Input Format


#The first line contains a positive integer T denoting the number of questions that you are asked.
#Each of the next T lines contain two integers  L and  R denoting the range of questions.

# sample input
# 3 
#1 3 
# 5 8 
# 7 12 
# output format
# Print the number of integers in the range such that GCD(X,F(X)) >1  where F(X)
#  is equal to the sum of digits of X  in its hexadecimal (or base 16) representation.
# 2
# 4
# 6




#!/bin/python3
import math

def hexadecimal(n):
    sum =0
    while n>0:
        sum += n%16
        n = n//16
    return sum
 


t  = int(input())
for i in range(t):
    l, r = map(int, input().split())
    count = 0
    for n in range(l, r + 1):
        if (math. gcd(n, hexadecimal(n)) > 1):
            count += 1
    print(count)





    
    