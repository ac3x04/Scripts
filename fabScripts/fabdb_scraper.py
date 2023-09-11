#/usr/bin/python3

"""Connects to fabdb and gets all information about a cards from each set

This script will create a valid json object that contains all of the cards from each set from the popular trading card game flesh and blood
"""

import requests
import os
import json
import time

__author__ = "Ace Xor"
__copyright__ = "Copyright 2023"
__credits__ = ["Festus Pemberton", "Fabdb API"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ace Xor"
__email__ = "ac3x04@gmail.com"
__status__ = "Dev"
__version__ = "0.1.0"

allSets = {"WTR" : "225", "ARC" : "218", "CRU" : "197", "MON" : "306", "ELE" : "237", "EVR" : "197", "UPR" : "225", "OUT" : "238", "DTD" : "235"}
scriptHeader = {'User-Agent' : "fabCardScraper"}
allCardsList = []

def cardScraper(setId, setNum):
    #"curl https://api.fabdb.net/cards/$i$j" => bash command to get single card. 
    #cards is the api endpoint
    #This function returns a string of json text about the card
    if int(setNum) < 10:
        url = "https://api.fabdb.net/cards/" + str(setId) + "00" + str(setNum)
        print(url)
    elif int(setNum) < 100:
        url = "https://api.fabdb.net/cards/" + str(setId) + "0" + str(setNum)
        print(url)
    else:
        url = "https://api.fabdb.net/cards/" + str(setId) + str(setNum)
        print(url)
    try:
        request = requests.get(url, headers = scriptHeader)
        return request.text
    except Exception as e:
        print(e)

def fullSet(setId, cardCount):
    #This function uses the card scraper to scrape each card in a set
    cardsList = []
    for cardNum in range(int(cardCount) + 1):
        cardsList.append(cardScraper(setId, cardNum))
        time.sleep(1.5)
    return cardsList

def jsonify(aList):
    #Converts a list to a json object
    return json.dumps(aList)

for fabSet in allSets:
    allCardsList.append(fullSet(fabSet, allSets[fabSet]))

print(allCardsList)
#with open("fulldb.json", "rw") as jsonFile:
#    pass

