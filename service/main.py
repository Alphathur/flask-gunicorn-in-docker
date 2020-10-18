import decimal
import logging
from logging.handlers import RotatingFileHandler

import flask.json
from flask import Flask, jsonify, request

from common.utils import error_response
from service import data_student


class MyJSONEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(MyJSONEncoder, self).default(obj)


config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "filesystem",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 0,
    "CACHE_DIR": './api_caching'
}
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
app.json_encoder = MyJSONEncoder
app.config['JSON_AS_SCII'] = False


@app.route("/students", methods=["GET"])
def list_student():
    app.logger.info(request)
    res = data_student.list_students()
    return jsonify(res)


@app.route("/students/<id>", methods=["GET"])
def get_student_by_id(id):
    app.logger.info(request)
    if not id:
        return jsonify(error_response(50001))
    res = data_student.get_student(id)
    return jsonify(res)


@app.route("/students/<id>", methods=["DELETE"])
def delete_student_by_id(id):
    app.logger.info(request)
    if not id:
        return jsonify(error_response(50001))
    data_student.delete_student(id)
    return "DELETED"


@app.route("/students", methods=["POST"])
def save_student():
    app.logger.info(request)
    if not request.data:
        return jsonify(error_response(50001))
    res = data_student.save_student(request.get_json(force=True))
    return jsonify(res)


def main():
    log_filename = './server.log'
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler(log_filename, maxBytes=10000000, backupCount=5)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='0.0.0.0', port=8000)


if __name__ == "__main__":
    main()
