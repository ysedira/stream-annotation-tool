class ResourceController:
    def __init__(self, schema):
        print "Resource controller: Schema Initialized!"
        self._schema = schema

    def get_resource(self, resource_type):
        return filter(lambda res: res["type"] == resource_type, self._schema["resources"])[0]

    def get_resources(self):
        return map(lambda res: {"type": res["type"], "label": res["label"] or None}, self._schema["resources"])


class OntologyController:
    def __init__(self):
        pass

    @classmethod
    def get_ontology(cls, resource, frmt):
        content = ["{0} {1} {2}".format(resource["subject"], "rdf:type", resource["type"]).strip()]
        for pred in resource["predicates"]:
            content.append("{0} {1} {2}".format(resource["subject"], pred["predicate"], pred["object"]).strip())
        return ";\n".join(content) + "."
