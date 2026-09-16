"""
data_loader.py
----------------
Ce script charge les avis clients bruts et les nettoie pour qu'ils soient
prêts à être utilisés en NLP et en analyse temporelle.

Étapes :
1. Charger le CSV brut
2. Convertir le timestamp Unix en vraie date
3. Nettoyer le texte (minuscules, ponctuation, espaces multiples)
4. Supprimer les doublons et valeurs manquantes
5. Sauvegarder le résultat dans data/processed/
"""

import pandas as pd
import re
import os


def load_raw_data(filepath: str) -> pd.DataFrame:
    """
    Charge le fichier CSV brut.

    On utilise pandas car c'est le standard pour manipuler des données
    tabulaires en Python. On garde cette fonction séparée (plutôt que de
    tout faire dans un seul gros bloc) pour pouvoir la réutiliser ou la
    tester indépendamment plus tard.
    """
    df = pd.read_csv(filepath)
    print(f"Données chargées : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    return df


def convert_timestamp(df: pd.DataFrame, time_col: str = "Time") -> pd.DataFrame:
    """
    Convertit le timestamp Unix (nombre de secondes depuis 1970) en une
    vraie date lisible.

    Pourquoi c'est important : sans ça, impossible de faire de la série
    temporelle plus tard. On crée aussi des colonnes Year/Month séparées,
    pratiques pour agréger les données ensuite (ex: nombre d'avis par mois).
    """
    df["Date"] = pd.to_datetime(df[time_col], unit="s")
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.to_period("M")
    return df


def clean_text(text: str) -> str:
    """
    Nettoie une chaîne de texte brute pour le NLP.

    Étapes du nettoyage (et pourquoi) :
    - minuscules : "Good" et "good" doivent être traités comme le même mot
    - suppression des balises HTML résiduelles (fréquentes dans les avis web)
    - suppression de la ponctuation : elle n'apporte pas d'info pour un
      modèle bag-of-words / TF-IDF classique
    - suppression des espaces multiples : nettoyage cosmétique final
    """
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"<.*?>", " ", text)          # balises HTML
    text = re.sub(r"[^a-zA-Z\s]", " ", text)    # garde uniquement les lettres
    text = re.sub(r"\s+", " ", text).strip()    # espaces multiples -> un seul
    return text


def remove_duplicates_and_na(df: pd.DataFrame, text_col: str = "Text") -> pd.DataFrame:
    """
    Supprime les lignes dupliquées et celles où le texte est manquant.

    On le fait APRÈS le nettoyage du texte (pas avant), car deux avis
    identiques avec une casse différente ("Good!" vs "good") ne seraient
    pas détectés comme doublons sinon.
    """
    before = len(df)
    df = df.dropna(subset=[text_col])
    df = df[df[text_col].str.strip() != ""]
    df = df.drop_duplicates(subset=[text_col])
    after = len(df)
    print(f"Suppression doublons/NA : {before - after} lignes retirées "
          f"({before} -> {after})")
    return df


def run_pipeline(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Orchestre toutes les étapes ci-dessus dans l'ordre, et sauvegarde
    le résultat final.
    """
    df = load_raw_data(input_path)
    df = convert_timestamp(df)
    df["Text_clean"] = df["Text"].apply(clean_text)
    df = remove_duplicates_and_na(df, text_col="Text_clean")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Données nettoyées sauvegardées dans : {output_path}")
    return df


if __name__ == "__main__":
    RAW_PATH = "data/raw/sample_reviews.csv"
    PROCESSED_PATH = "data/processed/reviews_clean.csv"

    df_clean = run_pipeline(RAW_PATH, PROCESSED_PATH)
    print("\nAperçu des données nettoyées :")
    print(df_clean[["Date", "Score", "Text_clean"]].head())
