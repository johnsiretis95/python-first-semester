
import os
name = raw_input("Give file name")
o = open(name,"r")
lines = o.readlines()
o.close()
o = open(name,"w")
for i in lines:
    if ( ("#" in i) == False):
        o.write(i)

o.close