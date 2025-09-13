# 🌦 Weather App (Flask + OpenWeather API)

A simple **Flask-based Weather Web App** that shows real-time weather and a 7-day forecast using the [OpenWeather API](https://openweathermap.org/api).

---

## 🚀 Features

- 🔍 Search weather by **city name**
- 📝 **Auto-suggest cities** while typing
- 📍 Get weather using your **GPS location**
- 🌡️ Show **temperature, wind speed, and conditions**
- 📅 Display a **7-day forecast with icons**
- 🎨 Clean, responsive UI

---

## 🛠️ Requirements

- Python 3.8+
- Flask
- Requests

Install dependencies:

```bash
pip install -r requirements.txt
🔑 Setup OpenWeather API Key
Sign up at OpenWeather and get your API key

Set the key as an environment variable:

Linux / macOS
bash
Copy code
export OPENWEATHER_API_KEY="your_api_key_here"
Windows (PowerShell)
powershell
Copy code
setx OPENWEATHER_API_KEY "your_api_key_here"
⚠️ Restart your terminal/IDE after setting the variable.

▶️ Run the App
Start the Flask server:

bash
Copy code
python app.py
Open the app in your browser:
👉 http://127.0.0.1:5000

📂 Project Structure
bash
Copy code
weather-app/
│── app.py              # Flask backend
│── requirements.txt    # Python dependencies
│── templates/
│     └── index.html    # Frontend UI
│── README.md           # Documentation
🌍 Usage
Open the app in your browser

Enter a city name (auto-suggestions will appear)

Click search or use the GPS button

See current weather + 7-day forecast

🛡️ Notes
Don’t hardcode your API key in app.py

Store it safely in an environment variable

If you see ❌ Missing OPENWEATHER_API_KEY, your API key is not set correctly
