# you are given two string S and T of length N . your task is to convert string S into string T by doing some operations
# in operation you  can delete the first character of the string S and append any character at the end of the string.
# s= aaxaabc
# t = aabcaax

# after first operation s = axaabca
#  after second operation s = xaabcaa
# after third operation s = aabcaax
# after third operation s and t are same string


n = int(input())
s = input()
t = input()
#brute force approach
count = 0
for i in range(n):
    if(t.find(s[i:n])==-1):
        count+=1
        
print(count)






