from unittest import TestCase
from LearnEncryPtion.test_request import ApiRequest


class TestApiRequest(TestCase):
    req_data = {
        "url": "http://localhost:9999/demo/demo.txt",
        "method": "get",
        "headers": None,
        "encoding": "base64"
    }

    def test_get_data(self):
        ar = ApiRequest().get_data(self.req_data)
        print(ar)
