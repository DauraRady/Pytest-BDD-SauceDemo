Feature: Connexion à l'application

  Scenario: Connexion réussie
    Given l'utilisateur est sur la page de connexion
    When il entre son nom d'utilisateur "standard_user" et son mot de passe "secret_sauce"
    And il clique sur le bouton de connexion
    Then il doit être redirigé vers la page des produits

  Scenario: Connexion échouée avec un utilisateur bloqué
    Given l'utilisateur est sur la page de connexion
    When il entre son nom d'utilisateur "locked_out_user" et son mot de passe "secret_sauce"
    And il clique sur le bouton de connexion
    Then un message d'erreur "Epic sadface: Sorry, this user has been locked out." doit s'afficher
