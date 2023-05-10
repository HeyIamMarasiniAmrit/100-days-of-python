import json
import requests
import sys
if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://music.apple.com/us/playlist/new-music-daily/pl.2b0e6e332fdf4b7a91164da3162127b5" + sys.argv)

o = response.json()
for result in o["results"]:
    print(result["trackName"])