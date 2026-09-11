# Catálogo do SauceDemo — Selenium e Python

[English version](README.en.md)

Testes contra **https://www.saucedemo.com/**, com Page Object e casos parametrizados. Complementa meu [checkout com Selenium](https://github.com/brunobaccari/selenium-test-checkout-automation) com verificações de catálogo, detalhe do produto e sessão.

## Instalação

Python 3.12 ou superior e Google Chrome. O CI usa Python 3.14. Selenium Manager resolve o driver; não há executável de ChromeDriver versionado.

```bash
python -m venv .venv
```

Ative com `.venv\Scripts\activate` no Windows ou `source .venv/bin/activate` no Linux/macOS.

```bash
cp .env.example .env
python -m pip install -r requirements.txt
python -m pytest -q --junitxml=results/junit.xml
```

## Cenários

- Ordenação crescente e decrescente com comparação da sequência completa de preços.
- Detalhe de mochila e lanterna: nome, preço e retorno ao catálogo.
- Adição pelo detalhe e remoção pelo carrinho.
- Logout impede acesso direto ao catálogo sem novo login.

## Organização

`pages.py` reúne as interações com o catálogo. `tests/test_catalog.py` contém expectativas explícitas e parâmetros. `tests/conftest.py` abre um navegador por teste e guarda screenshot em falhas.

## Relatórios e limites

JUnit e screenshots em `results/`, publicados como artifacts no CI. [Execuções e artifacts no Actions](https://github.com/brunobaccari/selenium-saucedemo-tests/actions). Sem aplicação local, mocks ou sleeps. Usa somente a conta pública `standard_user/secret_sauce` do ambiente de demonstração. Mudanças no catálogo podem alterar os resultados esperados e precisam ser revisadas.

## Configuração do ambiente

O Page Object aguarda visibilidade e estabilidade da posição e dimensão antes de devolver um elemento. O logout é ativado por teclado. Não há repetição automática de ações nem de cenários.

Copie `.env.example` para `.env` (`Copy-Item .env.example .env` no PowerShell ou `cp .env.example .env` no Linux/macOS). As variáveis do processo têm prioridade. `.env` não é versionado. URLs e credenciais ficam nessa configuração; os valores esperados dos testes permanecem nos cenários.

As contas do exemplo são públicas e exclusivas de demonstração. Para outro ambiente, injete credenciais via secrets do CI e confirme também o contrato e os dados esperados antes de executar.

Datas de commits deste portfólio foram reorganizadas retroativamente; as execuções do Actions mantêm suas datas reais.
