import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


scenarios("../features/checkout.feature")


# ---------------- FIXTURES ---------------- #

@pytest.fixture
def checkout_page(login_user):
    cart_page = login_user.go_to_cart()
    return cart_page.go_to_checkout()


# ---------------- ÉTAPES GIVEN ---------------- #

@given("l'utilisateur est connecté")
def utilisateur_connecte(login_user):
    return login_user

@given("l'utilisateur a trié les produits par prix décroissant")
def utilisateur_a_tri(login_user):
    login_user.sort_products_high_to_low()

@given("l'utilisateur a ajouté des produits au panier")
def utilisateur_a_ajoute(login_user):
    login_user.sort_products_high_to_low()
    login_user.add_top_two_products_to_cart()


# ---------------- ÉTAPES WHEN ---------------- #

@when("il trie les produits du plus cher au moins cher")
def trie_desc(login_user):
    login_user.sort_products_high_to_low()

@when("il ajoute les deux premiers produits au panier")
def ajout_deux(login_user):
    login_user.add_top_two_products_to_cart()

@when("il accède au panier et clique sur Checkout")
def aller_checkout():  # cette étape est remplacée par la fixture `checkout_page`
    pass  # rien à faire ici car `checkout_page` est injectée dans les étapes suivantes

@when(parsers.parse('il saisit les informations de livraison "{prenom}" "{nom}" "{code_postal}"'))
def saisie_infos(checkout_page, prenom, nom, code_postal):
    checkout_page.enter_shipping_info(prenom, nom, code_postal)

@when("il finalise la commande")
def fin_commande(checkout_page):
    checkout_page.finalize_order()


# ---------------- ÉTAPES THEN ---------------- #

@then("le panier doit contenir 2 articles")
def verifier_panier(login_user):
    assert login_user.get_cart_count() == 2

@then("la commande doit être confirmée")
def verif_confirmation(checkout_page):
    assert "THANK YOU" in checkout_page.get_confirmation_message().upper()

@then("les produits doivent être triés correctement")
def produits_triés():
    # À implémenter si tu veux comparer les prix
    pass
