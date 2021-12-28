# In this problem, we define "set" is a collection of distinct numbers. 
# For two sets A and B , we define their sum set is a set S (A+B) = {a+b|a belongs A , b belongs B} . 
# In other word,  set S(A+B) contains all elements which can be represented as sum of an element in A
#  and an element in B  . Given two sets A,C , your task is to find set B   of positive integers less than
#  or equals 100  with maximum size such that  S(A,B) = C. 
# It is guaranteed that there is unique such set

# input format
#The first line contains N denoting the number of elements in set A, 
# the following line contains  N space-separated integers ai denoting the elements of set A .
# The third line contains M denoting the number of elements in set C, 
# the following line contains  M space-separated integers ci denoting the elements of set C .





n = int(input()) # number of elements in set A
a = list(map(int, input().split())) # elements of set A
m = int(input()) # number of elements in set C
c = list(map(int, input().split())) # elements of set C
b=[] # elements of set B
maximum_a = max(a) # maximum element in set A
maximum_c= max(c) # maximum element in set C
for i in range(abs(maximum_a-maximum_c)+1): # loop for elements of set B
    
    count = 0 # count of elements in set B

    for j in a: # loop for elements of set A

     if i+j in c: # if element of set B is in set C

        count += 1 # increment count of elements in set B

    if count == n:# if count of elements in set B is equal to number of elements in set A

        b.append(i) # append element of set B

b.sort() # sort elements of set B

print(" ".join(map(str, b))) # print elements of set B




   
