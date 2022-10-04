import json
import jsonschema
from jsonschema import validate,Draft202012Validator

def load_json(path, **rest):
    with open(path, "r") as f:
        loaded = json.load(f, **rest)
    return loaded

def validate_json(json_data,schema_path):
    execute_api_schema = load_json(schema_path)
    v = Draft202012Validator(execute_api_schema)
    errors = sorted(v.iter_errors(json_data), key=lambda e: e.path)

    try:
        validate(instance=json_data, schema=execute_api_schema)

    except jsonschema.exceptions.ValidationError as err:
        for error in errors:
          print(error.message)
        err = "Given JSON data is Invalid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message

