#!/usr/bin/python3
"""Russell Zachary Feeser | Alta3 Research
   @rzfeeser              | https://alta3.com


"""

import uuid
import os
from time import sleep

from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)

## CRid Request /crid
@app.route("/crid")
def crid():
    return jsonify(uuid.uuid1())

## Alta3 Research - /alta3
@app.route("/alta3")
def alta3():
    alta = {}
    alta["version"] = "1"
    alta["thanks"] = "Thank you for training with Alta3 Research!"
    alta["alta3"] = {}
    alta["alta3"]["homepage"] = "https://alta3.com"
    alta["alta3"]["youtube"] = "https://www.youtube.com/user/Alta3Research/videos"
    alta["alta3"]["posters"] = "https://alta3.com/posters"
    return jsonify(alta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9876)
