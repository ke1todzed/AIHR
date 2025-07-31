import uvicorn
from app.API import api
from fastapi import FastAPI

app = FastAPI()

app.include_router(api.router)


if __name__ == "__main__":
    uvicorn.run(app)