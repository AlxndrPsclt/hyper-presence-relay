from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        print(data)

        with open("readings.jsonl", "a") as f:
            json.dump(data, f)
            f.write("\n")  # Newline-delimited JSON

        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
