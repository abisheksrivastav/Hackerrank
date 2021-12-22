#make a python function in  decorators! of a  given N mobile numbers. Sort them in ascending order then print them in the standard format shown below:
# 
#The given mobile numbers may have ,  or  written before the actual  digit number. Alternatively, there may not be any prefix at all.
#Sample Input

#3
#07895462130
#919875641230
#9195969878

# sample output
#+91 78954 62130
#+91 91959 69878
#+91 98756 41230
# python decorators 
#!/usr/bin/env python3
# Path: decorators.py

def wrapper(f):
    def fun(l):
        f(["+91 " + i[-10:-5] + " " + i[-5:] for i in l])
    return fun
