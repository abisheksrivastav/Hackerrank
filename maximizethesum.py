#hackerearth Maximum sum of subarray link :https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximize-sum-0423b95e/

#!/usr/bin/env python3
# Path: maximizethesum.py
# You are given an array   A of     N integers. You want to choose some integers from the array subject to the condition that the number of distinct integers chosen should not exceed  K. Your task is to maximize the sum of chosen numbers. 
# you are given T test cases

#input format
#(1)The first line contains a single integer T   denoting the number of test cases.
#(2)The first line of each test case contains two space-separated integers N  and  K denoting the length of the array and the maximum number of distinct integers you can choose.
#(3)The second line of each test case contains N space-separated integers denoting the integer array A.

#output format 

#For each test case(in a separate line), print the maximum sum you can obtain by choosing some elements such that the number of distinct integers chosen is at most K . If you cannot choose any element, output 0.

t=int(input())
for test in range(t):
    ans=[]
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    # print(a)
    num_arr=[0]*n
    arr.sort()
    last_item=arr[-1]
    i=0
    while len(arr)>0:
        if(arr[-1]<0):
            break
        if(last_item!=arr[-1]):
            # print(last_item,arr[-1])
            i+=1
        last_item=arr[-1]
        num_arr[i]+=arr[-1]
        arr.pop()

    num_arr.sort()
    print(sum(num_arr[-k:]))

