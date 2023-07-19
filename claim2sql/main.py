from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/fact-check", response_class=HTMLResponse)
async def read_page1(request: Request):
    return templates.TemplateResponse("fact-check.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit_text(request: Request):
    form_data = await request.body()
    data = json.loads(form_data)

    user_input = data.get("text")

    model_outputs = {
        "input_sentence":"Joe Biden voted for the Iraq War.",
        "frame":"Vote",
        "target":"Voted",
        "frame_elements":{
            "Agent":{"start":0, "end":9},
            "Issue":{"start":20, "end":32},
            "Position":{"start":16, "end":19}
        },
        "bill_title":"Iraq War Resolution",
        "bill_id":"hjres114-107",
        "congress_member":"Joe Biden",
        "member_id":"B000444"
    }

    return templates.TemplateResponse("results.html", {"request": request, "model_outputs": model_outputs})
