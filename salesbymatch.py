#There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

#Function Description

#Complete the sockMerchant function in the editor below.

#sockMerchant has the following parameter(s):

#int n: the number of socks in the pile
#int ar[n]: the colors of each sock
#Returns

#int: the number of pairs

#int n: the number of socks in the pile
#int ar[n]: the colors of each sock
#Returns the number of matching pairs of socks.
# Complete this function with math and return the result

def sockMerchant(n, ar):
    # Write your code
    #socks = {}
    #for i in range(n):
    #    if ar[i] in socks:
    #        socks[ar[i]] += 1
    #    else:
    #        socks[ar[i]] = 1
    #print(socks)
    #print(len(socks))
    #print(len(socks.values()))
    #print(len(socks.values())/2)
    #print(int(len(socks.values())/2))
    #return int(len(socks.values())/2)
    d = dict()
    for i in ar:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    count = 0
    for key in d:
        count += d[key]//2
    return count
    
    

    

n = int(input())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)