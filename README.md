# OpenWeather & TV Maze API Tests

This project contains Python code and automated tests for interacting with the [OpenWeather API](https://openweathermap.org/api) and the [TV Maze API](https://www.tvmaze.com/api).

## Features

- Fetch current weather data for a city using OpenWeather API
- Search for TV shows and fetch show details using TV Maze API
- Automated tests with pytest, including:
  - Parameterized tests
  - Custom assertions for API responses
  - Mocking of HTTP requests for reliable test results

## Project Structure

```
openweather-api-tests/
├── open_weather.py         # OpenWeather API wrapper
├── tv_maze.py              # TV Maze API wrapper
├── tests/
│   ├── test_custom.py      # Custom tests for OpenWeather
│   ├── test_parametrize.py # Parameterized tests
│   ├── test_tv_maze.py     # TV Maze API tests
│   └── conftest.py         # Pytest fixtures and mocks
├── .env                    # Environment variables (API keys)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Setup

1. **Clone the repository**

   ```sh
   <!-- TODO: update rpo-url when uploaded to GitHub -->
   git clone <your-repo-url> 
   cd openweather-api-tests
   ```

2. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:

   ```
   APP_ID=your_openweather_api_key
   ```

## Creating a Virtual Environment

It is recommended to use a virtual environment for dependency management.

Create and activate a virtual environment:

```sh
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

## Running Tests

Run all tests with:

```sh
pytest
```

## Notes

- Tests use real API calls by default. For isolated testing, add fixtures in a file called `conftest.py` for mocked HTTP requests.
- Make sure to keep your API keys secure and **never commit them to version control**.

---
