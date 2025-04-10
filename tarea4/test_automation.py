import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def setup():
    # Configuración del navegador (Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_homepage(setup):
    driver = setup
    try:
        driver.get("file:///c:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
        assert "Tienda de Computadoras" in driver.title, "El título de la página no coincide"
    except Exception as e:
        driver.save_screenshot("error_homepage.png")
        raise e
    driver.save_screenshot("homepage.png")

def test_login(setup):
    driver = setup
    try:
        driver.get("file:///c:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "loginButton").click()

        # Manejar la alerta
        alert = driver.switch_to.alert
        alert.accept()

        time.sleep(1)  # Espera para que se actualice la página
        driver.save_screenshot("login_success.png")
    except Exception as e:
        driver.save_screenshot("error_login.png")
        raise e

def test_click_link(setup):
    driver = setup
    driver.get("file:///c:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
    link = driver.find_element(By.TAG_NAME, "a")
    link.click()
    assert "iana.org" in driver.current_url, "La redirección no ocurrió correctamente"
    driver.save_screenshot("after_click.png")

def test_logout(setup):
    driver = setup
    try:
        driver.get("file:///c:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "loginButton").click()

        # Manejar la alerta
        alert = driver.switch_to.alert
        alert.accept()

        # Cerrar sesión
        logout_button = driver.find_element(By.ID, "logoutButton")
        logout_button.click()

        # Manejar la alerta de cierre de sesión
        alert = driver.switch_to.alert
        alert.accept()

        time.sleep(1)
        driver.save_screenshot("logout_success.png")
    except Exception as e:
        driver.save_screenshot("error_logout.png")
        raise e

def test_login_and_logout(setup):
    driver = setup
    try:
        driver.get("file:///c:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
        driver.save_screenshot("before_login.png")

        # Iniciar sesión
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "loginButton").click()

        # Manejar la alerta
        alert = driver.switch_to.alert
        alert.accept()

        time.sleep(1)
        driver.save_screenshot("after_login.png")

        # Cerrar sesión
        logout_button = driver.find_element(By.ID, "logoutButton")
        logout_button.click()

        # Manejar la alerta de cierre de sesión (si existe)
        time.sleep(1)
        driver.save_screenshot("after_logout.png")
    except Exception as e:
        driver.save_screenshot("error.png")
        raise e

def test_products_visible_after_login(setup):
    driver = setup
    try:
        driver.get("file:///c:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "loginButton").click()

        # Manejar la alerta
        alert = driver.switch_to.alert
        alert.accept()

        # Verificar que los productos sean visibles
        products = driver.find_element(By.ID, "products")
        assert products.is_displayed(), "Los productos no son visibles después de iniciar sesión"
        driver.save_screenshot("products_visible.png")
    except Exception as e:
        driver.save_screenshot("error_products.png")
        raise e