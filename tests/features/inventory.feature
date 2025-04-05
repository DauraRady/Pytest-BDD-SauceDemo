Feature: Tri des Produits

  Scenario: Trier les produits du plus cher au moins cher
    Given l'utilisateur est connecté
    When il trie les produits par prix décroissant
    Then les produits doivent être affichés du plus cher au moins cher
