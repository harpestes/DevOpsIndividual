from flask import Flask, jsonify
import logging
import time
import socket

app = Flask(__name__)

start_time = time.time()
request_count = 0

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

UPD_SERVER_IP = "127.0.0.1"
UPD_SERVER_PORT = 9999


def send_to_upd_server(message: str):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode("utf-8"), (UPD_SERVER_IP, UPD_SERVER_PORT))
        sock.close()
    except Exception as e:
        app.logger.warning(f"An error occurred during sending to UPD server: {e}")


@app.route('/')
def home():
    global request_count
    request_count += 1
    app.logger.info("Received request to '/' (Service work)")
    return "Сервіс працює", 200


@app.route('/error')
def error():
    global request_count
    request_count += 1
    try:
        1 / 0
    except Exception as e:
        app.logger.exception("Exception thrown on /error")
        send_to_upd_server(f"ERROR: {e}")
        return "Виникла помилка (дивись app.log)", 500


@app.route('/status')
def status():
    global request_count
    request_count += 1
    uptime = time.time() - start_time
    app.logger.info("Received request to /status")
    return jsonify({
        "uptime_seconds": round(uptime, 2),
        "total_requests": request_count
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
