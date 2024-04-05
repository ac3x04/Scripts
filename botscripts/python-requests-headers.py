#!/opt/homebrew/bin/python3
#title           :python-requests.py
#description     :This script will use the python requests module to make a get request on a website. This is to showcase the evolution of basic command line tools as bots.
#author		 :Ace Xor
#date            :2023-10-25
#version         :0.1
#usage		 :python python-requests.py <website>
#notes           :The requests library is required to run this script

import requests
import sys

wwwArg = "https://" + str(sys.argv[1])
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0", "Accept-Language" : "en-US,en;q=0.5", "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Referer" : "https://www.google.com/", "Accept-Encoding" : "gzip, deflate", "Upgrade-Insecure-Requests" : "1"}
response = requests.get(wwwArg, headers=headers)
print(response.request.headers)
print(response.status_code)
print(response.headers)
print(response.content)
