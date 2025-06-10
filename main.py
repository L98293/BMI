from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Form
from fastapi import FastAPI
from starlette.responses import HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("Main.html", {"request": request})

@app.post("/bmi")
async def calculate_bmi(
        height: float = Form(...),
        weight: float = Form(...),
):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return JSONResponse({"bmi": round(bmi, 2)}) # round는 특정 자릿수 까지 반올림

app.mount("/static", StaticFiles(directory="static"), name="static")
