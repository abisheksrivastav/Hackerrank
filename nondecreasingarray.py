#you are given  an array A consiting of N positive integers. Your task is to find an array B of length N satisfying the following conditions:
#Bi > 0 for all 1 <= i <= N
#Bi <=B+1 for all 1 <= i <= N
#Bi is divisible by Ai for all 1 <= i <= N
#sigma Bi is minimum
#you are given T test cases
#!/usr/bin/env python3
# Path: minimumsum.py

# input format 
#(1)The first line contains a single integer T   denoting the number of test cases.
#(2)The first  line of each test case contains a single integer N  denoting the length of the array.
#(3)The second line of each test case contains N space separated integers A1, A2, ..., AN denoting the integer A  array.

# output format
#(1)For each test case (in a separate line), print   N space-separated integers denoting B1,B2...BN. If there are multiple answers, you can print any of them. It is guaranteed that under the given constraints at least 1 B  exists.

#hackerearth Non decreasing array link : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/non-decreasing-array-1/
#!/usr/bin/env python3
# Path: non-decreasingarray.py

def get_input_arr():
    return list(map(int, input().split()))
 
 
def get_input_int():
    return int(input())
 
 
def get_input_float():
    return float(input())
 
 
def get_input_str():
    return input()
 
 
def print_arr(arr):
    print(' '.join(map(str, arr)))
 
 
def solve():
    from math import ceil
    n = get_input_int()
    arr = get_input_arr()
    ans = [arr[0]]
    for i in range(1, n):
        k = ceil(ans[-1] / arr[i])
        ans.append(k*arr[i])
    print_arr(ans)
 
 
t = get_input_int()
for _ in range(t):
    solve()
            
