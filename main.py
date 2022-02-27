''' Import library '''
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

''' Class Item Model '''
class Item(BaseModel):
    pretest: int
    anatomi_telinga: int
    posttest: int


# Inisiasi router
app = FastAPI()


@app.post('/progress')
async def create(item: Item):
    # Mendapatkan input data
    pretest = item.pretest
    anatomi_telinga = item.anatomi_telinga
    posttest = item.posttest

    return item
