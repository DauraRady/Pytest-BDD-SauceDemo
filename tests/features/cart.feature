Feature: Ajout au Panier

  Scenario: Ajouter deux produits les plus chers au panier
    Given l'utilisateur a trié les produits par prix décroissant
    When il ajoute les deux premiers produits au panier
    Then le panier doit contenir 2 articles
