#Two strings A and   B comprising of lower case English letters are compatible if they are equal or can be made equal by following this step any number of times
#Your task is to determine if given strings A and  b are compatible.

# output format 
# print "yes"if string A can be converted to string B otherwise print "NO"

str1 = input()
str2 = input()

if len(str1) == len(str2):
    for i  in range(len(str1)):
        if str1[i] > str2[i]:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")
          
      