# 📌 Projet de Test Automatisé avec **Pytest-BDD + POM**

Ce projet est une suite de tests automatisés pour le site [Sauce Demo](https://www.saucedemo.com/) utilisant **Pytest-BDD** et **Page Object Model (POM)**.

# 🧪 Projet QA Automation – Saucedemo E2E

Ce projet est une **automatisation complète** du site [saucedemo.com](https://www.saucedemo.com), avec une architecture professionnelle respectant les bonnes pratiques QA : **BDD**, **Page Object Model**, et intégration **CI/CD GitHub Actions**.

---

## 🚀 Objectifs

- Valider les parcours utilisateurs critiques : connexion, panier, commande.
- Détecter les anomalies fonctionnelles ou UX sur un site e-commerce.
- Appliquer une structure propre et scalable en automation QA.
- Fournir un exemple pro à intégrer dans mon portfolio GitHub.

---

## 🛠️ Stack technique

| Élément         | Outil                                  |
| --------------- | -------------------------------------- |
| Langage         | Python 3.10                            |
| Framework tests | `pytest`, `pytest-bdd`                 |
| Automatisation  | Selenium WebDriver                     |
| Pattern         | Page Object Model (POM)                |
| Gherkin         | Scénarios `.feature` en langage métier |
| Rapports        | HTML avec `pytest-html`                |
| CI/CD           | GitHub Actions                         |

---

## 📁 Architecture du projet

## 📂 **Structure du Projet**

```
pom_selenium/
├── pages/                     # Page Object Model (POM)
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│
├── tests/
│   ├── features/              # Scénarios Gherkin
│   │   ├── login.feature
│   │   ├── cart.feature
│   │   └── checkout.feature
│   ├── step_definitions/      # Steps Python liés aux features
│   │   ├── test_login.py
│   │   ├── test_cart.py
│   │   └── test_checkout.py
│   └── conftest.py            # Fixture WebDriver
│
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline GitHub Actions
│
├── requirements.txt           # Dépendances Python
├── pytest.ini                 # Config pytest
├── TEST_STRATEGY.md           # Stratégie de test détaillée (inspirée TMAP)
├── README.md                  # Présentation du projet (ci-dessous)


```

## 🔥 **Pourquoi cette structure ?**

1. **Separation des responsabilités**

   - `pages/` : Contient les objets des pages web (POM).
   - `features/` : Contient les scénarios de test en Gherkin.
   - `step_definitions/` : Contient l'implémentation des steps.
   - `conftest.py` : Gère les fixtures pour réduire la duplication de code.
   - `requirements.txt` : Liste les packages Python nécessaires.

2. **Modularité et maintenabilité**

   - En cas de changement sur la page de login, on ne modifie que `login_page.py`.
   - Toutes les pages utilisent les mêmes méthodes que ceux de base page, juste les locators changent: c'est pour cela que dans la base_page, il n'y'a pas de locators définis, on mets juste value.
   - On peut réutiliser `LoginPage` dans d'autres tests.

3. **Intégration simple avec CI/CD**
   - L'utilisation de `pytest` permet une exécution simple dans un pipeline CI/CD.

---

## 📌 **Explication des fichiers**

### **1️⃣ Page Object Model (POM)**

#### `pages/base_page.py`

- Classe de base qui fournit des **méthodes réutilisables** pour interagir avec Selenium.
- Permet d'éviter la duplication du code.Évite la répétition de find_element().
- Ajoute des attentes intelligentes (WebDriverWait) pour éviter les erreurs.

#### `pages/login_page.py`

- Classe spécifique à la page de connexion.
- Utilise `BasePage` pour interagir avec les champs d'entrée et le bouton de connexion.

```python
class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
```

### **2️⃣ Les Scénarios en Gherkin**

#### `tests/features/login.feature`

Ce fichier contient **deux scénarios** :

1. **Connexion réussie**
2. **Connexion échouée** avec un utilisateur bloqué.

```gherkin
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
```

### **Pourquoi découper en deux scénarios ?**

- **Un scénario pour le test positif** (connexion réussie).
- **Un scénario pour le test négatif** (connexion refusée).
- Ça permet de **tester différents comportements de l'application** sans mélanger les cas.

### **3️⃣ Les Step Definitions**

#### `tests/step_definitions/test_login.py`

Ce fichier **lie les scénarios Gherkin avec le code Selenium**.

**Exemple :**

```python
@given("l'utilisateur est sur la page de connexion")
def step_open_login_page(browser):
    browser.get("https://www.saucedemo.com")
```

➡ Associe `Given l'utilisateur est sur la page de connexion` à une fonction qui ouvre la page.

**Gestion du message d'erreur en cas d'échec de connexion** :

```python
@then('un message d\'erreur "<error_message>" doit s\'afficher')
def step_check_error_message(browser, error_message):
    error_element = browser.find_element(By.CLASS_NAME, "error-message-container")
    assert error_element.text == error_message
```

➡ **Vérifie que le message d'erreur affiché correspond à l'attendu.**

---

## 📌 **Gestion du navigateur avec `conftest.py`**

Dans **Pytest**, `conftest.py` permet de **centraliser la gestion des fixtures**.

#### `tests/conftest.py`

```python
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
```

➡ **Pourquoi utiliser une fixture ?**

- Évite d'initialiser `webdriver.Chrome()` à chaque test.
- **Automatise l'ouverture et la fermeture du navigateur**.

---

---

## 📋 Stratégie de test

📄 [Consulter la stratégie de test](./TEST_STRATEGY.md) – inspirée des bonnes pratiques **TMAP**, avec :

- Définition du périmètre
- Analyse des risques produit/projet
- Typologie de tests
- KPI et objectifs qualité
- Roadmap QA

---

## ⚙️ Lancer les tests

1. Créer et activer un environnement virtuel :

````bash
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sur Windows

## 🎯 **Comment exécuter les tests ?**

### 📌 **Installation des dépendances**

```bash
pip install -r requirements.txt
````

### 📌 **Exécution des tests**

```bash
pytest tests/ --bdd-verbose --html=reports/report.html
```

- **`pytest tests/`** → Exécute tous les tests.
- **`--bdd-verbose`** → Affiche les étapes BDD.
- **`--html=reports/report.html`** → Génère un **rapport HTML**.

---

## 🎯 **Pourquoi Pytest-BDD et POM ?**

✅ **Lisibilité avec Gherkin** (lisible pour les non-devs).  
✅ **Modularité avec POM** (meilleure organisation et réutilisation).  
✅ **Exécution rapide et facile en CI/CD**.

---
