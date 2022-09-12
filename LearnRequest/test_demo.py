import requests
from hamcrest import *
from jsonpath import jsonpath
class TestGet:
    def test_timeout(self):
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }
        # 添加参数verify为False，表明对这个请求设置代理不需要证书
        r = requests.post("https://httpbin.testing-studio.com/post", proxies=proxies, verify=False, timeout=3)
        print(r.json())

    def test_01(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.json())


    def test_file(self):
        files = {
            "huang": open('D:\\a.txt', 'rb')
        }
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", files=files, proxies=proxies, verify=False)
        print(r.json())

    def test_file2(self):
        files = {
            "huang": ('D:\\b.txt', open('D:\\a.txt', 'rb'))
        }
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", files=files, proxies=proxies, verify=False)
        print(r.json())


'''
    def test_02(self):
        params = {
            "name": "huangjiajia",
            "password": "HJJHJJzk1234"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=params)
        print(r.json())

    def test_03(self):
        params = {
            "name": "huangjiajia",
            "password": "HJJHJJzk1234"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=params)
        print(r.json())
    
    def test_04(self):
        file = {"file": open("D:\\a.txt", 'rb', encoding='utf-8')}
        r = requests.post("https://httpbin.testing-studio.com/post", files=file)
        print(file)
    

    def test_05(self):
        params = {
            "name": "huangjiajia",
            "password": "HJJHJJzk1234"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=params, headers={"huangjiajia": "hello"})
        print(r.json())
        assert r.status_code == 200
        assert r.json()["headers"]["Huangjiajia"] == "hello"

    def test_06(self):
        params = {
            "name": "huangjiajia",
            "password": "HJJHJJzk1234"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=params)
        print(r.json())

    def test_07(self):
        params = {
            "name": "huangjiajia",
            "password": "HJJHJJzk1234"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=params)
        print(r.json())
        assert_that(r.json()["origin"], equal_to('172.17.56.110'))

    def test_json_path(self):
        params = {
            "name": "huangjiajia",
            "password": "HJJHJJzk1234"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=params)
        print(r.json())
        assert jsonpath(r.json(), '$..name')[0] == 'huangjiajia'
    
    def test_proxies(self):
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }
        #添加参数verify为False，表明对这个请求设置代理不需要证书
        r = requests.post("https://httpbin.testing-studio.com/post", proxies=proxies, verify=False)
        print(r.json())
    

    def test_cookies(self):
        headers = {
            "Cookie": "huang=jia"
        }
        r = requests.get("https://httpbin.testing-studio.com/cookies", headers=headers)
        print(r.request.headers)

    def test_cookies(self):
        headers = {
            "User_Agent": "huangjia"
        }
        cookie = {
            "ZK": 'WJK'
        }
        r = requests.get("https://httpbin.testing-studio.com/cookies", headers=headers, cookies=cookie)
        print(r.request.headers)


    def test_from(self):
        data = {
            "name": "huangjiajia",
            "password": "HJJHJJzk1234"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=data)
        print(r.json())
        assert jsonpath(r.json(), '$..name')[0] == 'huangjiajia'
'''





