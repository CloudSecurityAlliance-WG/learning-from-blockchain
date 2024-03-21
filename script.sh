#!/bin/bash

sed 's/^/\/home\/kurt\/GitHub\/AI-Prompting\/utilities\/content_downloader\/content_downloader.py --url="/' urls.txt  | sed 's/$/"/' > script
sh ./script
rm script
/home/kurt/GitHub/AI-Prompting/utilities/content_downloader/sha256.sh urls.txt

