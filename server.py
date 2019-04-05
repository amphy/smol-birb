from flask import Flask
import cassiopeia as cass
import os

app = Flask(__name__)

@app.route('/')
def display_build():
	# Get summoner
	# Get Match
	# Get items for champion from Match
	# display items and champion picture on page

    return 'Hello, World!'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)