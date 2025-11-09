from flask import Flask, jsonify
import time

app = Flask(__name__)

start_time = time.time()
request_count = 0


@app.before_request
def before_request():
    global request_count
    request_count += 1


@app.route('/')
def home():
    return "Сервіс працює", 200


@app.route('/error')
def error():
    return 1 / 0


@app.route('/status')
def status():
    uptime = time.time() - start_time
    return jsonify({
        "uptime_seconds": round(uptime, 2),
        "total_requests": request_count
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
