#you are given a string S consisting of lowercase English alphabets.A good subsequence of this string is a subsequence which contains distinct
#Determine the number of good subsequences of the maximum possible length modulo 10^9+7.
#n other words, determine the length X of the longest good subsequence and the number of good subsequences of length X modulo 10^9+7.

#input format 
#The first line contains an integer T denoting the number of test cases.
#each of the next T lines contains a string S.

#include <iostream>

#define MOD 1000000007

#define ll long long


 

from collections import Counter
 
for i in range(int(input())):
   # s= list(set(input()))
   s=input()
   ans=1
   c=Counter(s).values()
   for i in c:
       ans*=i
   print(ans%(10**9+7))