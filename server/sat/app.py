from flask import Flask, request, jsonify, g, redirect, url_for
from flask_cors import CORS

from sat.config import SCHEMA
from sat.services import get_resource, get_resources, get_ontology

app = Flask(__name__)  # create the application instance :)


@app.before_first_request
def get_schema():
    rc = getattr(g, '_schema', None)
    if rc is None:
        rc = g._schema = SCHEMA
    return rc


@app.route("/api/resources", methods=["GET"])
def resource():
    _schema = get_schema()
    response = get_resources(_schema)
    return jsonify(response)


@app.route("/api/resources/<resource_type>", methods=["GET"])
def resource_details(resource_type):
    _schema = get_schema()
    resource = get_resource(_schema, resource_type)
    response = {}
    response["type"] = resource["type"]
    response["requiredPredicates"] = [res for res in filter(lambda res: res["required"], resource["predicates"])]
    response["optionalPredicates"] = [res for res in filter(lambda res: not res["required"], resource["predicates"])]
    return jsonify(response)


@app.route("/api/resources", methods=["POST"])
def _resource():
    _schema = get_schema()
    out_format = request.args.get("format")
    if not out_format:
        out_format = "JSON_LD"
    request_resource = request.get_json()
    predicates = []
    predicates.extend(request_resource["optionalPredicates"])
    predicates.extend(request_resource["requiredPredicates"])
    resource = {
        "subject": request_resource["subject"],
        "type": request_resource["type"],
        "predicates": predicates
    }
    response = {"content": get_ontology(_schema, resource, frmt=out_format)}

    return jsonify(response)


if __name__ == "__main__":
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.run(debug=True, use_reloader=True)
