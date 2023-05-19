from fastapi import FastAPI, Request
from logging_request import log_request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
@app.post("/")
async def read_root(request: Request):
    headers = dict(request.headers)
    body = await request.body()
    await log_request(request, "./logs")
    response = {"headers": headers, "body": body.decode()}
    return templates.TemplateResponse("response.html", {"request": request, "response": response})