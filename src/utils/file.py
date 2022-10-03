import json
import jsonschema
from jsonschema import validate

def load_json(path, **rest):
    with open(path, "r") as f:
        loaded = json.load(f, **rest)
    return loaded

def load_schema(path,**rest):
    with open(path, 'r') as f:
        schema = json.load(f,**rest)
    return schema


def validate_json(json_data,schema_path):
    execute_api_schema = load_schema(schema_path)

    try:
        validate(instance=json_data, schema=execute_api_schema)

    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is Invalid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message
