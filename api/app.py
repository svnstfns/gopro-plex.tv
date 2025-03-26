from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GOPRO_IP = os.getenv("GOPRO_IP")
RTMP_URL = os.getenv("RTMP_URL")
M3U_PATH = os.getenv("M3U_PATH")
EPG_PATH = os.getenv("EPG_PATH")

@app.route('/api/set_stream', methods=['POST'])
def set_stream():
    r = requests.get(f"http://{GOPRO_IP}/gp/gpControl/execute?p1=gpStream&a1=proto_v2&c1=start")
    return jsonify({"status": "stream_start_sent", "response": r.text})

@app.route('/api/configure_rtmp', methods=['POST'])
def configure_rtmp():
    payload = {"stream_url": RTMP_URL}
    r = requests.get(f"http://{GOPRO_IP}/gp/gpControl/command/live/set_transmit?transmit=rtmp&url={RTMP_URL}")
    return jsonify({"status": "rtmp_configured", "response": r.text})

@app.route('/m3u')
def get_m3u():
    return app.send_static_file("gopro.m3u")

@app.route('/epg.xml')
def get_epg():
    return app.send_static_file("epg.xml")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
