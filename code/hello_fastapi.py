"""
hello_fastapi

Introduction to FastAPI
"""
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"developer_name": "rico"}

if __name__ == "__main__":
    uvicorn.run(app)