# You have N  rectangles. 
# A rectangle is golden if the ratio of its sides is in between[1.6,1.7], both inclusive. 
# Your task is to find the number of golden rectangles.

# Input Format
# The first line contains an integer N denoting the number of rectangles.
# Each of the next N lines contains two integers W,H  and  denoting the Width and height 
# of the rectangle respectively.

# sample input 
# 5
# 10 1
# 165 100 
# 180 100 
# 170 100
# 160 100

# There are three golden rectangles: (165, 100), (170, 100), (160, 100).

# how many golden rectangles are there?

n = int(input())
count = 0
for _ in range(n):
    w,h = list(map(int,input().split()))
    if( w/h>=1.6 and w/h<=1.7) or (h/w>=1.6 and h/w<=1.7):
        count+=1
print(count)





