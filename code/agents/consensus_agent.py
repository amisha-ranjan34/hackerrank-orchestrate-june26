# agents/consensus_agent.py

from models.groq_model import groq_llm
from schemas.decision_schema import FinalDecision

decision_llm = groq_llm.with_structured_output(
    FinalDecision
)


def consensus_decision(

        parsed_claim,
        image_analysis,
        evidence_result,
        history_result

):

    prompt = f"""

User claim:

{parsed_claim}

Image findings:

{image_analysis}

Evidence evaluation:

{evidence_result}

User history:

{history_result}

Rules:

Images are the primary truth.

History cannot override
clear image evidence.

Allowed claim_status:

supported
contradicted
not_enough_information

Return JSON only.
"""

    response = decision_llm.invoke(
        prompt
    )

    return response.model_dump()