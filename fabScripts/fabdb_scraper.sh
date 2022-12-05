#!/bin/bash
#for i in {0..255};do if $i > 10 then j = 00$i elif $i > 100 then j = 0$i else j = $i fi curl https://api.fabdb.net/cards/WTR$j | jq -r ".image"; sleep 2; done
#This Script was created to grab a copy of all the cards in the fabdb database for having a local copy of the cards/ images/ etc
#Written by Ace Xor to teach festthebest some simple bash scraping
#$v0.3
#Added new sets to script

WTR=225
ARC=218
CRU=197
MON=306
ELE=237
EVR=197
UPR=225
DYN=246

declare -A setsDict
setsDict["WTR"]=$WTR
setsDict["ARC"]=$ARC
setsDict["CRU"]=$CRU
setsDict["MON"]=$MON
setsDict["ELE"]=$ELE
setsDict["EVR"]=$EVR
setsDict["UPR"]=$UPR
setsDict["DYN"]=$DYN

rm fulldb.json
for i in ${!setsDict[@]};
do
	for (( j=0; j<=${setsDict[$i]}; j++ ));
	do
		echo "${i} ${j}";
		echo "";
		if [[ $j -lt 10 ]]; then
			curl https://api.fabdb.net/cards/${i}00${j} | jq -r >> fulldb.json
		elif [[ $j -lt 100 ]]; then
			curl https://api.fabdb.net/cards/${i}0${j} | jq -r >> fulldb.json
		else
			curl https://api.fabdb.net/cards/${i}${j} | jq -r >> fulldb.json
		fi
		sleep 1.5;
	done
done
