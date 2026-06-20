# evaluation/evaluate.py

import pandas as pd

from evaluation.metrics import (
    classification_metrics
)


def evaluate(

        ground_truth_path,

        prediction_path

):

    gt = pd.read_csv(
        ground_truth_path
    )

    pred = pd.read_csv(
        prediction_path
    )

    report = {}

    columns = [
        "claim_status",
        "issue_type",
        "object_part",
        "severity",
        "evidence_standard_met",
        "valid_image"
    ]

    for col in columns:

        metrics = classification_metrics(

            gt[col],

            pred[col]

        )

        report[col] = metrics

    return report