from pydantic import BaseModel
from typing import Annotated
from pydantic import StringConstraints

class SectorInput(BaseModel):
    sector: Annotated[
        str,
        StringConstraints(min_length=2, max_length=30, pattern="^[a-zA-Z]+$")
    ]