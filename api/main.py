from mangum import Mangum
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def sanity_check():
    return "Serverless FastAPI running!"


handler = Mangum(app, lifespan='off')