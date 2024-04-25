"""
hello_fastapi
Introduction to FastAPI
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <head>
      <title>Rico's boring website</title>
    </head>
    <body>
      <h1>Welcome to Rico's website</h1> 
      <p>We are learning about FastAPI today</p>
      <h2>This is an h2 topic</h2>
      <p>Content</p>
    </body>
    """
if __name__ == "__main__":
    uvicorn.run(app, port=8001)