from flask import request, Flask, jsonify

app = Flask(__name__) 

@app.route('/', methods=['POST'])
def index():
	data = request.get_json()
	message = data['message']
	return jsonify({
		'message' : message
	})


if __name__ == '__main__':
    app.run(debug=True)