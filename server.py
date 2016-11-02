import time
from tfic import run_inference_on_image
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/tfic", methods=['GET'])
def tfic():
	stime = time.time()
	url = request.args['url']
	# run inference
	results = run_inference_on_image(url)
	etime = time.time()	
	return jsonify({
		'elapsed':etime-stime,
		'tfic_results':results
	})

if __name__ == "__main__":
	app.run()
