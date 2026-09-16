# Analyse et prévision de la réputation client à partir d'avis

Projet data science combinant analyse de données, NLP et séries temporelles,
réalisé en préparation d'un stage.

## Objectif
Analyser des avis clients (Amazon Fine Food Reviews) pour :
- Comprendre l'évolution du sentiment client dans le temps
- Identifier les sujets récurrents de satisfaction/insatisfaction
- Prévoir l'évolution du sentiment sur les prochains mois

## Structure
```
data/raw/         données brutes (non modifiées)
data/processed/   données nettoyées
src/              code source réutilisable
notebooks/        exploration et visualisation
outputs/          figures et modèles générés
```

## Avancement
- [x] Étape 1 : Choix du dataset
- [x] Étape 2 : Structure du projet
- [x] Étape 3 : Chargement et nettoyage des données (`src/data_loader.py`)
- [ ] Étape 4 : Analyse exploratoire (EDA)
- [ ] Étape 5 : Analyse de sentiment (NLP)
- [ ] Étape 6 : Topic modeling
- [ ] Étape 7 : Prévision (séries temporelles)
- [ ] Étape 8 : Dashboard et restitution

## Comment lancer
```bash
pip install -r requirements.txt
python src/data_loader.py
```

## Dataset
Amazon Fine Food Reviews — https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
Remplacer `data/raw/sample_reviews.csv` par le `Reviews.csv` téléchargé sur Kaggle.
