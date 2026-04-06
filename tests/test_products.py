from utils.api_client import get, post
from utils.assertions import validate_status

def test_get_all_products():
    response = get("/products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for product in data:
        assert "id" in product
        assert "title" in product
        assert "price" in product
        assert "category" in product
        assert "image" in product
        assert "rating" in product


def test_get_single_product():
    response = get("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_create_product():
    payload = {
        "title": "Test Product",
        "price": 100,
        "description": "Test Desc",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }

    response = post("/products", payload)
    assert response.status_code == 201
    assert "id" in response.json()


def test_invalid_product():
    response = get("/products/999999")
    assert response.status_code == 200
    if response.text:
        data = response.json()
        assert data != {}
    else:
        assert response.text == ""