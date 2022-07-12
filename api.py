import os

import flask
import numpy as np
import json


from flask import request, send_from_directory

from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})
app.config["DEBUG"] = True



class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


@app.route('/grid/test', methods=['GET'])
def test() -> str:
    return "hello world"


@app.route('/')
def index() -> str:
    return 'INDEX => Hello World'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
