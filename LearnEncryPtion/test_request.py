import requests
import base64
import json

class ApiRequest:

    def get_data(self, data: dict):
        res = requests.request(method=data["method"], url=data["url"])
        if data["encoding"] == "base64":
            r = json.loads(base64.b64decode(res.content))
            return r

