#!/bin/bash

#This is a quick and dirty bash script to install demonsaw on Debian based systems written by Acexor
#twitter @acexor site: acexor.com
#Also big thanks to negativerad on youtube and github - https://gist.github.com/negativerad/712ecd52ddea1548b2f0

mkdir ~/Downloads/demonsaw

MACHARCH=`uname -m`

echo ""
echo "Downloading Demonsaw based on your machine's arch..."
echo ""

if [ $MACHARCH == 'x86_64' ]; then
	wget -P ~/Downloads/demonsaw https://www.demonsaw.com/download/v2-01/demonsaw_linux64.zip
else
	wget -P ~/Downloads/demonsaw https://www.demonsaw.com/download/v2-01/demonsaw_linux32.zip
fi

echo ""
echo ""

echo "Downloading libraries needed to run demonsaw next, you should be prompted for your sudo password"

sudo apt-get update && sudo apt-get install libxcb-render-util0 libxcb-image0 libxcb-icccm4 libxcb-randr0 libxcb-keysyms1

if [ $MACHARCH == 'x86_64' ]; then
	ln -s /usr/lib/x86_64-linux-gnu/libxcb-sync.so.1 /usr/lib/libxcb-sync.so.0
else
	ln -s /usr/lib/i386-linux-gnu/libxcb-sync.so.1 /usr/lib/libxcb-sync.so.0
fi

echo "Almost done, unpacking the files now"
echo ""
echo ""

cd ~/Downloads/demonsaw
if [ $MACHARCH == 'x86_64' ]; then
	unzip demonsaw_linux64.zip
else
	unzip demonsaw_linux32.zip
fi
chmod +x demonsaw

echo "Now you can run demonsaw by typing ./demonsaw, Happy Sharing =)"
