# from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import argparse
import sys
import getopt


#need to grab urls from txt or something
firsturl = "https://www.ebay.com/sch/futon5/m.html?_nkw=&_armrs=1&_ipg=&_from="
anchorlist = []
anchorlist2 = []
anchorlist3 = []
str1 = ""
str2 = ""

parser = argparse.ArgumentParser()
parser.add_argument('--url', action='store', dest='url')
args = parser.parse_args()
url = args.url

req = Request(url)


html_page = urlopen(req)

#load into bs4
soup = BeautifulSoup(html_page, "lxml")

#get all links
for link in soup.findAll('a'):
   anchorlist.append(str(link.get('href')))
   anchorlist3.append(str(link.get('class')))
   anchorlist2.append(str(link.text))
   str2 = str(link.get('href'))
   str1 = str1 + str2 + "\n"

#print string
print(url + "\n\n")
print("Appended anchorlist\n\n")
for i in range(len(anchorlist)):
    #print("IDX " + str(i) + " : HREF : " + "#" + anchorlist[i] + "# \n\tCLASS : " + anchorlist3[i] + " TEXT : " + anchorlist2[i]  + "\n")
    print(str(anchorlist[i]) + "\n")

