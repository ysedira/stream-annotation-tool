from flask import Flask, request, jsonify, Response, g

from flask_cors import CORS

from settings.base import SCHEMA
from vocals.controllers import ResourceController, OntologyController

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , api.py
app.config.from_envvar('STREAM_ANNOTATION_TOOL_SETTINGS', silent=True)
app.config["DEBUG"] = True
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.before_first_request
def init_controller():
    rc = getattr(g, '_resource_controller', None)
    if rc is None:
        rc = g._resource_controller = ResourceController(schema=SCHEMA)


def get_resource_controller():
    rc = getattr(g, '_resource_controller', None)
    if rc is None:
        rc = g._resource_controller = ResourceController(schema=SCHEMA)
    return rc


@app.route("/api/resources", methods=["GET"])
def get_resource():
    controller = get_resource_controller()
    response = controller.get_resources()
    return jsonify(response)


@app.route("/api/resources/<resource_type>", methods=["GET"])
def get_resource_details(resource_type):
    controller = get_resource_controller()
    resource = controller.get_resource(resource_type)
    response = {}
    response["type"] = resource["type"]
    response["requiredPredicates"] = filter(
        lambda res: res["required"], resource["predicates"])
    response["optionalPredicates"] = filter(
        lambda res: not res["required"], resource["predicates"])
    return jsonify(response)


@app.route("/api/resources", methods=["POST"])
def post_resource():
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
    response = {"content": OntologyController.get_ontology(
        resource, frmt=out_format)}

    return jsonify(response)


if __name__ == "__main__":
    app.run()
