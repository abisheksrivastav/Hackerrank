#In Python, a string of text can be aligned left, right and center
#.ljust(width), .rjust(width), .center(width)


#!/usr/bin/env python3
thickness = int(input("Enter the thickness: "))
c = 'H'

 #Top cone

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

  #Top Pillars
  #   H
  #  HHH
  # HHHHH
  #HHHHHHHH
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

  #Middle Belt
  #HHHHHHHH
  #HHHHHHHH
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

  #Bottom Pillars
  #   H
  #  HHH
  # HHHHH
  #HHHHHHHH
for i in range(thickness+1):
      print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

  #Bottom Cone
  #   H
  # HHHHH
  # HHHHH
  # HHHHH
  # HHHHH
  # HHHHH
  # HHHHH
  # HHHHH
  #  HHH
  #   H
for i in range(thickness+1):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
      




