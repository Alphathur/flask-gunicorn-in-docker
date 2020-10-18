import decimal
import flask.json
import sys
from flask import Flask, jsonify, request

from pathlib import Path
# Of course, you can use `os` instead of `pathlib`, but `pathlib` is good ;)
sys.path.append(str(Path(__file__).resolve().parent.parent))  # add project root to path

import apps.data_student as ds
from apps.utils import error_response

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
    res = ds.list_students()
    return jsonify(res)


@app.route("/students/<id>", methods=["GET"])
def get_student_by_id(id):
    app.logger.info(request)
    if not id:
        return jsonify(error_response(50001))
    res = ds.get_student(id)
    return jsonify(res)


@app.route("/students/<id>", methods=["DELETE"])
def delete_student_by_id(id):
    app.logger.info(request)
    if not id:
        return jsonify(error_response(50001))
    ds.delete_student(id)
    return "DELETED"


@app.route("/students", methods=["POST"])
def save_student():
    app.logger.info(request)
    if not request.data:
        return jsonify(error_response(50001))
    res = ds.save_student(request.get_json(force=True))
    return jsonify(res)


def main():
    app.run(host='0.0.0.0', port=8000)


if __name__ == "__main__":
    main()
