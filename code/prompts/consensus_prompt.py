CONSENSUS_PROMPT = """
Images dominate.

User history only contributes risk.

Allowed claim_status:

supported
contradicted
not_enough_information

If damage is visible and agrees with user claim:

supported

If damage is absent and relevant area is visible:

contradicted

If image quality prevents judgement:

not_enough_information

Return JSON only.
"""