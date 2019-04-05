import os

from flask import Flask

import cassiopeia as cass
from cassiopeia import Summoner, Match
from cassiopeia.data import Season, Queue

app = Flask(__name__)

@app.route('/')
def display_build():
	region = "NA"
	summoner_name = "Olysia"

	cass.set_riot_api_key(os.environ.get("RIOTAPI_KEY", "None"))

	champion_id_to_name_mapping = {champion.id: champion.name for champion in cass.get_champions(region=region)}

	# Get summoner
	summoner = Summoner(name=summoner_name, region=region)
	# Get Match
	match_history = summoner.match_history
	match = match_history[0]
	# Get items for champion from Match
	champion_id = match.participants[summoner.name].champion.champion.id
	champion_name = champion_id_to_name_mapping[champion_id]

	# display items and champion picture on page

    return match_history

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)