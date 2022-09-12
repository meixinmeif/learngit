import requests
import yaml
import os
class TestSwithEvn:
    def setup_class(self):
        env_host = os.getenv("interface_env")
        print(env_host)
        re_data = yaml.safe_load(open(f'{env_host}.yaml', encoding='utf-8'))
        print(re_data)
        self.base_url = re_data['url']

    def test_test_evn(self):
        path = '/get'
        res = requests.get(self.base_url + path)
        assert res.json()['headers']['Host'] == 'httpbin.ceshiren.com'

    def test_dev_evn(self):
        path = '/get'
        res = requests.get(self.base_url + path)
        assert res.json()['headers']['Host'] == 'httpbin.org'







