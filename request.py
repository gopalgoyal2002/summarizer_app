import string
from typing import Any, Collection, Dict, List, Optional, Union, Literal

from pydantic import BaseModel
from fastapi import Form

class Summaryrequest(BaseModel):
    text: str
    minL: int
    maxL: int