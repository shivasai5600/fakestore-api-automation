# FakeStore API Automation (Python + Pytest)

## Overview
This project demonstrates API automation using Python, Pytest, and Requests library for testing the FakeStore API.

## Features
- Modular framework design with reusable API client
- Comprehensive test cases (positive and negative)
- Logging and HTML reporting
- CI/CD using GitHub Actions

## Test Coverage
- GET /products - Fetch all products
- GET /products/{id} - Fetch single product
- POST /products - Create new product
- GET /products/categories - Fetch all categories
- GET /products/category/{category} - Filter products by category
- Negative test cases (invalid IDs, etc.)

## Setup & Installation

### Prerequisites
- Python 3.8+
- pip

### Steps
```bash
# Clone the repository
git clone https://github.com/shivasai5600/fakestore-api-automation.git
cd fakestore-api-automation

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Generate HTML report
pytest --html=reports/report.html