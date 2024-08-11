import sys
sys.path.insert(0, 'C:\\Users\\TUF_12500H\\Desktop\\LawDiff\\applied')

from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from scr.retrieve import retrieve
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/retrieve")
async def query(message: str):
    response = retrieve(message)
    response_content = {
        "query": message,
        "documents": [i['docs'] for i in response],
        "answer": [i['context'] for i in response]
    }
    return JSONResponse(content=response_content, status_code=200)
