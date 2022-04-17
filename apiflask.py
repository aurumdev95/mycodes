from flask import *
import json, time 

app = Flask(__name__)

@app.route("/", methods=["GET"])

def home():
	data_set = {"page": "home", "message": "success", "timestamp": time.time()}
	json_data = json.dumps(data_set)
	
	return json_data
	
	
if __name__ == "__main__":
	app.run(port=5000)