from config import DATASET_DIR
from openai import OpenAI
from utils.image_convertor import image_to_base64_jpeg

client = OpenAI()

path = DATASET_DIR / "images" / "test" / "case_001" / "img_1.jpg"

# Convert AVIF/any format to clean JPEG base64
image_b64 = image_to_base64_jpeg(path)

response = client.responses.create(

    model="gpt-4.1-mini",

    input=[

        {

            "role": "user",

            "content": [

                {
                    "type": "input_text",

                    "text": "What is in this image?"
                },

                {
                    "type": "input_image",

                    "image_url":
                        f"data:image/jpeg;base64,{image_b64}"
                }

            ]

        }

    ]

)

print(response.output_text)