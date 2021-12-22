# There is a frog initially placed at the origin of the coordinate plane. In exactly  second, the frog can either move up  unit, move right  unit, or stay still. In other words, from position , the frog can spend  second to move to:

#After  seconds, a villager who sees the frog reports that the frog lies on or inside a square of side-length  with coordinates , , , . Calculate how many points with integer coordinates on or inside this square could be the frog's position after exactly  seconds

#hackerearth algorithms linear search counting frog path 

# input format 
# The first and only line of input contains four space-separated integers: X, Y, s, and T .
# Output format
#Print the number of points with integer coordinates that could be the frog's position after T seconds.


# Sample Input
#2 2 3 6
# Sample Output
#6


#!/bin/python3
x,y,s,t = map(int,input().split())

total=0

for i in range(x,x+s+1):

    for j in range(y,y+s+1):

        if(i+j<=t):

            total+=1

print(total)


