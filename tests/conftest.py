import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.inventory_page import InventoryPage  # ✅ Nécessaire pour login_user

@pytest.fixture(scope="function")
def setup():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")  # ✅ empêche la barre "Chrome est contrôlé"
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")  # ✅ pour isoler et ne rien conserver du cache
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2  # ✅ bloque les notifications
    })

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_user(setup):
    """
    Effectue la connexion à l'application avec les identifiants :
    standard_user / secret_sauce et retourne la page d'inventaire.
    """
    setup.get("https://www.saucedemo.com/")
    setup.find_element("id", "user-name").send_keys("standard_user")
    setup.find_element("id", "password").send_keys("secret_sauce")
    setup.find_element("id", "login-button").click()
    return InventoryPage(setup)  # ✅ Retourne une instance utilisable directement dans les steps
