from open_weather import get_weather

def test_authorised():
    response = get_weather("Utrecht")
    assert response.status_code == 200
    assert "Provincie Utrecht" in response.text

def test_not_authorised():
    response = get_weather("Utrecht", "")
    assert response.status_code == 401
    assert "Invalid API key" in response.text
