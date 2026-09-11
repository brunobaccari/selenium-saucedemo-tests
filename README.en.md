# SauceDemo catalog — Selenium and Python

[Versão em português](README.md)

Tests against the hosted [SauceDemo](https://www.saucedemo.com/) site, using a Page Object and parameterized cases. This extends my [Selenium checkout project](https://github.com/brunobaccari/selenium-test-checkout-automation) with catalog, product-detail and session checks.

## Run

Python 3.12 or later and Google Chrome. CI uses Python 3.14. Selenium Manager resolves the driver; no ChromeDriver executable is committed here.

Create a virtual environment with `python -m venv .venv` and activate it with `.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on Linux/macOS.

```bash
cp .env.example .env
python -m pip install -r requirements.txt
python -m pytest -q --junitxml=results/junit.xml
```

Use `Copy-Item .env.example .env` on PowerShell. URLs and public demo credentials are loaded from `.env`; process variables take precedence. `.env` is ignored by Git. Private credentials belong in CI secrets when adapting the project.

## Scenarios

Six cases cover both price-sort directions with complete expected sequences, backpack and bike-light details and return navigation, adding from product details and removing in the cart, and logout followed by direct access to the protected catalog.

`pages.py` contains catalog interactions. `tests/test_catalog.py` holds explicit expectations. `tests/conftest.py` opens a browser per test and captures screenshots on failure.

Before returning an element, the Page Object waits for visibility and stable position/dimensions. It reads fresh references while waiting. Logout is activated with Enter, exercising keyboard navigation. Actions and tests are not automatically retried.

## Evidence and limits

JUnit and screenshots are written to `results/` and uploaded by CI. See [Actions runs and artifacts](https://github.com/brunobaccari/selenium-saucedemo-tests/actions). No local application, mocks or fixed sleeps. Only the public demo account is used. Catalog changes may require reviewing expected results.

Commit dates in this portfolio were reorganized retroactively; Actions runs retain their actual execution dates.
