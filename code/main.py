# main.py

import pandas as pd
from tqdm import tqdm

from config import CODE_DIR, DATASET_DIR
from graph.workflow import graph
from loaders.csv_loader import load_claims
from utils.logger import logger

OUTPUT_PATH = CODE_DIR / "outputs" / "output.csv"


def create_failure_row(row, error):

    return {

        "user_id": row["user_id"],

        "image_paths": row["image_paths"],

        "user_claim": row["user_claim"],

        "claim_object": row["claim_object"],

        "evidence_standard_met": False,

        "evidence_standard_met_reason":
            "Pipeline failure",

        "risk_flags":
            "manual_review_required",

        "issue_type":
            "unknown",

        "object_part":
            "unknown",

        "claim_status":
            "not_enough_information",

        "claim_status_justification":
            str(error),

        "supporting_image_ids":
            "none",

        "valid_image":
            False,

        "severity":
            "unknown"
    }


def process_claim(row):

    raw_paths = row["image_paths"].split(";")
    abs_paths = [
        str(DATASET_DIR / p) for p in raw_paths
    ]

    state = {

        "user_id": row["user_id"],

        "image_paths": abs_paths,

        "user_claim": row["user_claim"],

        "claim_object": row["claim_object"]

    }

    result = graph.invoke(state)

    return result["output_row"]


def main():

    logger.info("Loading claims...")

    claims_df = load_claims()

    rows = []

    for _, row in tqdm(
            claims_df.iterrows(),
            total=len(claims_df),
            desc="Processing Claims"
    ):

        try:

            logger.info(
                f"Processing {row['user_id']}"
            )

            output_row = process_claim(row)

            rows.append(output_row)

        except Exception as e:

            logger.error(
                f"{row['user_id']} failed: {e}"
            )

            rows.append(
                create_failure_row(
                    row,
                    e
                )
            )

    output_df = pd.DataFrame(rows)

    output_df = output_df[

        [

            "user_id",

            "image_paths",

            "user_claim",

            "claim_object",

            "evidence_standard_met",

            "evidence_standard_met_reason",

            "risk_flags",

            "issue_type",

            "object_part",

            "claim_status",

            "claim_status_justification",

            "supporting_image_ids",

            "valid_image",

            "severity"

        ]

    ]

    output_df.to_csv(

        OUTPUT_PATH,

        index=False

    )

    logger.info("Finished.")

    print(
        f"\nOutput saved to {OUTPUT_PATH}"
    )


if __name__ == "__main__":

    main()