from flask import Flask, request
import time
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'



@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    print(data)
    time.sleep(10)
    print("Finished.")
    # Do something with the webhook data
    return  {
        "success": True,
        "payload": {'message' : 'success'}
        }
