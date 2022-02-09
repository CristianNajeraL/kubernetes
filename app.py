import time
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
    return jsonify({'What time is it? It is ': time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
