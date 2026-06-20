from pydantic import BaseModel


class FinalDecision(BaseModel):

    evidence_standard_met: bool

    evidence_standard_met_reason: str

    risk_flags: str

    issue_type: str

    object_part: str

    claim_status: str

    claim_status_justification: str

    supporting_image_ids: str

    valid_image: bool

    severity: str