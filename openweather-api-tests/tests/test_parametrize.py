import pytest
from open_weather import get_weather

test_city_ids = [
    ("Amsterdam", 2759794),
    ("Rotterdam", 2747891),
    ("Den Haag", 2747373),
    ("Groningen", 2755249)
]

@pytest.mark.parametrize("city,expected_id", test_city_ids)
def test_city_ids(city, expected_id):
    response = get_weather(city)
    
    assert response.status_code == 200
    assert response.json()["id"] == expected_id
