from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "b48d512235d695068e4c0eb340e256c7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_forecast(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    r = requests.get(FORECAST_URL, params=params)
    if r.status_code == 200:
        data = r.json()
        daily = {}
        for entry in data["list"]:
            date = datetime.fromtimestamp(entry["dt"]).strftime("%Y-%m-%d")
            temp_min = entry["main"]["temp_min"]
            temp_max = entry["main"]["temp_max"]
            desc = entry["weather"][0]["description"]
            icon = entry["weather"][0]["icon"]

            if date not in daily:
                daily[date] = {
                    "temp_min": temp_min,
                    "temp_max": temp_max,
                    "description": desc,
                    "icon": icon,
                }
            else:
                daily[date]["temp_min"] = min(daily[date]["temp_min"], temp_min)
                daily[date]["temp_max"] = max(daily[date]["temp_max"], temp_max)

        forecast = []
        for date, vals in list(daily.items())[:7]:
            forecast.append({
                "date": datetime.strptime(date, "%Y-%m-%d").strftime("%a, %d %b"),
                "temp_min": round(vals["temp_min"]),
                "temp_max": round(vals["temp_max"]),
                "description": vals["description"],
                "icon": vals["icon"],
            })
        return forecast
    return []


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    forecast = []
    if request.method == "POST":
        city = request.form["city"]
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temperature": round(data["main"]["temp"]),
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "country": data["sys"]["country"],
                "condition": data["weather"][0]["main"].lower(),
                "is_day": data["weather"][0]["icon"].endswith("d"),
                "wind": data["wind"]["speed"],
            }
            forecast = get_forecast(city)
    return render_template("index.html", weather=weather, forecast=forecast)


@app.route("/suggest")
def suggest():
    query = request.args.get("q", "")
    if not query:
        return jsonify([])
    params = {"q": query, "limit": 5, "appid": API_KEY}
    r = requests.get(GEO_URL, params=params)
    if r.status_code == 200:
        data = r.json()
        suggestions = [
            f"{item['name']}, {item.get('state','')}, {item['country']}".strip(", ")
            for item in data
        ]
        return jsonify(suggestions)
    return jsonify([])


@app.route("/weather_by_coords")
def weather_by_coords():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if not lat or not lon:
        return jsonify({"error": "Missing coordinates"}), 400

    params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": round(data["main"]["temp"]),
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "country": data["sys"]["country"],
            "condition": data["weather"][0]["main"].lower(),
            "is_day": data["weather"][0]["icon"].endswith("d"),
            "wind": data["wind"]["speed"],
        }
        return jsonify(weather)
    return jsonify({"error": "Failed to fetch weather"}), 500


if __name__ == "__main__":
    app.run(debug=True)
