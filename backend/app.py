from flask import Flask, request, jsonify, redirect
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

import RandomWalks as ranWal
import LatticePresets as latP
import json

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/generateRandomWalk", methods=["POST"])
@cross_origin()
def generateRandomWalk():
    request_data = request.get_json()
    shape = request_data["shape"]
    size = request_data["size"]

    shapeToLattice = {
        "2S": ranWal.Lattice(latP.lat2DAdj),
        "2T": ranWal.Lattice(latP.triGridAdj),
        "2H": ranWal.Lattice(latP.hexGridAdj)
    }

    walk = ranWal.RandWalk(shapeToLattice[shape],size)

    response = {
        "walk": walk.runNumInt
    }
    return json.dumps(response)

if __name__ == '__main__':
    app.run()