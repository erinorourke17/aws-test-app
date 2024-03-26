from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Third time's the charm: validating this pipeline"}