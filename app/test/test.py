import subprocess
import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture
def driver():
    process =subprocess.Popen(["streamlit", "run", "app/main.py"])
    
    driver = webdriver.Chrome()
    driver.get("http://localhost:8501")
    driver.set_page_load_timeout(60)
    
    yield driver
    
    driver.quit()
    process.kill()
    
def test_open(driver):
    driver.get("http://localhost:8501")
    sleep(10)

def test_title(driver):
    driver.get("http://localhost:8501")
    sleep(10)
    assert driver.title == "Validador de CSV"
    