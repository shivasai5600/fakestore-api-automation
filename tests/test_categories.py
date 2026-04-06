from utils.api_client import get

def test_get_categories():
    response = get("/products/categories")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_products_by_category():
    category = "electronics"
    response = get(f"/products/category/{category}")
    assert response.status_code == 200
    for product in response.json():
        assert product["category"] == category