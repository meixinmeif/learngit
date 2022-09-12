import requests
from requests.auth import HTTPBasicAuth


class TestTokenAuth:
    def setup_class(self):
        self.proxy = {
            "http": "127.0.0.1:8000",
            "https": "127.0.0.1:8000",
        }

    def test_token(self):
        r = requests.get("https://httpbin.ceshiren.com/basic-auth/username/password", auth=HTTPBasicAuth("username", "password"))
        print(r.json())
