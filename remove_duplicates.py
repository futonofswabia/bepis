#list of duplicates
import argparse
import sys
import getopt
import os


parser = argparse.ArgumentParser()
parser.add_argument('--path', action='store', dest='path')
args = parser.parse_args()

path =args.path


bepis = ""

harray = []
huarray = []

txt = open(path, 'r')


for line in txt :
    harray.append(line)

harray.sort()

tmp = harray[0]
huarray.append(tmp)
i = 1
while i < len(harray):
 if harray[i] != tmp : 
    huarray.append(harray[i])
    tmp = harray[i]
 i += 1
for k in huarray :
    print(k)
