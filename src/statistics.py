"""Module de calculs statistiques."""
from typing import List, Any
import numpy as np


class StatisticsError(Exception):
    """Exception personnalisée pour les erreurs statistiques."""
    pass


def calculate_mean(values: List[float]) -> float:
    """
    Calcule la moyenne d'une liste de valeurs.
    
    Args:
        values: Liste de valeurs numériques
        
    Returns:
        La moyenne des valeurs
        
    Raises:
        StatisticsError: Si la liste est vide
    """
    if not values:
        raise StatisticsError("La liste ne peut pas être vide")
    
    arr = np.array(values)
    return float(np.mean(arr))


def calculate_correlation(x: List[float], y: List[float]) -> float:
    """
    Calcule le coefficient de corrélation de Pearson entre deux séries.
    
    Args:
        x: Première série de valeurs
        y: Deuxième série de valeurs
        
    Returns:
        Le coefficient de corrélation de Pearson (entre -1 et 1)
        
    Raises:
        StatisticsError: Si les listes ont des longueurs différentes ou sont vides
    """
    if len(x) != len(y):
        raise StatisticsError(
            f"Les séries doivent avoir la même longueur. "
            f"Longueur de x: {len(x)}, longueur de y: {len(y)}"
        )
    
    if not x or not y:
        raise StatisticsError("Les séries ne peuvent pas être vides")
    
    # Conversion en arrays numpy pour les calculs vectoriels
    x_arr = np.array(x, dtype=float)
    y_arr = np.array(y, dtype=float)
    
    # Calcul des moyennes
    mean_x = float(np.mean(x_arr))
    mean_y = float(np.mean(y_arr))
    
    # Calcul du numérateur
    numerator = float(np.sum((x_arr - mean_x) * (y_arr - mean_y)))
    
    # Calcul des dénominateurs
    sum_sq_diff_x = float(np.sum((x_arr - mean_x) ** 2))
    sum_sq_diff_y = float(np.sum((y_arr - mean_y) ** 2))
    
    # Calcul du dénominateur
    denominator = float(np.sqrt(sum_sq_diff_x * sum_sq_diff_y))
    
    # Gestion du cas où le dénominateur est zéro (écart-type nul)
    if denominator == 0:
        return 0.0
    
    return numerator / denominator


def validate_numeric_series(values: Any, series_name: str) -> List[float]:
    """
    Valide et convertit une série en liste de flottants.
    
    Args:
        values: Liste de valeurs à valider
        series_name: Nom de la série (pour les messages d'erreur)
        
    Returns:
        Liste de flottants
        
    Raises:
        StatisticsError: Si une valeur n'est pas numérique
    """
    if not isinstance(values, list):
        raise StatisticsError(f"{series_name} doit être une liste")
    
    converted = []
    for i, value in enumerate(values):
        try:
            float_value = float(value)
            converted.append(float_value)
        except (ValueError, TypeError):
            raise StatisticsError(
                f"{series_name}[{i}] = {value} n'est pas une valeur numérique"
            )
    
    return converted
