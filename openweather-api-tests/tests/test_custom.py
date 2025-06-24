import json
from open_weather import get_weather

def test_invalid_request():
    response = get_weather(None)
    assert response.status_code == 400
    assert "Nothing to geocode" in response.text

def test_security_headers_present():
    response = get_weather("Rotterdam")
    headers = response.headers

    assert "Content-Type" in headers
    assert headers["Content-Type"] == "application/json; charset=utf-8"

def test_coordinates_for_city():
    response = get_weather("Rotterdam")
    data = response.json()
    
    lat = data.get("coord", {}).get("lat")
    lon = data.get("coord", {}).get("lon")

    assert lat and lon, "Latitude en longitude mogen niet leeg zijn"
    assert isinstance(lat, (int, float)), "Latitude moet een getal zijn"
    assert isinstance(lon, (int, float)), "Longitude moet een getal zijn"
    assert -90 <= lat <= 90, "Latitude buiten bereik"
    assert -180 <= lon <= 180, "Longitude buiten bereik"

def test_valid_temperature():
    response = get_weather("Rotterdam")
    data = response.json()

    assert response.status_code == 200
    assert "main" in data
    assert "temp" in data["main"]
    assert isinstance(data["main"]["temp"], (int, float))