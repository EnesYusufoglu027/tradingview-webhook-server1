from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook Server Aktif!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Gelen veri:", data)
    # Burada gelen sinyale göre işlem yapabilirsin (örn: bir dosyaya kaydetmek, cTrader'a iletmek vs.)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
