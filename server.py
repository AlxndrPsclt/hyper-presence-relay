from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        print(data)
        mac_address = data.get("mac_address")
        rssi = data.get("rssi")
        scanner_id = data.get("scanner_id")

        print(f"Received from {scanner_id}: {mac_address} -> RSSI {rssi}")
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
