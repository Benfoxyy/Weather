import requests
from datetime import datetime

def get_weather(city):
    
        URL="https://api.openweathermap.org/data/2.5/weather"
        PARAMS={'q':city,'appid':'3f591382e9e21b0549d3fbdeeca1bf13'}
        r=requests.get(url=URL,params=PARAMS)
        data=r.json()
        if data['cod']==200:
            print(data['cod'])
            name=data['name']
            t=data['main']['temp']-272.15
            tm=("%.2f" % t)
            hmt=data['main']['humidity']
            wind_speed=data['wind']['speed']
            date=datetime.now().strftime("%b %d")
            day=datetime.now().strftime("%A")
            weather=data['weather'][0]['main']
            print(weather)
            return name,tm,hmt,wind_speed,date,day,weather
        else:
            error_type = data['cod']
            rmessage = data['message']
            return error_type,rmessage
