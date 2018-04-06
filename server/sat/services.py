def get_resource(_schema, resource_type):
    resource = next(filter(lambda res: res["type"] == resource_type, _schema["resources"]))
    return dict(resource)


def get_resources(_schema):
    print(len(_schema))
    return list(map(lambda res: {"type": res["type"], "label": res["label"] or None}, _schema["resources"]))


def get_ontology(resource, frmt):
    content = ["{0} {1} {2}".format(resource["subject"], "rdf:type", resource["type"]).strip()]
    for pred in resource["predicates"]:
        content.append("{0} {1} {2}".format(resource["subject"], pred["predicate"], pred["object"]).strip())
    return ";\n".join(content) + "."
