import logging
from flask import Flask, jsonify


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
    return jsonify({'statusCode': 200})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1234)
