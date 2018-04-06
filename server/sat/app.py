from flask import Flask, request, jsonify, g, send_from_directory, send_file
from flask_cors import CORS
from werkzeug.routing import BaseConverter

import helpers.config as cnf
import helpers.services as srv

app = Flask(__name__)  # create the application instance :)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.before_first_request
def get_schema():
    rc = getattr(g, '_schema', None)
    if rc is None:
        rc = g._schema = cnf.SCHEMA
    return rc


@app.route("/")
@app.route("/static/resources/")
@app.route("/static/resources")
def index():
    return send_file("static/index.html")


@app.route("/<regex('\w\.(js|css)'):path>")
def assets(path):
    return send_from_directory("static", path)


@app.route("/api/resources", methods=["GET"])
def resource():
    _schema = get_schema()
    response = srv.get_resources(_schema)
    return jsonify(response)


@app.route("/api/resources/<resource_type>", methods=["GET"])
def resource_details(resource_type):
    _schema = get_schema()
    resource = srv.get_resource(_schema, resource_type)
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
    response = {"content": srv.get_ontology(_schema, resource, frmt=out_format)}

    return jsonify(response)


if __name__ == "__main__":
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.run(debug=True, use_reloader=True)
