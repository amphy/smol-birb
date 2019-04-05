import os

from flask import Flask

import cassiopeia as cass
from cassiopeia import Summoner, Match
from cassiopeia.data import Season, Queue

app = Flask(__name__)

@app.route('/')
def display_build():
	# Get summoner
	summoner = Summoner(name="Olysia", region="NA")
	# Get Match
	match_history = summoner.match_history

	# Get items for champion from Match
	# display items and champion picture on page

    return match_history

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)