# loaders/history_loader.py

import pandas as pd
from config import DATASET_DIR

history_df = pd.read_csv(
    DATASET_DIR / "user_history.csv"
)


def get_history(user_id):

    row = history_df[
        history_df.user_id == user_id
    ]

    if len(row) == 0:

        return {}

    return row.iloc[0].to_dict()