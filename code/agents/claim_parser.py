from models.groq_model import groq_llm
from schemas.claim_schema import ParsedClaim

parser_llm = groq_llm.with_structured_output(
    ParsedClaim
)

def parse_claim(user_claim):

    prompt = f"""
Extract:

issue_type
object_part
claim_summary

Allowed issue types:

dent
scratch
crack
glass_shatter
broken_part
missing_part
torn_packaging
crushed_packaging
water_damage
stain

Conversation:

{user_claim}
"""

    response = parser_llm.invoke(prompt)

    return response.model_dump()