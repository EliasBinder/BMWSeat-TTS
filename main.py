from flask import Flask, request

from aiRunner import say

app = Flask(__name__)


@app.route('/say', methods=['POST'])
def sayEndpoint():
    # Get text from request
    data = request.get_json()
    say(data['text'])
    return "{\"status\":\"OK\"}"


app.run(host='127.0.0.1', port=3002)
