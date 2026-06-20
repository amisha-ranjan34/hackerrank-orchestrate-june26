# loaders/csv_loader.py

import pandas as pd
from config import DATASET_DIR


def load_claims(
        path=None
):
    if path is None:
        path = DATASET_DIR / "claims.csv"

    df = pd.read_csv(path)

    df.columns = df.columns.str.strip()

    return df


def load_sample_claims(
        path=None
):
    if path is None:
        path = DATASET_DIR / "sample_claims.csv"

    df = pd.read_csv(path)

    df.columns = df.columns.str.strip()

    return df