import requests
from django.shortcuts import render

API_KEY = "f0250efd8bcc5fd559101d6ba3bd9c03"

def weather(request):
    city = request.GET.get('city', 'Almaty')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    weather_data = {}
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") == 200:
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"],
            }
        else:
            weather_data = {"error": "Город не найден!"}
    except:
        weather_data = {"error": "Ошибка запроса"}

    return render(request, 'weather.html', {'weather': weather_data})
from django.shortcuts import render

# Create your views here.
