import requests
import json
import pprint
import pytest
import os
from datetime import datetime

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(THIS_FOLDER, 'config.json')


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_FILE) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def api_url(config):
  return config['api_url']

@pytest.fixture(scope='session')
def auth(config):
  return config['authorization']



#@pytest.mark.skip(reason="test is done, but not relevant during other development")
def test_TC02_post(api_url, auth):


    # current date and time

    NAME_SUFFIX = datetime.now().microsecond.__str__()


    #Additional headers.
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth.__str__()
    }

    # Body
    payload = {
                "test": [
                          {
                            "Name": "CSAS" + NAME_SUFFIX,
                            "ID": "sdfg",
                            "Test": "sdf",
                            "Adress": "asdfgh"
                          }
                        ]
    }

    # convert dict to json by json.dumps() for body data.
    response = requests.request("POST", api_url + 'api/endpoint', headers=headers, json = payload)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()

    # print full response
    #pprint.pprint(response.json())

    # assert set(['Check', 'Results']).issubset(set(list))