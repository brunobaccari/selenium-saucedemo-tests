from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
import pytest
from selenium import webdriver
from pages import CatalogPage


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f'rep_{report.when}', report)


@pytest.fixture
def catalog(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1280,900')
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(45)
    try:
        page = CatalogPage(driver)
        page.login()
        yield page
    finally:
        report = getattr(request.node, 'rep_call', None)
        if report is None or report.failed:
            Path('results').mkdir(exist_ok=True)
            driver.save_screenshot(f'results/{request.node.name}.png')
        driver.quit()
