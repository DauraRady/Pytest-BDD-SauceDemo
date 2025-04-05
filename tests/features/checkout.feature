Feature: Achat de produits sur SauceDemo

  Scenario: Trier les produits du plus cher au moins cher
    Given l'utilisateur est connecté
    When il trie les produits du plus cher au moins cher
    Then les produits doivent être triés correctement

  Scenario: Ajouter deux produits au panier
    Given l'utilisateur a trié les produits par prix décroissant
    When il ajoute les deux premiers produits au panier
    Then le panier doit contenir 2 articles

  Scenario Outline: Finaliser une commande
    Given l'utilisateur a ajouté des produits au panier
    When il accède au panier et clique sur Checkout
    And il saisit les informations de livraison "<prenom>" "<nom>" "<code_postal>"
    And il finalise la commande
    Then la commande doit être confirmée

    Examples:
      | prenom | nom  | code_postal |
      | Daura  | Rady | 91130       |
