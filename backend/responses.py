from flask import jsonify
from errors import ERRORS

def success(data=None, message="ok", status=200):
    res = {"status": "success", "message": message}
    if data is not None:
        res["data"] = data
    return jsonify(res), status

def error(key, details=None):
    message, status = ERRORS.get(key, ERRORS["SERVER_ERROR"])
    res = {"status": "error", "code": key, "message": message}
    if details:
        res["details"] = str(details)
    return jsonify(res), status

