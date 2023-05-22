
## About this repo
My approach to learn python bu building a simple httpbin.org clone (oversimplified of course)

## tech stack
- python 3.10
- FastAPI
- uvicorn
- docker
- docker-compose

## How to run
- `docker-compose up --build`
- `docker-compose up --build -d` (detached mode)

## features
- [x] / --> view all of your http request (headers, body, etc)
- [x] /ip --> view your ip
- [x] /logs --> view all logs (it is saved on ./logs by default)

