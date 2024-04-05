#!/bin/bash
#title           :curl.sh
#description     :This script is meant to show using a curl to do a GET request to a website. This is an example of an early style bot.
#author		 :Ace Xor
#date            :2023-10-25
#version         :0.1
#usage		 :bash curl.sh <website>

curl -vLlk $1 -o /dev/null
