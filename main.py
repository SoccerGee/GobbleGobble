#! /usr/local/bin/python3
import urllib.request
import os
import time
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="pass the URL that you would like to analyze")
args = parser.parse_args()

filename = "hrefs"
visited_filename = "visited_hrefs"
rejected_filename = "rejected_hrefs"

dir_name = "./.%%"+time.strftime("%m_%d_%H_%M_%S",time.gmtime())
os.makedirs(dir_name)

THE_FILE = open(dir_name+"/"+filename,'w')
THE_VISITED_FILE = open(dir_name+"/"+visited_filename,'w')
THE_REJECTED_FILE = open(dir_name+"/"+rejected_filename,'w')

THE_URL = args.url

page = urllib.request.urlopen(THE_URL).read()
soup =  BeautifulSoup(page,"html.parser")
urls = []

for a in soup.find_all('a'):
    default_url = THE_URL
    href = a.get('href')

    if href[0:10] == "javascript":
        THE_REJECTED_FILE.write(href + "\n")
        continue
    elif href[0]=="/" or href[0]=="#":
        href = "#" if href=="/home.php" else href
    elif href[0:6]=="mailto":
        THE_REJECTED_FILE.write(href + "\n")
        continue
    elif href[0:4]=="http":
        default_url = ""
    elif href[0].isalpha():
        href = "/" + href

    if href in urls:
        continue
    else:
        urls.append(href)
        THE_FILE.write(default_url + href + "\n")

THE_FILE.close()
THE_VISITED_FILE.write(THE_URL + "\n")
THE_VISITED_FILE.close()
