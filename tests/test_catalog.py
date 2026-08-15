import pytest
import os
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.parametrize('sort,expected', [
    ('lohi', [799, 999, 1599, 1599, 2999, 4999]),
    ('hilo', [4999, 2999, 1599, 1599, 999, 799]),
])
def test_ordena_catalogo_por_preco(catalog, sort, expected):
    catalog.sort(sort)
    catalog.wait.until(lambda _: catalog.prices() == expected)
    assert catalog.prices() == expected


@pytest.mark.parametrize('product_id,name,price', [
    (4, 'Sauce Labs Backpack', '$29.99'),
    (0, 'Sauce Labs Bike Light', '$9.99'),
])
def test_detalhe_corresponde_ao_produto_escolhido(catalog, product_id, name, price):
    catalog.open_product(product_id)
    assert catalog.element('inventory-item-name').text == name
    assert catalog.element('inventory-item-price').text == price
    catalog.element('back-to-products').click()
    catalog.wait.until(EC.url_contains('/inventory.html'))
    assert len(catalog.prices()) == 6


def test_adiciona_pelo_detalhe_e_remove_pelo_carrinho(catalog):
    catalog.open_product(4)
    catalog.element('add-to-cart').click()
    assert catalog.element('shopping-cart-badge').text == '1'
    catalog.open_cart()
    assert catalog.element('inventory-item-name').text == 'Sauce Labs Backpack'
    catalog.element('remove-sauce-labs-backpack').click()
    catalog.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[data-test="inventory-item"]')))
    assert not catalog.driver.find_elements(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')

