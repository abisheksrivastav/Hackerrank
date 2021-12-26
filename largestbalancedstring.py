# You are given a string A, consisting of '(', ')', '[', ']', '{' and '}' only. 
# You have to find the maximum length of the balanced string after performing some valid operation(s).

#Valid operations are

#Remove any character from string A

#Swap any two adjacent characters of string A

#You can perform these valid operations in any order and any numbers of times.

op = ['(','{','[']
cl =[')','}',']']
t = int(input())
for _ in range(t):
    s = input()
    x=0
    for i in range(3):
       a=s.count(op[i])
       b=s.count(cl[i])
       x += 2*min(a,b)
    print(x)


        
    


            



    