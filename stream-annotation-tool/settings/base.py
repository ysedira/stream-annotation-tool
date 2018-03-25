SCHEMA = {
    "resources": [
        {
            "label": "Stream",
            "type": "vocals:Stream",
            "predicates": [{
                "predicate": "dc:subject",
                "required": True
            },
                {
                    "predicate": "dct:title",
                    "required": True
                },
                {
                    "predicate": "dct:description",
                    "required": False
                },
                {
                    "predicate": "dct:issued",
                    "required": False
                },
                {
                    "predicate": "dct:modified",
                    "required": False
                },
                {
                    "predicate": "dct:language",
                    "required": False
                },
                {
                    "predicate": "dct:publisher",
                    "required": False
                },
                {
                    "predicate": "dct:accrualPeriodicity",
                    "required": False
                },
                {
                    "predicate": "dct:identifier",
                    "required": False
                },
                {
                    "predicate": "dct:spatial",
                    "required": False
                },
                {
                    "predicate": "dct:temporal",
                    "required": False
                },
                {
                    "predicate": "dcat:theme",
                    "required": False
                },
                {
                    "predicate": "dcat:keyword",
                    "required": False
                },
                {
                    "predicate": "dcat:contactPoint",
                    "required": False
                },
                {
                    "predicate": "dcat:landingPage",
                    "required": False
                },
                {
                    "predicate": "vocals:hasEndpoint",
                    "required": False
                },
                {
                    "predicate": "vocals:hasPartition",
                    "required": False
                },
            ]
        },
        {
            "label": "StreamingService",
            "type": "vocals-sd:StreamingService",
            "predicates": [{
                "predicate": "dc:subject",
                "required": True
            },
                {
                    "predicate": "dc:title",
                    "required": True
                },
                {
                    "predicate": "dc:description",
                    "required": False
                },
                {
                    "predicate": "vocals-sd:hasFeature",
                    "required": True
                },
                {
                    "predicate": "vocals-sd:registerdTask",
                    "required": True
                },
                {
                    "predicate": "vocals-sd:registeredStreams",
                    "required": True
                },
                {
                    "predicate": "vocals-sd:availableGraph",
                    "required": False
                },
                {
                    "predicate": "vocals-sd:availableStream",
                    "required": False
                },
                {
                    "predicate": "vocals-sd:defaultGraph",
                    "required": False
                },
                {
                    "predicate": "vocals-sd:defaultStreamingDataset",
                    "required": False
                },
                {
                    "predicate": "vocals-sd:graph",
                    "required": False
                },
                {
                    "predicate": "vocals-sd:resultFormat",
                    "required": False
                }
            ]
        }
    ]

}
