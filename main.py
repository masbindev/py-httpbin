from fastapi import FastAPI, Request
from logging_request import log_request

app = FastAPI()

@app.get("/")
@app.post("/")
async def read_root(request: Request):
    headers = dict(request.headers)
    body = await request.body()
    await log_request(request, "./logs")
    return {"headers": headers, "body": body.decode()}