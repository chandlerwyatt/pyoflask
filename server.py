import json

from flask import Flask, request
import redis

with open('config.json', 'r') as fp:
    config = json.load(fp)

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/temp', methods=['POST'])
def temp():
    data = request.get_data(as_text=True)
    print(f"Got data : {data}")
    r.lpush('temp', data)
    return 'OK'
