#!/usr/local/bin/python3
import urllib.request
import os
import time
from bs4 import BeautifulSoup

filename = "hrefs"
visited_filename = "visited_hrefs"
dir_name = "../scraped_files/"+time.strftime("%Y_%m_%d_%H_%M_%S",time.gmtime())
os.makedirs(dir_name)

THE_FILE = open(dir_name+"/"+filename,'w')
THE_VISITED_FILE = open(dir_name+"/"+visited_filename,'w')
THE_URL = 'https://freshharvest.deliverybizpro.com/home.php#'

page = urllib.request.urlopen(THE_URL).read()
soup =  BeautifulSoup(page,"html.parser")
urls = []

for a in soup.find_all('a'):
    href = a.get('href')

    if href[0:10] == "javascript":
        continue
    elif href[0]=="/" or href[0]=="#":
        path = "#" if href=="/home.php" else href
        href = THE_URL + path
    elif href[0].isalpha() and href[0:6]!="mailto" and href[0:4]!="http":
        href = THE_URL + "/" + href

    if href in urls:
        continue
    else:
        urls.append(href)
        THE_FILE.write(href + "\n")
THE_FILE.close()
THE_VISITED_FILE.write(THE_URL + "\n")
THE_VISITED_FILE.close()
