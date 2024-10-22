from typing import List

from pydantic import BaseModel


class ProcessItem(BaseModel):
    urls: List[str]
