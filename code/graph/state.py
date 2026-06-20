# graph/state.py

from typing import TypedDict


class ClaimState(TypedDict):

    # Input
    user_id: str
    image_paths: list[str]
    user_claim: str
    claim_object: str

    # Intermediate outputs
    parsed_claim: dict
    image_analysis: dict
    evidence_result: dict
    history_result: dict

    # Final decision
    final_decision: dict

    # Output row
    output_row: dict