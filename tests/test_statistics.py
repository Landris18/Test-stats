import pytest
from src.statistics import (
    calculate_mean,
    calculate_correlation,
    validate_numeric_series,
    StatisticsError,
)


class TestCalculateMean:
    """Tests pour la fonction calculate_mean."""
    
    def test_mean_nominal(self):
        """Test cas nominal."""
        values = [1.0, 2.0, 3.0, 4.0, 5.0]
        assert calculate_mean(values) == 3.0
    
    def test_mean_negative_values(self):
        """Test avec valeurs négatives."""
        values = [-1.0, -2.0, -3.0]
        assert calculate_mean(values) == -2.0
    
    def test_mean_single_value(self):
        """Test avec une seule valeur."""
        values = [5.0]
        assert calculate_mean(values) == 5.0
    
    def test_mean_empty_list(self):
        """Test avec liste vide."""
        with pytest.raises(StatisticsError, match="ne peut pas être vide"):
            calculate_mean([])


class TestCalculateCorrelation:
    """Tests pour la fonction calculate_correlation."""
    
    def test_correlation_nominal(self):
        """Test cas nominal."""
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        y = [2.0, 4.0, 5.0, 4.0, 5.0]
        result = calculate_correlation(x, y)
        assert abs(result - 0.7746) < 0.0001
    
    def test_correlation_perfect_positive(self):
        """Test corrélation parfaite positive."""
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        y = [2.0, 4.0, 6.0, 8.0, 10.0]
        result = calculate_correlation(x, y)
        assert abs(result - 1.0) < 0.0001
    
    def test_correlation_perfect_negative(self):
        """Test corrélation parfaite négative."""
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        y = [10.0, 8.0, 6.0, 4.0, 2.0]
        result = calculate_correlation(x, y)
        assert abs(result - (-1.0)) < 0.0001
    
    def test_correlation_no_correlation(self):
        """Test absence de corrélation."""
        x = [1.0, 2.0, 3.0, 4.0, 5.0]
        y = [5.0, 5.0, 5.0, 5.0, 5.0]
        result = calculate_correlation(x, y)
        assert abs(result - 0.0) < 0.0001
    
    def test_correlation_different_lengths(self):
        """Test avec longueurs différentes."""
        x = [1.0, 2.0, 3.0]
        y = [1.0, 2.0]
        with pytest.raises(StatisticsError, match="même longueur"):
            calculate_correlation(x, y)
    
    def test_correlation_empty_lists(self):
        """Test avec listes vides."""
        with pytest.raises(StatisticsError, match="ne peuvent pas être vides"):
            calculate_correlation([], [])
    
    def test_correlation_one_empty_list(self):
        """Test avec une liste vide."""
        with pytest.raises(StatisticsError):
            calculate_correlation([1.0, 2.0], [])


class TestValidateNumericSeries:
    """Tests pour la fonction validate_numeric_series."""
    
    def test_validate_nominal(self):
        """Test cas nominal."""
        values = [1, 2, 3.5, 4]
        result = validate_numeric_series(values, "x")
        assert result == [1.0, 2.0, 3.5, 4.0]
    
    def test_validate_string_numbers(self):
        """Test avec nombres en string."""
        values = ["1", "2.5", "3"]
        result = validate_numeric_series(values, "x")
        assert result == [1.0, 2.5, 3.0]
    
    def test_validate_non_numeric(self):
        """Test avec valeur non numérique."""
        values = [1, 2, "abc", 4]
        with pytest.raises(StatisticsError, match="n'est pas une valeur numérique"):
            validate_numeric_series(values, "x")
    
    def test_validate_not_list(self):
        """Test avec type non liste."""
        with pytest.raises(StatisticsError, match="doit être une liste"):
            validate_numeric_series("not a list", "x")
