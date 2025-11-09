from flask import Flask, jsonify
import logging
import time

app = Flask(__name__)

start_time = time.time()
request_count = 0

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


@app.route('/')
def home():
    global request_count
    request_count += 1
    app.logger.info("Received request to '/' (Service work)")
    return "Сервіс працює", 200


@app.route('/error')
def error():
    try:
        1 / 0
    except Exception as e:
        app.logger.exception("Exception thrown on /error")
    return "Виникла помилка (дивись app.log)", 500


@app.route('/status')
def status():
    uptime = time.time() - start_time
    app.logger.info("Received request to /status")
    return jsonify({
        "uptime_seconds": round(uptime, 2),
        "total_requests": request_count
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
