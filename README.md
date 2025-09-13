# 🌦️ Flask Weather App

A simple **Weather Forecast Web Application** built with **Python (Flask)** and the **OpenWeather API**.  
This app allows users to search for weather by **city name**, use **autocomplete suggestions**, or fetch weather by **current location (GPS)**.  
It also shows the **7-day forecast** with min/max temperatures, weather icons, and descriptions.

---

## 🚀 Features
- ✅ Search weather by **city name**  
- ✅ **Autocomplete city suggestions** while typing  
- ✅ Fetch weather by **current location (GPS)**  
- ✅ Current weather info:  
  - 🌡️ Temperature  
  - 🌍 City & Country  
  - ⛅ Weather condition & description  
  - 💨 Wind speed  
- ✅ **7-Day Forecast** with min/max temperature, weather icon & description  
- ✅ Clean, responsive UI with simple design  

---

## 🛠️ Requirements
Make sure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)  

---

## 📦 Installation & Setup

### 1️⃣ Clone the project
```bash
git clone https://github.com/yourusername/flask-weather-app.git
cd flask-weather-app
2️⃣ Create a virtual environment (recommended)
bash
Copy code
python -m venv venv
Activate it:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Get an OpenWeather API Key
Go to OpenWeatherMap

Sign up (free) and get your API key

Replace the API key in app.py:

python
Copy code
API_KEY = "your_api_key_here"
5️⃣ Run the Flask app
bash
Copy code
python app.py
By default, the app runs on http://127.0.0.1:5000/

🌐 Usage
Open your browser and go to:
👉 http://127.0.0.1:5000/

Type a city name (e.g., London, New York, Mumbai)

Select from suggestions or press search

Or click the 📍 GPS button to get weather for your current location

View current weather and 7-day forecast

📁 Project Structure
bash
Copy code
flask-weather-app/
│── app.py              # Main Flask backend
│── requirements.txt    # Dependencies
│── templates/
│    └── index.html     # Frontend (HTML + JS + CSS)
│── README.md           # Documentation
📷 Screenshot
(You can add your own screenshot here later)

🙌 Credits
Flask - Python Web Framework

OpenWeather API - Weather Data Provider

📜 License
This project is open-source and free to use for learning purposes.
