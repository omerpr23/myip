from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from IpService import IpService
import logging
import os
load_dotenv()

# instantiate the app
app = Flask(__name__, static_folder='../client/dist/', static_url_path='/')
CORS(app, resources={r'/*': {'origins': '*'}})
ips = IpService()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/ip', methods=['GET'])
def get_ip():
    logging.info("About to process GET API request...")
    return ips.get_ip()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)