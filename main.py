from fastapi import FastAPI

app = FastAPI()


@app.put("/")
async def open_shutters():
    pass
