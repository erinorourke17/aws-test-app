from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def root():
    return {"message": "Test 1 2 3 4 5"}