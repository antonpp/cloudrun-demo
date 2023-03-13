import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    address = request.args.get('address', 'not_provided')
    return "Getting smart contract for {}!".format(address)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))