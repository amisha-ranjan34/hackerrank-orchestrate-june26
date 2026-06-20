# agents/formatter_agent.py


def format_output(

        row,
        decision

):

    return {

        "user_id":
            row["user_id"],

        "image_paths":
            row["image_paths"],

        "user_claim":
            row["user_claim"],

        "claim_object":
            row["claim_object"],

        "evidence_standard_met":
            decision[
                "evidence_standard_met"
            ],

        "evidence_standard_met_reason":
            decision[
                "evidence_standard_met_reason"
            ],

        "risk_flags":
            decision[
                "risk_flags"
            ],

        "issue_type":
            decision[
                "issue_type"
            ],

        "object_part":
            decision[
                "object_part"
            ],

        "claim_status":
            decision[
                "claim_status"
            ],

        "claim_status_justification":
            decision[
                "claim_status_justification"
            ],

        "supporting_image_ids":
            decision[
                "supporting_image_ids"
            ],

        "valid_image":
            decision[
                "valid_image"
            ],

        "severity":
            decision[
                "severity"
            ]
    }