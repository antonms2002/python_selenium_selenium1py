# Selenium Test Framework for Books Shop

## About Project
The project contains automated UI tests using POM for an online books shop (http://selenium1py.pythonanywhere.com/).  

## Technologies
- Python 3.10+
- pytest
- Selenium WebDriver
- Allure (reporting)
- Faker (test data generation)
- python-dotenv (environment variables)
- GitHub Actions (CI)

## Setup and Run

1. Clone the repository  
   `git clone https://github.com/antonms2002/python_selenium_selenium1py.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Create `.env` file from example  
   `cp .env.example .env`  
   (If .env is missing, default values from config.py are used)

4. Run tests  
   `pytest --alluredir=allure-results`

### Custom parameters
- Language: `pytest --language=es` (default: en)
- Headless mode: `pytest --headless=false` (default: true)

## Allure Report

1. Generate report from results:  
   `allure generate allure-results --clean`

2. Open report:  
   `allure open allure-report`

## CI/CD (GitHub Actions)

The workflow is defined in `.github/workflows/run_tests.yml`.

- **Triggers:**  
  - Manual via `workflow_dispatch` (GitHub UI → Actions → Run workflow)  
  - Automatic on push to `main` branch

- **What it does:**  
  - Sets up Python 3.10, Chrome browser  
  - Installs dependencies  
  - Runs all tests in headless mode

## Project Structure
project/
├── pages/
│   # Page Object classes (BasePage -> MainPage, LoginPage, ProductPage, CartPage)
├── components/
│   # Reusable components (Navbar: login link, go to cart button)
├── tests/
│   # Test files (test_main_page, test_product_page, test_login_page)
├── conftest.py
│   # Pytest fixtures, hooks (addoption, screenshots, browser setup, logging)
├── config.py
│   # Reads environment variables (BASE_URL, DEFAULT_TIMEOUT)
├── .env.example
│   # Example of environment variables
├── pytest.ini
│   # Pytest configuration (markers, addopts)
├── requirements.txt
└── .github/workflows/
    # GitHub Actions workflows