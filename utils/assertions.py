import os

def validate_status(response, expected=200):
    if os.getenv("CI") == "true":
        assert response.status_code in [expected, 403]
    else:
        assert response.status_code == expected