"""Arquivo de teste do schema definido."""

import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))
import subprocess
from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Função que inicializa o Selenium e o WebDriver."""
    processo = subprocess.Popen(["streamlit", "run", "main.py"])

    driver = webdriver.Chrome()
    driver.get("http://localhost:8501")
    driver.set_page_load_timeout(10)

    yield driver

    driver.quit()
    processo.kill()


def test_open_app(driver):
    """Testa se o site está aberindo corretamente."""
    driver.get("http://localhost:8501")
    sleep(2)


def test_title_app(driver):
    """Testa se o site está com o titulo correto."""
    driver.get("http://localhost:8501")
    sleep(2)
    assert driver.title == "Validador de CSV"