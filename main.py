from fastapi import FastAPI

app = FastAPI()

politicians = {
    "rfk": {
        "name": "Robert F. Kennedy Jr.",
        "party": "Independent",
        "website": "https://www.kennedy24.com/",
        "issues": {
            "vaccines": "Opposes mandates, promotes individual choice",
            "environment": "Supports clean energy, concerned about pollution",
            "covid": "Criticizes mainstream pandemic response"
        }
    },
    "biden": {
        "name": "Joe Biden",
        "party": "Democratic",
        "website": "https://joebiden.com/",
        "issues": {
            "vaccines": "Supports vaccine mandates in certain cases",
            "environment": "Rejoined the Paris Climate Accord",
            "covid": "Led federal response with mandates and funding"
        }
    }
}

@app.get("/politician/{name}")
def get_politician(name: str):
    return politicians.get(name.lower(), {"error": f"No data found for politician '{name}'"})