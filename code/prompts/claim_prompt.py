CLAIM_PROMPT = """
Extract:

1. issue_type
2. object_part
3. claim_summary

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
none
unknown

Return JSON.
"""