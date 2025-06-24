import requests

BASE_URL = "https://api.tvmaze.com"

def search_show_by_name(name) -> requests.Response:
    """
    Search for a TV show by its name.
    Args:
        name (str): The name of the TV show to search for.
    """
    response = requests.get(f"{BASE_URL}/search/shows", params={"q": name})
    return response

def get_show_by_id(show_id) -> requests.Response:
    """
    Fetch a TV show by its ID.
    Args:
        show_id (int): The ID of the show to fetch.
    Returns:
        requests.Response: The HTTP response object.
    """
    response = requests.get(f"{BASE_URL}/shows/{show_id}")
    return response