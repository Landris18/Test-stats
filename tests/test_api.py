from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


class TestAnalyzeEndpoint:
    """Tests pour l'endpoint POST /analyze."""
    
    def test_analyze_nominal(self):
        """Test cas nominal."""
        response = client.post(
            "/analyze",
            json={
                "x": [1, 2, 3, 4, 5],
                "y": [2, 4, 5, 4, 5]
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert abs(data["mean_x"] - 3.0) < 0.0001
        assert abs(data["mean_y"] - 4.0) < 0.0001
        assert abs(data["correlation"] - 0.7746) < 0.0001
    
    def test_analyze_perfect_correlation(self):
        """Test corrélation parfaite."""
        response = client.post(
            "/analyze",
            json={
                "x": [1, 2, 3, 4, 5],
                "y": [2, 4, 6, 8, 10]
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert abs(data["correlation"] - 1.0) < 0.0001
    
    def test_analyze_different_lengths(self):
        """Test avec longueurs différentes."""
        response = client.post(
            "/analyze",
            json={
                "x": [1, 2, 3],
                "y": [1, 2]
            }
        )
        assert response.status_code == 400
        assert "même longueur" in response.json()["detail"]
    
    def test_analyze_empty_lists(self):
        """Test avec listes vides."""
        response = client.post(
            "/analyze",
            json={
                "x": [],
                "y": []
            }
        )
        assert response.status_code == 400
        assert "vides" in response.json()["detail"]
    
    def test_analyze_one_empty_list(self):
        """Test avec une liste vide."""
        response = client.post(
            "/analyze",
            json={
                "x": [1, 2, 3],
                "y": []
            }
        )
        assert response.status_code == 400
    
    def test_analyze_non_numeric_values(self):
        """Test avec valeurs non numériques."""
        response = client.post(
            "/analyze",
            json={
                "x": [1, 2, "abc", 4],
                "y": [1, 2, 3, 4]
            }
        )
        assert response.status_code == 400
        assert "numérique" in response.json()["detail"]
    
    def test_analyze_string_numbers(self):
        """Test avec nombres en string (devrait fonctionner)."""
        response = client.post(
            "/analyze",
            json={
                "x": ["1", "2", "3"],
                "y": ["2", "4", "6"]
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert abs(data["mean_x"] - 2.0) < 0.0001
        assert abs(data["mean_y"] - 4.0) < 0.0001
    
    def test_analyze_negative_values(self):
        """Test avec valeurs négatives."""
        response = client.post(
            "/analyze",
            json={
                "x": [-1, -2, -3],
                "y": [-2, -4, -6]
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert abs(data["mean_x"] - (-2.0)) < 0.0001
        assert abs(data["mean_y"] - (-4.0)) < 0.0001


class TestRootEndpoint:
    """Tests pour l'endpoint racine."""
    
    def test_root(self):
        """Test endpoint racine."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
