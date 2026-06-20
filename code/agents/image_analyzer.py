# agents/image_analyzer.py

import base64
from PIL import Image
from openai import OpenAI

from schemas.image_schema import ImageAnalysis
from config import GPT_MODEL
from utils.image_convertor import image_to_base64_jpeg

client = OpenAI()


def validate_image(path):
    """
    Check whether image is readable.
    """

    try:
        img = Image.open(path)
        img.verify()

        return True

    except Exception as e:

        print(f"Invalid image skipped: {path}")
        print(e)

        return False


def encode_image(path):

    image_b64 = image_to_base64_jpeg(path)

    return image_b64, "image/jpeg"


def analyze_images(
        image_paths,
        claim_object,
        parsed_claim
):
    """
    Analyze one or more images using GPT Vision.
    """

    content = [

        {
            "type": "input_text",

            "text": f"""
You are an insurance damage analyst.

Object type:
{claim_object}

Parsed claim:
{parsed_claim}

Determine:

1. visible_issue
2. object_part
3. severity
4. image_quality_flags
5. supporting_image_ids

Images are the PRIMARY source of truth.

Return JSON only.
"""
        }

    ]

    valid_image_count = 0

    for path in image_paths:

        if not validate_image(path):
            continue

        image_b64, mime_type = encode_image(path)

        print(f"Processing: {path}")
        print(f"MIME type: {mime_type}")

        content.append(

            {
                "type": "input_image",

                "image_url":
                    f"data:{mime_type};base64,{image_b64}"
            }

        )

        valid_image_count += 1

    # No valid images found
    if valid_image_count == 0:

        return {

            "visible_issue": "unknown",

            "object_part": "unknown",

            "severity": "unknown",

            "image_quality_flags": [

                "damage_not_visible"

            ],

            "supporting_image_ids": []
        }

    response = client.responses.parse(

        model=GPT_MODEL,

        input=[

            {

                "role": "user",

                "content": content

            }

        ],

        text_format=ImageAnalysis

    )

    return response.output_parsed.model_dump()