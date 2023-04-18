from fastapi import FastAPI
from routes.api import api


app = FastAPI(
    title="Web Scrappy from Senahmi and Mongodb",
    description="This API get 'pronostico del tiempo' from Senahmi"
)
app.include_router(api)


@app.get("/")
async def root():
    return {"message": "Hello IsacDann"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
