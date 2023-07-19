from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import wikipediaapi

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

wiki = wikipediaapi.Wikipedia('idir_lab', 'en')

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
        "bills":[
            {
                "bill_title":"Iraq War Resolution",
                "bill_id":"hjres114-107",
                "bill_summary":"A joint resolution to authorize the use of United States Armed Forces against Iraq."
            }, 
            {
                "bill_title":"Gun Control Act",
                "bill_id":"hjres114-110",
                "bill_summary":"A bill to restrict the use of guns in the United States."
            },
            {
                "bill_title":"Abortion Act",
                "bill_id":"hjres114-130",
                "bill_summary":"A bill to allow the use of abortion in the United States."
            }
        ],
        "congress_member":"Joe Biden",
        "member_id":"B000444"
    }


    fe_definitions = {
        "Agent": "The conscious entity, generally a person, that performs the voting decision on an Issue.",
        "Issue": "The matter which the Agent has a positive or negative opinion about and either votes for or votes against.",
        "Side": "The conscious entity, generally a person, that performs the voting decision on an Issue together with the Agent.",
        "Position": "This FE identifies the position that the Agent takes on an Issue. The Agent either votes for or against.",
        "Frequency": "The number of times that the Agent made the same voting decision on an Issue.",
        "Time": "This FE identifies the time when the Agent performs the voting decision.",
        "Place": "The location where the voting decision took place.",
        "Support_rate": "The percentage of Agent's total votes, in which the Agent took the same position with a Side for a specific period of time."
    }



    # Build html for frame elements
    prev_end = 0
    fe_html = ""
    for fe, span in sorted(model_outputs["frame_elements"].items(), key=lambda x: x[1]['start']):
        if prev_end != span['start']:
            fe_html += f"<span class='non-fe'>{model_outputs['input_sentence'][prev_end:span['start']]}</span>"
        fe_html += f"<span data-content='{fe_definitions[fe]}' class='fe-{fe.lower()}'>{model_outputs['input_sentence'][span['start']:span['end']]}</span>"

        prev_end = span['end']
    fe_html += f"<span>{model_outputs['input_sentence'][prev_end:]}</span>"



    # Get agent wikipedia page
    agent_page = wiki.page(model_outputs["congress_member"])
    agent_summary = agent_page.summary.split("\n")[0]

    agent_url = agent_page.fullurl

    return templates.TemplateResponse("results.html", {"request": request, "model_outputs": model_outputs, "agent_summary": agent_summary, "agent_url": agent_url, "fe_html": fe_html})
