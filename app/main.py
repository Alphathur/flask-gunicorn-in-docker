import decimal

import flask.json
from flask import Flask, jsonify, request

from app.utils import error_response
from app import data_student


class MyJSONEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(MyJSONEncoder, self).default(obj)


app = Flask(__name__)
app.config['DEBUG'] = True
app.json_encoder = MyJSONEncoder
app.config['JSON_AS_SCII'] = False


@app.route("/", methods=["GET"])
def hi():
    return "Hello World"


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
    app.run(host='0.0.0.0', port=8000)


if __name__ == "__main__":
    main()
