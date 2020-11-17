import requests
import json
import pprint
import pytest
import os

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
def test_get_config_values(api_url, auth):

    # Additional headers.
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth.__str__()
    }

    # Body
    payload = {}

    # convert dict to json by json.dumps() for body data.
    response = requests.request("GET", api_url+ 'config', headers=headers, data = payload)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body['sequences']['accession'] == 1
    assert resp_body['system']['login_valid_hours'] == 24

    # print full response
    pprint.pprint(response.json())