#!/usr/bin/env python
#make a text file with all the details
pathtolinks='results/links.txt'

import argparse
import sys
import getopt
import os

tmp = ""
   
#new list NEED TO CONSOLIDATE
linklist = []
booklist = set()
username = 'futon5'

# open links grabbed from earlier
txt = open(pathtolinks, 'r')

for x in txt:
  if x.startswith("http") == True and x.find(str("/itm/")) > -1:
    linklist.append(x)
          
txt.close()

mylist = list(dict.fromkeys(linklist))
#print(mylist)

for k in range(len(linklist)) :
    print (str(linklist[k]))
	
	  #if x.startswith("http") == True and xfind(str("ssn=" + username)) >-1 and x.find(str("sch/m.html?")) < 0:
          
