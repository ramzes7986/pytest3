import requests
import logging

from src.pydantic_schemas.validation_admin_product_json_add import Base
from baseclasses.Respone_validate import Response
from src.enums.global_enums import global_url
from logs.logging import logger


class Test_admin_product_controller:

    def test_admin_product_json_add(self, test_authorization):
        url = global_url + "/api/admin/product/json/add"
        headers = {"Content-Type": "application/json", "token": f'{test_authorization}'}
        filename = "../data.json"

        with open(filename, "rb") as f:
            try:
                r = requests.post(url, data=f.read(), headers=headers)
                message = r.json()
                res = Response(r)
                assert res.validate(Base)
                assert message.status_code == 200
            except requests.exceptions.RequestException:
                logger.critical(f'Продукт не создан; {requests.exceptions.RequestException}')

    def test_admin_product_id(self, test_authorization):
        headers = {"Content-Type": "application/json", "token": f'{test_authorization}'}
        id = "300702"
        url = global_url + "/api/admin/product/" + id

        try:
            req = requests.get(url=url, headers=headers)
            message = req.json()
            print(req.json())
            assert message["data"]["name"] == "testing_product_7"
            assert message["data"]["categoryIds"][0] == 30
            assert message["data"]["skuPriceDtoList"][0]["price"] == 300
            assert message.status_code == 200
        except requests.exceptions.RequestException:
                logger.critical(f'Продукт не получен; {requests.exceptions.RequestException}')

    def test_admin_product_find_byBarcode_barcode(self, test_authorization):
        barcode = '2809699'
        url = global_url + "/api/admin/product/find/byBarcode/" + barcode
        headers = {"Content-Type": "application/json", "token": f'{test_authorization}'}

        try:
            r = requests.post(url=url, headers=headers)
            message = r.json()
            print(message)
            assert message['data']['id'] == 108800
            assert message.status_code == 200
        except requests.exceptions.RequestException:
            logger.critical(f'Продукт с штрих-кодом 2809699 не получен; {requests.exceptions.RequestException}')

    def test_admin_product_delete(self, test_authorization):
        url = global_url + "/api/admin/product/product/delete"
        headers = {"Content-Type": "application/json", "token": f'{test_authorization}'}
        json = {"deleteReason": "test", "productId": 300704}

        try:
            r = requests.post(url=url, json=json, headers=headers)
            message = r.json()
            assert message['data']['id'] == 108800
            assert message.status_code == 200
        except requests.exceptions.RequestException:
            logger.critical(f'Продукт не удален; {requests.exceptions.RequestException}')
