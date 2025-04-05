import os
import pytest
import sys
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

scenarios('../features/login.feature')  # ou le chemin relatif vers le fichier .feature


@pytest.fixture
def login_page(setup):
    return LoginPage(setup)

@given("l'utilisateur est sur la page de connexion")
def open_login_page(setup):
    setup.get("https://www.saucedemo.com/")

@when(parsers.parse('il entre son nom d\'utilisateur "{username}" et son mot de passe "{password}"'))
def enter_credentials(login_page, username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)

@when("il clique sur le bouton de connexion")
def click_login(login_page):
    login_page.click_login()

@then("il doit être redirigé vers la page des produits")
def verify_login_success(setup):
    assert "inventory.html" in setup.current_url, "Erreur : L'utilisateur n'a pas été redirigé"

@then(parsers.parse('un message d\'erreur "{expected_error}" doit s\'afficher'))
def verify_login_failure(login_page, expected_error):
    actual_message = login_page.get_error_message()
    assert actual_message == expected_error, f"Erreur attendue : {expected_error}, mais obtenu : {actual_message}"
