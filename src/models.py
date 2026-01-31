from pydantic import BaseModel, Field
from typing import List


class AnalyzeRequest(BaseModel):
    """Modèle de requête pour l'endpoint /analyze."""
    x: List = Field(..., description="Première série numérique")
    y: List = Field(..., description="Deuxième série numérique")


class AnalyzeResponse(BaseModel):
    """Modèle de réponse pour l'endpoint /analyze."""
    mean_x: float = Field(..., description="Moyenne de la série x")
    mean_y: float = Field(..., description="Moyenne de la série y")
    correlation: float = Field(..., description="Coefficient de corrélation de Pearson")
