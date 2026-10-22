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
Voir le README à la racine du dépôt, qui présente aussi les résultats.

## Comment lancer
```bash
pip install -r requirements.txt
python src/data_loader.py
```

## Dataset
Amazon Fine Food Reviews — https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
Remplacer `data/raw/sample_reviews.csv` par le `Reviews.csv` téléchargé sur Kaggle.
