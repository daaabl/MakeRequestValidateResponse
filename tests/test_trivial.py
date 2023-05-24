from config import URL
import requests
from messages import Error_Messages
from schema import response_schema
from jsonschema import validate
from SchemaClass import Response_Schema
from config import wanted_status

def test_status_code(make_request):
    if isinstance(wanted_status, tuple):
        assert make_request.status_code in wanted_status, Error_Messages.WRONG_STATUS
    else:
        assert make_request.status_code == wanted_status, Error_Messages.WRONG_STATUS

# testing using json schema
def test_responce_schema(make_request):
    received_message = make_request.json()
    for item in received_message:
        validate(item, response_schema)

# testing using pydentic
def test_responce_structure(make_request):
    received_message = make_request.json()
    for item in received_message:
        Response_Schema.parse_obj(item)