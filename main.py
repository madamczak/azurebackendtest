from fastapi import FastAPI

app = FastAPI()


@app.get("/getmsg")
async def root():
    return {"message": "Hello World"}
