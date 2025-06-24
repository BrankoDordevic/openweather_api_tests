from open_weather import get_weather

def test_get_weather_in_city():
    response = get_weather("Utrecht")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Provincie Utrecht"

def test_invalid_city_name():
    response = get_weather("Beginhoven")
    assert response.status_code == 404
    assert "city not found" in response.text