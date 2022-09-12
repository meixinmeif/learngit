

import pytest
import requests
import logging
class TestLitemal:
    def setup_class(self):
        #===登陆操作
        data = {
            "username": "admin123",
            "password": "admin123",
            "code": ""}
        url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
        res = requests.post(url=url, json=data)
        self.token = res.json()["data"]["token"]
        json = {
            "username": "user123",
            "password": "user123"}
        json_url = "https://litemall.hogwarts.ceshiren.com/wx/auth/login"
        res = requests.post(url=json_url, json=json)
        self.Litemall_token = res.json()["data"]["token"]

    def teardown(self):
        #====删除操作，完成闭环
        url = "https://litemall.hogwarts.ceshiren.com/admin/goods/delete"
        r = requests.post(url=url, json={"id": self.goodid}, headers={"X-Litemall-Admin-Token": self.token})
        print(r.json())


    #====实现参数化
    @pytest.mark.parametrize("good_name", ["验证一下", "验证两下"])
    #====上架商品
    def test_add_goods(self, good_name):
        data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "9098", "name": good_name, "counterPrice": "20000"},
            "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price":"20", "number":"1000", "url":""}],
            "attributes": []
        }
        headers = {
            "X-Litemall-Admin-Token": self.token
        }
        requests.post("https://litemall.hogwarts.ceshiren.com/admin/goods/create", json=data, headers=headers)

        #====获取商品ID
        goods_list_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
        goods_data = {
            "page": "1",
            "limit": "20",
            "order": "desc",
            "sort": "add_time"
        }
        res = requests.get(goods_list_url, params=goods_data, headers=headers)
        self.goodid = res.json()["data"]["list"][0]["id"]
        #====获取产品ID
        pro_data = {
            "id": self.goodid
        }
        pro_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/detail"
        res = requests.get(url=pro_url, params=pro_data, headers=headers)
        groid = res.json()["data"]["products"][0]["id"]
        #====加入购物车
        cart_data = {"goodsId": self.goodid,
                "number": 1,
                "productId": groid
                }
        cart_url = "https://litemall.hogwarts.ceshiren.com/wx/cart/add"
        cart_headers = {
            "X-Litemall-Token": self.Litemall_token
        }
        res = requests.post(url=cart_url, json=cart_data, headers=cart_headers)
        print(res.json())



