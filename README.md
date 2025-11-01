# Weather Flask App

A simple, minimal, and responsive single-page weather application. The backend is built with Python and Flask, which serves a frontend built with vanilla HTML, CSS, and JavaScript. It fetches and displays real-time weather data from the OpenWeatherMap API.

 
<img width="1608" height="682" alt="image" src="https://github.com/user-attachments/assets/ce523c6e-ce5d-4541-8dd8-f1958e635920" />


## Features

*   **Real-time Weather:** Get current weather information for any city.
*   **Detailed Information:** Displays temperature, "feels like" temperature, humidity, wind speed, pressure, visibility, sunrise, and sunset times.
*   **Clean UI:** A modern, dark-themed, and responsive user interface that looks great on both desktop and mobile.
*   **Auto-Refresh:** Automatically updates the weather data for the current city every 3 minutes.
*   **Simple Backend:** A lightweight Flask API acts as a proxy to the OpenWeatherMap service, keeping the API key secure and simplifying the data for the frontend.

## Tech Stack

*   **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-CORS
*   **Frontend:** HTML, CSS, JavaScript (no frameworks)
*   **Database:** SQLite
*   **API:** [OpenWeatherMap API](https://openweathermap.org/api)

## Project Structure

```
Weather_Flask/
├── app.py                  # The main Flask application and API logic
├── templates/
│   └── weather.html        # The single-page HTML file for the UI
├── weather.db              # SQLite database file (auto-generated)
└── README.md               # This file
```

## Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Weather_Flask
```

### 2. Create a Virtual Environment

It's a best practice to use a virtual environment for Python projects.

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Create a `requirements.txt` file in the project root with the following content:

```txt
Flask
Flask-SQLAlchemy
Flask-Cors
requests
```

Then, install the packages:

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key

The application uses an API key from OpenWeatherMap. While the key is currently hardcoded in `app.py`, the recommended approach is to use an environment variable.

Get your free API key from OpenWeatherMap. Then, you can either replace the hardcoded key in `app.py` or (preferably) set it as an environment variable and modify the code to read it.

### 5. Run the Application

```bash
python app.py
```

The application will start and be accessible at `http://127.0.0.1:5000` in your web browser.

