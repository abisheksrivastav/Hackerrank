#There are  N numbers A1,A2...An  , and you are given Q queries. In each query, you are given two integers l and r .

#You are required to print the sum of all the numbers whose frequency of occurrence is between l  and r (including l andr ). Print a single integer for each query in a new line.

# Input format

#The first line contains N denoting the size of the array.
#The second line contains N integers denoting the elements of the array.
#The third line contains Q denoting the number of queries.
#Next  lines Q contains l  and r. 
#Output format
#For each query, print the sum of all elements of the array whose frequency of occurrence is between l and  r (inclusive) in a new line.

#sample input
#8
#4 4 6 5 3 3 3 9
#4
#1 4
#2 7
#3 7
#5 6
#sample output
#37
#17
#9
#0
#Explanation In the first query we need to output the sum of all the numbers whose frequency of occurrecne is between 1 and 4 (inclusive). Here all the given numbers have their frequecny between 1 and 4. 3 occurs 3 times, 4 occurs 2 times, 5, 6, 9 occurs 1 time. So total sum would be 3+3+3+4+4+5+6+9 = 37.

from collections import Counter
'''N = int(input())
arr = list(map(int, input().split()))
res = Counter(arr)
Q = int(input())
for _ in range(Q):
    l,r = map(int, input().split())
    sum = 0
    for value,key in res.items():
        if key>=l and key<=r:
            sum+=(value*key)
    print(sum)'''
 
from sys import stdin
from collections import Counter
 
N = int(input())
arr = list(map(int, input().split()))
counts = Counter(arr)
psums = [0]*(max(counts.values())+1) 
for num,count in counts.items():
    psums[count] += num*count
 
for i in range(1,len(psums)):
    psums[i] += psums[i-1]
 
Q = int(input())
 
for q in range(Q):
    l,r = map(int, stdin.readline().split())
    r = min(len(psums)-1,r)
    l = min(len(psums),l)
 
    print(psums[r]-psums[l-1])