# loaders/evidence_loader.py

import pandas as pd
from config import DATASET_DIR

evidence_df = pd.read_csv(
    DATASET_DIR / "evidence_requirements.csv"
)


def get_requirement(

        claim_object,
        issue_type

):

    rows = evidence_df[

        (
            evidence_df.claim_object
            == claim_object
        )

    ]

    if len(rows) == 0:

        rows = evidence_df[
            evidence_df.claim_object == "all"
        ]

    return rows.iloc[0].to_dict()