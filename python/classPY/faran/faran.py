
from fastapi import FastAPI

app = FastAPI()


@app.get('/faran')
def faran():
    return {"name":"zia"}
