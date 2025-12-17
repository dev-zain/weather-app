# 🌤️ Weather App

A modern, responsive weather application built with Django that provides real-time weather information for cities worldwide using the OpenWeather API.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-4.2.5-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🌍 Real-time weather data for any city worldwide
- 🎨 Beautiful, responsive UI with smooth animations
- 🌡️ Displays temperature, humidity, wind speed, pressure, and visibility
- 📱 Mobile-friendly design

## 🛠️ Tech Stack

- **Backend:** Python 3.10, Django 4.2.5
- **Frontend:** HTML5, CSS3, JavaScript
- **API:** OpenWeather API
- **Static Files:** WhiteNoise
- **Production Server:** Gunicorn

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- OpenWeather API Key ([Get it free here](https://openweathermap.org/api))

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/dev-zain/weather-app.git
cd weather-app
```

2. **Create virtual environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create `.env` file in root directory**
```env
OPENWEATHER_API_KEY=your_api_key_here
SECRET_KEY=your_django_secret_key_here
DEBUG=True
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Start development server**
```bash
python manage.py runserver
```

7. **Open your browser**
```
http://127.0.0.1:8000/
```

## 🌐 Environment Variables

Create a `.env` file in the root directory with the following variables:

| Variable | Description |
|----------|-------------|
| `OPENWEATHER_API_KEY` | Your OpenWeather API key |
| `SECRET_KEY` | Django secret key for security |
| `DEBUG` | Set to `True` for development, `False` for production |




## 🚀 Deployment

This app can be deployed on Railway, Heroku, or any platform supporting Django.

**Live Demo:**(https://web-production-c3ac9.up.railway.app/)

## 📝 To-Do / Future Enhancements

- [ ] Add 5-day weather forecast
- [ ] Add geolocation support
- [ ] Add multiple city comparison
- [ ] Add weather alerts and notifications
- [ ] Add dark mode toggle
- [ ] Add unit conversion (°C to °F)
- [ ] Add search history
- [ ] Add weather maps integration

## 👨‍💻 Author

**Zain**
- GitHub: [@dev-zain](https://github.com/dev-zain)

## 📄 License

This project is open source and available under the MIT License. 

## 🙏 Acknowledgments

- Weather data provided by [OpenWeather](https://openweathermap.org/)
- Built with [Django](https://www.djangoproject.com/)

---

⭐ **If you like this project, please give it a star! **