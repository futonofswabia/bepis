from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import argparse
import sys
import getopt
import os


######GRAB ALL PAGES
pathtolinks='results/pages.txt'
txt = open(pathtolinks, 'r')

sttt = ""

for line in txt :
    sttt = sttt + str(line)

styt = sttt.split("#")
for j in range(len(styt)):
    print("uououo: " + str(j) + "uououououo: " + str(styt[j]) + "\n")
txt.close()

#python getlinks.py --url "https://www.ebay.com/sch/futon5/m.html?_nkw=&_armrs=1&_ipg=&_from=" > results/links.txt
#Executes terminal commands for each page

com1 = "python getlinks.py --url "
com2_over = " > results/links.txt\n"
com2_appd = " >> results/links.txt\n"

kom1 = com1 + '"' + styt[1] + '"' + com2_over
kom2 = com1 +  '"' + styt[3] +  '"' + com2_appd

print(kom1)
print("\n")
print(kom2)

os.system(kom1)
os.system("\n")
os.system(kom2)
os.system("\n")
