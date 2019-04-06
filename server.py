import os

from flask import Flask, render_template, request

import cassiopeia as cass
from cassiopeia import Summoner, Match
from cassiopeia.data import Season, Queue

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/results', methods = ['GET'])
def results():
	region = "NA"
	try:
		summoner_name = str(request.args.getlist('search')[0])
	except:
		summoner_name = "Olysia"

	cass.set_riot_api_key(os.environ.get("RIOTAPI_KEY", "None"))

	champion_id_to_name_mapping = {champion.id: champion.name for champion in cass.get_champions(region=region)}

	# Get summoner
	summoner = Summoner(name=summoner_name, region=region)
	# Get Match
	match_history = summoner.match_history
	match = match_history[0]
	# Get items for champion from Match
	champion_id = match.participants[summoner.name].champion.id
	champ_img = match.participants[summoner.name].champion.image.url
	champion_name = champion_id_to_name_mapping[champion_id]
	items = match.participants[summoner.name].stats.items

	itemUrls = []
	for item in items:
		# We want to get picture
		if item is not None:
			print(item.name)
			itemUrl = item.image.url
			itemUrls.append(itemUrl)
		else:
			itemUrl = 'static/none.png'
			itemUrls.append(itemUrl)

	# display items and champion picture on page
	return render_template('results.html', url_champ = champ_img, champ_name = champion_name, url_img1 = itemUrls[0], url_img2 = itemUrls[1], url_img3 = itemUrls[2], url_img4 = itemUrls[3], url_img5 = itemUrls[4], url_img6 = itemUrls[5])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)