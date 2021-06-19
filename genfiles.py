from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import argparse
import sys
import getopt

lista= open('results/itemlinks_noeline.txt', 'r')

anchorlist = []
anchorlist2 = []
anchorlist3 = []
str1 = ""
 
for line in lista :
    if line != "\n" :
        req = Request(line)
        html_page = urlopen(req)

        #   load into bs4
        soup = BeautifulSoup(html_page, "lxml")

        animageurl = soup.find(id='viEnlargeImgLayer_img_ctr')     #Picture
        
        anid = soup.find(id='itemTitle')    #Title
        #anabout = soup.find('body')     #About

        anprice = soup.find(id='prcIsum')     #Price
        anshipping = soup.find(id='fshippingCost')     #Ship Cost
        
        str1 = "#!\nanid : " + str(anid) + "\nanprice : " + str(anprice) + "\nanimageurl : " + str(animageurl) +  "\nanshipping : " + str(anshipping) + "\n"
         
        print(str1)
        
#for i in range(len(anchorlist)):
 
