# API d'analyse statistique

API REST simple en Python permettant de calculer des indicateurs statistiques sur deux séries numériques.

## 📋 Prérequis

- Python ≥ 3.10
- pip

## 🚀 Installation

1. **Créer et activer l'environnement virtuel** :

```bash
# Créer l'environnement virtuel
python -m venv env

# Activer l'environnement virtuel
# Sur Linux/Mac :
source env/bin/activate
# Sur Windows :
# env\Scripts\activate
```

1. **Installer les dépendances** :

```bash
pip install -r requirements.txt
```

## ▶️ Lancer l'API

```bash
uvicorn src.main:app --reload
```

L'API sera accessible à l'adresse : `http://localhost:8000`

### Documentation interactive

Une fois l'API lancée, vous pouvez accéder à :

- **Swagger UI** : `http://localhost:8000/docs`
- **ReDoc** : `http://localhost:8000/redoc`

## 🧪 Lancer les tests

```bash
pytest tests/ -v
```

## 📡 Utilisation de l'API

### Endpoint : POST /analyze

Calcule la moyenne de chaque série et le coefficient de corrélation de Pearson entre les deux séries.

**Requête** :

```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{
       "x": [1, 2, 3, 4, 5],
       "y": [2, 4, 5, 4, 5]
     }'
```

**Réponse** :

```json
{
  "mean_x": 3.0,
  "mean_y": 4.0,
  "correlation": 0.7746
}
```

## 🏗️ Structure du projet

```text
Test/
├── env/                 # Environnement virtuel (créé après installation)
├── src/
│   ├── __init__.py
│   ├── main.py         # Application FastAPI principale
│   ├── models.py       # Modèles Pydantic
│   ├── routes.py       # Routes/endpoints
│   └── statistics.py   # Module de calculs statistiques
├── tests/
│   ├── __init__.py
│   ├── test_api.py     # Tests de l'API
│   └── test_statistics.py  # Tests des calculs statistiques
├── requirements.txt    # Dépendances Python
└── README.md          # Ce fichier
```

## 📝 Notes techniques

- **Calculs explicites** : Les calculs statistiques sont implémentés explicitement (pas d'appel direct à des fonctions statistiques avancées)
- **Gestion des erreurs** : L'API gère les cas suivants :
  - Séries de longueurs différentes
  - Listes vides
  - Valeurs non numériques
- **Séparation des responsabilités** : La logique métier est séparée de l'API
- **Typage** : Le code utilise le typage Python

## ⏱️ Temps passé

1h30
