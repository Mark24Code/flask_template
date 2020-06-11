from flask import jsonify
from . import api

@api.route('/sample', methods=['GET', 'POST'])
def sample():
    return jsonify({
        "code": 200,
        "data": "successful api"
    })