from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    # Do something with the webhook data
    return 'OK'