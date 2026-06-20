# utils/json_parser.py

import json


def safe_json_parse(text):

    try:
        return json.loads(text)

    except Exception:

        try:

            text = text.replace(
                "```json",
                ""
            )

            text = text.replace(
                "```",
                ""
            )

            return json.loads(text)

        except Exception:

            return {}