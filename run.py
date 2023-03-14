import os
import json
import urllib.request

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    address = request.args.get('address', 'not_provided')
    return "The demo runs too long...Getting smart contract for {}!".format(address)

@app.route("/getsource")
def get_source():
    address = request.args.get('address', 'not_provided')
    url = "https://api.etherscan.io/api?module=contract&action=getsourcecode&address={ADDR}&apikey={KEY}".format(**{
        'ADDR': address,
        'KEY': os.environ['ETHERSCAN_KEY']
    })
    f = urllib.request.urlopen(url)
    data = json.loads(f.read())
    return data['result'][0]['SourceCode']


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))