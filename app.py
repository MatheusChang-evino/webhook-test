from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'



@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    print(data)
    # Do something with the webhook data
    return 'OK'
