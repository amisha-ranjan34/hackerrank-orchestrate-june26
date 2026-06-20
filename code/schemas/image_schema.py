from pydantic import BaseModel

class ImageAnalysis(BaseModel):

    visible_issue: str

    object_part: str

    severity: str

    image_quality_flags: list[str]

    supporting_image_ids: list[str]