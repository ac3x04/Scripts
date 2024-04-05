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
response = requests.get(wwwArg)
print(response.request.headers)
print(response.status_code)
print(response.headers)
print(response.content)
