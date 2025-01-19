from pydantic import BaseModel
from typing import Optional

class DataResponse(BaseModel):
    data: Optional[dict]
    message: str
