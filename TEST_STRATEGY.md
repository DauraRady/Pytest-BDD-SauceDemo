# Stratégie de Test Web - Saucedemo Automation (conforme au modèle TMAP)

## 1. Introduction

Cette stratégie de test décrit le cadre global pour la validation des fonctionnalités critiques du site [saucedemo.com](https://www.saucedemo.com) via une approche d'automatisation basée sur le langage Python et les pratiques BDD (Behavior Driven Development).

Objectifs :

- Assurer la stabilité des parcours utilisateur critiques (connexion, panier, commande).
- Détecter précocement les régressions.
- Appliquer une stratégie inspirée du modèle TMAP (Test Management Approach).
- Valoriser un projet d'automatisation complet dans un objectif de montée en compétences et de portfolio professionnel.

> **Pourquoi l'automatisation complète ?**
>
> Le site Saucedemo est un environnement stable, public, sans évolution fonctionnelle réelle. Ce projet a donc été conçu comme une vitrine technique pour illustrer la mise en place d’une architecture de tests automatisés professionnelle.
>
> - La totalité des cas critiques est connue à l’avance.
> - Le projet vise à démontrer la maîtrise du cycle complet d’automatisation : POM, BDD, CI/CD.
> - Le test exploratoire ou manuel n’apporte pas ici de valeur supplémentaire car le site ne contient ni nouveautés ni comportements dynamiques à investiguer.
>
> ✅ Dans un contexte réel et évolutif, une stratégie hybride serait bien sûr privilégiée (manuel + exploratoire + auto).

## 2. Définition du périmètre

### Modules et fonctionnalitées concernées :

- **Connexion utilisateur**
- **Ajout/suppression de produits au panier**
- **Validation du panier (checkout)**
- **Gestion des erreurs (utilisateur bloqué, formulaire vide, etc.)**

### Adhérences et impacts :

- Affichage dynamique (JS)
- Flux de navigation entre pages (URL)
- Comportement conditionnel selon l'utilisateur

## 2.1 Cas de test couvert par la stratégie

### ✅ Cas de test 1 : Connexion & Déconnexion

- Se connecter avec le compte `standard_user / secret_sauce`
- Vérifier qu’on est bien connecté
- Déconnecter l’utilisateur
- Vérifier qu’on est bien déconnecté

### ❌ Cas de test 2 : Connexion échouée

- Se connecter avec le compte `locked_out_user / secret_sauce`
- Vérifier le message d’erreur attendu

### 🛒 Cas de test 3 : Tri, Panier et Commande

- Se connecter avec le compte standard
- Trier les produits du plus cher au moins cher
- Ajouter les deux premiers produits au panier
- Vérifier qu’on a bien deux produits dans le panier
- Saisir les informations client (en paramètres)
- Finaliser la commande
- Vérifier que la commande s’est bien réalisée

### 🧾 Cas de test 3.bis : Vérification des prix au checkout

- Lors du checkout, vérifier que les prix des produits sont corrects et matchés

## 3. Analyse des Risques Produit

### 3.1 Dimensions analysées :

- **Criticité métier** : impact si la fonctionnalité ne marche pas
- **Complexité technique** : probabilité d'apparition de défaut
- **Caractéristiques de qualité** : stabilité, performance, expérience utilisateur

### 3.2 Tableau des Risques

| Fonctionnalité    | Criticité | Complexité | Qualité visée         | Classe de risque |
| ----------------- | --------- | ---------- | --------------------- | ---------------- |
| Connexion         | élevée    | faible     | fiabilité, UX         | élevée           |
| Gestion du panier | moyenne   | moyenne    | cohérence des données | moyenne          |
| Checkout          | élevée    | moyenne    | stabilité, séquence   | élevée           |
| Message d'erreur  | moyenne   | faible     | clarté, accessibilité | faible-moyenne   |

### 3.3 Typologie des tests associés

| Fonctionnalité    | Type de test                          |
| ----------------- | ------------------------------------- |
| Connexion         | tests fonctionnels, tests négatifs    |
| Panier            | tests fonctionnels, tests de séquence |
| Checkout          | tests end-to-end, tests de validation |
| Messages d'erreur | tests UX, tests de régression         |

## 4. Analyse des Risques Projet

| Risque                         | Impact potentiel                 | Plan de mitigation                               |
| ------------------------------ | -------------------------------- | ------------------------------------------------ |
| Instabilité de l'environnement | Tests faussés ou instables       | Utiliser des attentes explicites (WebDriverWait) |
| Non-prévisibilité des cas      | Oubli de tests critiques         | Définir les scénarios avec des features Gherkin  |
| Variabilité des données        | Données utilisateurs différentes | Utiliser des utilisateurs dédiés prévisibles     |

## 5. Effort de Test

### Approche recommandée : **approche basée sur les risques** + **BDD automatisée**

| Fonctionnalité   | Classe de risque | Effort de test     | Exemples de tests                             |
| ---------------- | ---------------- | ------------------ | --------------------------------------------- |
| Connexion        | élevée           | tests profonds     | user OK, user bloqué, champ vide              |
| Panier           | moyenne          | tests modérés      | ajout, retrait, vérification quantité         |
| Checkout         | élevée           | tests E2E complets | checkout sans champs, checkout réussi         |
| Message d'erreur | moyenne          | tests ciblés       | erreur visible, texte conforme, accessibilité |

## 6. Phases de test

### 6.1 Tests unitaires (via POM)

- Test de chaque méthode POM : click, send_keys, get_text
- Critère de sortie : 100 % des méthodes stables

### 6.2 Tests d'assemblage (BDD)

- Chaque scénario Gherkin = combinaison de plusieurs actions utilisateur
- Critère de sortie : 90 % des scénarios passent

### 6.3 Tests de validation

- Exécution sur environnement stable (CI/CD)
- Critère : 95 % des parcours critiques OK + rapport HTML + logs

## 7. KPI et Suivi

| Indicateur                                | Objectif           |
| ----------------------------------------- | ------------------ |
| Taux de réussite des tests                | ≥ 95 %             |
| Taux de couverture des parcours critiques | ≥ 80 %             |
| Temps moyen d'exécution d'une campagne    | < 30 secondes      |
| Nombre de tests automatisés               | ≥ 10 scénarios BDD |
| Rapport généré automatiquement            | Oui                |

## 8. Conclusion

Ce projet illustre une stratégie de test moderne, outillée et orientée métier grâce à la BDD. Elle permet de prototyper rapidement une suite de tests robustes, compréhensibles par tous les acteurs projet, et exécutables automatiquement via CI/CD. Le choix de tout automatiser est volontaire et adapté au contexte stable de Saucedemo.
