from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def root():
    return {"message": "Beep boop, I am a test API!"}