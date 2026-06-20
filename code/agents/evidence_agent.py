# agents/evidence_agent.py

from loaders.evidence_loader import get_requirement


def evaluate_evidence(

        claim_object,
        issue_type,
        image_analysis

):

    requirement = get_requirement(
        claim_object,
        issue_type
    )

    flags = image_analysis.get(
        "image_quality_flags",
        []
    )

    evidence_met = True

    reason = requirement[
        "minimum_image_evidence"
    ]

    if len(flags) > 0:

        evidence_met = False

        reason = (
            "Image quality issue detected."
        )

    return {

        "evidence_standard_met":
            evidence_met,

        "evidence_standard_met_reason":
            reason
    }