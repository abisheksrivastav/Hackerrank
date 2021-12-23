#Harry was studying a magic book that categorizes the magic spells into 3 categories - 
# Good , Worst and Bad. If any spell contains all the vowels in alphabetical order then that spell is categorized as Good. 
# If it contains the vowels in reverse alphabetical order , then that spell is categorized as Worst. 
# All the other spells that do not fall in any of the categories before are categorized as Bad


  k = int(input().strip())
p = "aeiou"
for _ in range(k):
    s = input().strip()
    v = []
    for i in s:
        if i in p:
            v.append(i)
    r = []
    for k in p:
        for j in v:
            if j == k:
                r.append(k)
    if r == v:
        print("Good")
    elif  v==r[-1::-1]:
        print("Worst")
    else:
        print("Bad")       
    