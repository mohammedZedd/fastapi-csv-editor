from pydantic import BaseModel
from typing import List, Dict

class ColumnRequest(BaseModel):
    selected_columns: List[str]
    new_columns: Dict[str, List[str]]
