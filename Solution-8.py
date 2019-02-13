# Solution to problem 8
# Rebecca Turley, 2019-02-13
# python datetime.py


import datetime

now = datetime.datetime.now().strftime("%a, %B %d %Y at %I:%M %p")

print (now)