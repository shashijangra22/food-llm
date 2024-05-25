from models.Request import Request
from services.RecommendationService import Foody
from fastapi import FastAPI

app = FastAPI()
foody = Foody()


@app.post("/recommendations")
def get_recommendations(req: Request):
    res, error = foody.get_recommendations(req)
    return {"recommendations": res, "error": error}
