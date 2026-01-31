import utils.session
from fastapi import FastAPI

from src.routes import router


app = FastAPI(
    title="API d'analyse statistique",
    description="API REST pour calculer des indicateurs statistiques sur deux séries numériques",
    version="1.0.0",
)

app.include_router(router)
