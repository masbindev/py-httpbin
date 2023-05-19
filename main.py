from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
@app.post("/")
async def read_root(request: Request):
    headers = dict(request.headers)
    body = await request.body()
    return {"headers": headers, "body": body.decode()}