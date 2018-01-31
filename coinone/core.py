from enum import Enum
import base64
import hashlib
import hmac
import json
import time
import requests
from coinone.params import ACCESS_TOKEN, SECRET_KEY, NONCE


class BaseClient:
    def __init__(self):
        self.uri = 'https://api.coinone.co.kr/'

SECRET_FILE = 'secret.json'
class V2Client(BaseClient):
    def __init__(self, secret_file=SECRET_FILE):
        super().__init__()
        self.uri += 'v2/'
        secret = _get_secret(secret_file)
        self.access_token = secret[ACCESS_TOKEN]
        self.secret_key = secret[SECRET_KEY]


def public_request(path):
    def _public_request_decorator(func):
        def _public_request_wrapper(self, *args, **kwargs):
            uri = self.uri + path.value
            params = _kwargs_2_params(kwargs)
            return _get_public_response(uri=uri, params=params)
        return _public_request_wrapper
    return _public_request_decorator

def v2_request(path):
    def _v2_request_decorator(func):
        def _v2_request_wrapper(self, *args, **kwargs):
            uri = self.uri + path.value
            params = _kwargs_2_params(kwargs)
            params[ACCESS_TOKEN] = self.access_token
            return _get_v2_response(uri=uri, params=params, secret_key=self.secret_key)
        return _v2_request_wrapper
    return _v2_request_decorator


def _kwargs_2_params(kwargs):
    params = {}
    for key in kwargs:
        value = kwargs[key]
        params[key] = value.value if isinstance(value, Enum) else value
    return params

def _get_secret(secret_file):
    with open(secret_file) as fp:
        return json.load(fp)

def _get_public_response(uri, params):
    return requests.get(uri, params=params).json()

def _get_v2_response(uri, params, secret_key):
    encoded_payload = _get_encoded_payload(params)
    signature = _get_signature(encoded_payload, secret_key)
    headers = {
        'Content-Type': 'application/json',
        'X-COINONE-PAYLOAD': encoded_payload,
        'X-COINONE-SIGNATURE': signature,
    }
    return requests.post(uri, data=encoded_payload, headers=headers).json()

def _get_encoded_payload(payload):
    payload[NONCE] = int(time.time()*1000)
    dumped_json = json.dumps(payload)
    encoded_json = base64.b64encode(_str_2_byte(dumped_json))
    return encoded_json

def _get_signature(encoded_payload, secret_key):
    signature = hmac.new(_str_2_byte(secret_key.upper()), encoded_payload, hashlib.sha512)
    return signature.hexdigest()

def _str_2_byte(string, encode='utf-8'):
    return bytes(string, encode)
