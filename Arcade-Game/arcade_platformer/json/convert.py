import json
from select import select

f = open ('player.json')

data = json.load (f)

f.close

p = data['players']

selected_player = data['selectedPlayer']

if data["selectedPlayer"] == selected_player:
        player_source = (p[selected_player]["Imgpath"])

print (player_source)