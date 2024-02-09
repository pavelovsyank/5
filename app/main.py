from fastapi import FastAPI, Request

app = FastAPI()

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

dir_static = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

dir_templates = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
print(f"dir static = {dir_static}")
print(f"dir templates = {dir_templates}")

app.mount("/static", StaticFiles(directory=dir_static), name="static")


templates = Jinja2Templates(directory=dir_templates)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="root.html"
    )