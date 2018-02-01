from enum import Enum
import base64
import hashlib
import hmac
import json
import time
import requests
from .params import V1, V2, ACCESS_TOKEN, SECRET_KEY, NONCE


class BaseClient:
    def __init__(self):
        self.uri = 'https://api.coinone.co.kr/'

SECRET_FILE = 'secret.json'
class V1Client(BaseClient):
    def __init__(self, secret_file=SECRET_FILE):
        super().__init__()
        self.uri += 'v1/'
        secret = _get_secret(secret_file)
        self.access_token = secret[V1][ACCESS_TOKEN]

class V2Client(BaseClient):
    def __init__(self, secret_file=SECRET_FILE):
        super().__init__()
        self.uri += 'v2/'
        secret = _get_secret(secret_file)
        self.access_token = secret[V2][ACCESS_TOKEN]
        self.secret_key = secret[V2][SECRET_KEY]


def public_get(path):
    def _public_get_decorator(func):
        def _public_get_wrapper(self, *args, **kwargs):
            uri = self.uri + path.value
            params = _kwargs_2_params(kwargs)
            return _public_get(uri=uri, params=params)
        return _public_get_wrapper
    return _public_get_decorator

def v1_get(path):
    def _v1_get_decorator(func):
        def _v1_get_wrapper(self, *args, **kwargs):
            uri = self.uri + path.value
            params = _kwargs_2_params(kwargs)
            params[ACCESS_TOKEN] = self.access_token
            return _public_get(uri=uri, params=params)
        return _v1_get_wrapper
    return _v1_get_decorator

def v1_post(path):
    def _v1_post_decorator(func):
        def _v1_post_wrapper(self, *args, **kwargs):
            uri = self.uri + path.value
            params = _kwargs_2_params(kwargs)
            params[ACCESS_TOKEN] = self.access_token
            return _v1_post(uri=uri, params=params)
        return _v1_post_wrapper
    return _v1_post_decorator

def v2_post(path):
    def _v2_post_decorator(func):
        def _v2_post_wrapper(self, *args, **kwargs):
            uri = self.uri + path.value
            params = _kwargs_2_params(kwargs)
            params[ACCESS_TOKEN] = self.access_token
            return _v2_post(uri=uri, params=params, secret_key=self.secret_key)
        return _v2_post_wrapper
    return _v2_post_decorator


def _kwargs_2_params(kwargs):
    params = {}
    for key in kwargs:
        value = kwargs[key]
        params[key] = value.value if isinstance(value, Enum) else value
    return params

def _get_secret(secret_file):
    with open(secret_file) as fp:
        return json.load(fp)

def _public_get(uri, params):
    return requests.get(uri, params=params).json()

def _v1_post(uri, params):
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json'
    }
    return requests.post(uri, headers=headers, params=params).json()

def _v2_post(uri, params, secret_key):
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
