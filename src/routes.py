from fastapi import APIRouter, HTTPException

from src.statistics import (
    calculate_mean,
    calculate_correlation,
    validate_numeric_series,
    StatisticsError,
)
from src.models import AnalyzeRequest, AnalyzeResponse


router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    """
    Calcule des indicateurs statistiques sur deux séries numériques.
    
    Args:
        request: Requête contenant les séries x et y
        
    Returns:
        Réponse contenant les moyennes et la corrélation
        
    Raises:
        HTTPException: En cas d'erreur de validation ou de calcul
    """
    try:
        # Validation et conversion des séries
        x_validated = validate_numeric_series(request.x, "x")
        y_validated = validate_numeric_series(request.y, "y")
        
        # Vérification des longueurs
        if len(x_validated) != len(y_validated):
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Les séries doivent avoir la même longueur. "
                    f"Longueur de x: {len(x_validated)}, longueur de y: {len(y_validated)}"
                )
            )
        
        # Vérification des listes vides
        if not x_validated or not y_validated:
            raise HTTPException(
                status_code=400,
                detail="Les séries ne peuvent pas être vides"
            )
        
        # Calculs statistiques
        mean_x = calculate_mean(x_validated)
        mean_y = calculate_mean(y_validated)
        correlation = calculate_correlation(x_validated, y_validated)
        
        return AnalyzeResponse(
            mean_x=mean_x,
            mean_y=mean_y,
            correlation=round(correlation, 4)
        )
        
    except HTTPException:
        raise
    except StatisticsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur interne du serveur: {str(e)}"
        )


@router.get("/")
async def root():
    """Endpoint racine."""
    return {
        "message": "API d'analyse statistique",
        "version": "1.0.0",
        "endpoints": {
            "POST /analyze": "Calcule des indicateurs statistiques sur deux séries numériques"
        }
    }
