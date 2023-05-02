import allure

from src.ayan_api.core_api import Test_admin_product_controller as Test_Produts

def test_admin_product():
    """
    1. Create product
    2. Check creat product
    3. Check product with barcode: 300702
    4. Delete created product
    """

    with allure.step("1. Create product"):
        Test_Produts.test_admin_product_json_add
    with allure.step("2. Check creat product"):
        Test_Produts.test_admin_product_id
    with allure.step("3. Check product with barcode: 300702"):
        Test_Produts.test_admin_product_find_byBarcode_barcode
    with allure.step("4. Delete created product"):
        Test_Produts.test_admin_product_delete
