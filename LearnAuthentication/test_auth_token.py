import requests
class TestTokenAuth:
    def setup_class(self):
        self.proxy = {
            "http": "127.0.0.1:8000",
            "https": "127.0.0.1:8000",
        }

    def test_token(self):
        data = {
            "username": "admin123",
            "password": "admin123",
            "code": ""}
        url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
        res = requests.post(url=url, json=data)
        print(res.json())
        self.token = res.json()["data"]["token"]
        headers = {"X-Litemall-Admin-Token": self.token}
        goods_data = {"name": "hogwarts", "order": "desc", "sort": "add_time"}
        r = requests.get("http://litemall.hogwarts.ceshiren.com/admin/goods/list", params=goods_data,
                         headers={"X-Litemall-Admin-Token": self.token})
        print(r.json())
