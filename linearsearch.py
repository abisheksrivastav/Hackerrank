# You have been given an array of size N consisting of integers. 
# In addition you have been given an element M you need to find 
# and print the index of the last occurrence of this element M in the array if it exists in it, 
# otherwise print -1. Consider this array to be 1 indexed

# Input Format
# The first line of input contains an integer N.
# The next line contains N space separated integers denoting the array.
# The last line contains an integer M.

n,m = input().split()
n = int(n)
m = int(m)

array = list(map(int,input().split()))

for i in range(n-1,-1,-1):
    if array[i] == m:
        print(i+1)
        break

else:
    print(-1)
