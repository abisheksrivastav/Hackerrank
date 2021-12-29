# Creatnx now wants to decorate his house by flower pots. He plans to buy exactly N  ones. 
# He can only buy them from Triracle's shop. There are only two kind of flower pots available in that shop.
#  The shop is very strange. 
# If you buy X flower pots of kind 1 then you must pay A*X^2 and B*Y^2 if you buy  Y flower pots of kind 2. 
# Please help Creatnx buys exactly N flower pots that minimizes money he pays.
# Input Format
# The first line contains an integer T, the number of test cases.
# Each of test case is described in a single line containing three space-separated integers N, A, B.
# Output Format
#For each test case, print a single line containing the answer.

def minCost(n,a,b):
    return round((n*b)/(a+b))

def  findCost(a,b,x,y):
    return a*x*x + b*y*y

t= int(input())
for i in range(t):
    n,a,b = map(int,input().split())
    z = minCost(n,a,b)
    print(findCost(a,b,z,n-z))




 
  


    
    

# Sample Input
# 2
# 5 1 2
# 10 2 4
# Sample Output
# 17
#134

