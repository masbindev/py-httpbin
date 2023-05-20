from fastapi import FastAPI, Request
from logging_request import log_request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
import os

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

@app.get("/logs")
async def logs(request: Request):
    log_dir = "logs"
    log_files = []
    for filename in os.listdir(log_dir):
        if filename.endswith(".csv") or filename.endswith(".txt"):
            log_files.append(filename)
    # get unique log file dates
    log_file_dates = list(set([filename.split(".")[0] for filename in log_files]))
    return templates.TemplateResponse("logs.html", {"request": request, "log_files": log_files, "log_file_dates": log_file_dates})

@app.get("/logs/{filename}")
async def download_log(filename: str):
    log_dir = "logs"
    file_path = os.path.join(log_dir, filename)
    return FileResponse(file_path, media_type="text/csv" if filename.endswith(".csv") else "text/plain", filename=filename)