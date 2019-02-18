# Solution to problem 2
# Rebecca Turley, 2019-02-18
# BeginswithT.py


import datetime

now = datetime.datetime.now().strftime("%a")




print (now)
if now == "Tue":
  print ('Yes - today begins with a T.')
elif now == "Thurs":
  print ('Yes - today begins with a T.')
else:
  print ('No - today does not begin with a T')