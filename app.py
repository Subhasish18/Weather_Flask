from flask import Flask, render_template, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

API_KEY = "2564e4bcb0096805ef5127ba6db26fd4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def index():
    return render_template('weather.html')

@app.route('/api/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter required"}), 400

    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}  
        r = requests.get(BASE_URL, params=params)
        data = r.json()

        if data.get("cod") != 200:
            return jsonify({"error": data.get("message", "City not found")}), 404

        weather_info = {
            "name": data["name"],
            "country": data["sys"]["country"],
            "temp_c": data["main"]["temp"],
            "feels_like_c": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "humidity": data["main"]["humidity"],
            "wind_kph": round(data["wind"]["speed"] * 3.6, 2),
            "pressure": data["main"]["pressure"],
            "visibility": data.get("visibility", 0),
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"]
        }

        return jsonify(weather_info)
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
