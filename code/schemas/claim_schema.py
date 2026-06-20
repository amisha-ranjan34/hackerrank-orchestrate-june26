from pydantic import BaseModel

class ParsedClaim(BaseModel):

    issue_type: str

    object_part: str

    claim_summary: str