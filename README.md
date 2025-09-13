🌦️ Weather App (Flask + OpenWeather API)

A simple and beginner-friendly web application built with Flask that shows current weather and a 7-day forecast for any city.
It also includes location-based weather detection using your device’s GPS and smart city name suggestions while typing.

✨ Features

🌍 Search weather by city name.

📍 Detect weather automatically using your current location (GPS).

🔮 Get a 7-day forecast (min/max temperature, weather description, and icons).

📝 City suggestions dropdown while typing.

🎨 Clean and responsive UI with background gradients.

🛠️ Requirements

Python 3.8+

An OpenWeatherMap API Key (free to generate at openweathermap.org
)

📦 Installation & Setup
1. Clone or Download the Project
git clone https://github.com/your-username/weather-app.git
cd weather-app

2. Create a Virtual Environment (recommended)
python -m venv venv


Activate it:

Windows (cmd):

venv\Scripts\activate


Linux / macOS:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, create it with:

Flask>=2.0
requests

4. Add Your API Key

Open app.py and replace the placeholder with your own API key:

API_KEY = "your_api_key_here"


You can get a free API key from 👉 OpenWeatherMap
.

5. Run the App
python app.py

6. Open in Browser

Go to 👉 http://127.0.0.1:5000

📂 Project Structure
weather-app/
│── app.py               # Flask backend logic
│── requirements.txt     # Dependencies
│── templates/
│    └── index.html      # Frontend UI

🚀 Usage

Type a city name (e.g., "London") → hit search.

Use the GPS button to auto-detect weather for your location.

View 7-day forecast cards with daily temperatures & descriptions.

Try typing slowly → you’ll see city suggestions dropdown.

🖼️ Demo Screenshots

🌤️ Weather card showing temperature, wind, and description.

📊 Forecast section with 7 days of weather info.

(You can add screenshots here by uploading PNG/JPG files to your repo and linking them.)

⚠️ Notes

Free OpenWeatherMap API keys have rate limits (60 requests/min).

If you see "Failed to fetch weather", double-check your API key.

Works best with stable internet and when location permissions are granted.

👨‍💻 Author

Made with ❤️ using Flask and OpenWeather API.
