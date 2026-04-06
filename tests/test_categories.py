from utils.api_client import get
from utils.assertions import validate_status


def test_get_categories():
    response = get("/products/categories")
    validate_status(response)


def test_products_by_category():
    category = "electronics"
    response = get(f"/products/category/{category}")

    validate_status(response)

    if response.status_code == 200:
        for product in response.json():
            assert product["category"] == category