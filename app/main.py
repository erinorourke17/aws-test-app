from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def root():
    return {"message": "I am not a robot"}