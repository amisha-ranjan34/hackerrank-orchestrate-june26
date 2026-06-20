from io import BytesIO
import base64
import pillow_avif  # registers AVIF format with Pillow
from PIL import Image


def image_to_base64_jpeg(path):
    """
    Open any image and re-save it as a clean JPEG.
    Returns a base64 string.
    """

    img = Image.open(path)

    # convert RGBA, P, etc. to RGB
    img = img.convert("RGB")

    buffer = BytesIO()

    img.save(
        buffer,
        format="JPEG",
        quality=95
    )

    jpeg_bytes = buffer.getvalue()

    return base64.b64encode(
        jpeg_bytes
    ).decode()