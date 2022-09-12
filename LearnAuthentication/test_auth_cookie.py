import requests
class TestAuth:
    def test_auth(self):
        #Session类被赋予成一个实例，这个对象在获取一次cookie之后，下一次请求都会带上cookie
        req = requests.Session()
        r1 = req.get("https://httpbin.testing-studio.com/cookies/set/username/huangjiajia")
        r2 = req.get("https://httpbin.testing-studio.com/cookies")
        print(r1.json(), r2.json())