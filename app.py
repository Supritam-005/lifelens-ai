from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    income: int
    state: str

# Dummy schemes database
schemes = [
    {
        "name": "PM Scholarship",
        "min_income": 0,
        "max_income": 500000,
        "state": "West Bengal",
        "description": "Financial support for students."
    },
    {
        "name": "MSME Subsidy",
        "min_income": 0,
        "max_income": 1000000,
        "state": "West Bengal",
        "description": "Support for small businesses."
    }
]

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/check")
async def check_scheme(user: UserInput):
    eligible = []

    for scheme in schemes:
        if (
            user.income >= scheme["min_income"]
            and user.income <= scheme["max_income"]
            and user.state.lower() == scheme["state"].lower()
        ):
            eligible.append(scheme)

    return {"eligible_schemes": eligible}
