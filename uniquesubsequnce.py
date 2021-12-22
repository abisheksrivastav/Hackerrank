# to determine the size and the unique subsequence of a given string such that no two  adjacent character are same */

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    count = 0
    for j in range(n-1):
        if s[j] != s[j+1]:
            count += 1
    print(count+1)

