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

