from fastapi import APIRouter, Query, Depends, Response
from huggingface import summrizer
from request import Summaryrequest
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.post("/summarizer")
async def summarizer(request:Summaryrequest):
    return {"summarizer":summrizer(text=request.text,minlen=request.minL,maxlen=request.maxL)}
