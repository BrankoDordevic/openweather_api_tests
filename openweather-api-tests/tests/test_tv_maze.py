from tv_maze import search_show_by_name, get_show_by_id

def test_breaking_bad_show_url_contains_id():
    search_response = search_show_by_name("breaking bad")
    assert search_response.status_code == 200

    data = search_response.json()
    assert len(data) > 0

    show_id = data[0]["show"]["id"]
    
    show_response = get_show_by_id(show_id)
    assert show_response.status_code == 200

    show_data = show_response.json()
    assert "url" in show_data
    assert str(show_id) in show_data["url"]