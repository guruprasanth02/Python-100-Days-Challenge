import requests, json

def getcode(code):
  if code == 0:
    return "Clear Sky"
  elif code == 1 or code == 2 or code == 3:
    return "Mainly Clear, Partly Cloudy, and Overcast"
  elif code == 45 or code == 48:
    return "Fog and Depositing Rain Fog"
  elif code == 51 or code == 53 or code == 55:
    return "Drizzle: Light, Moderate, and Dense Intensity"
  elif code == 56 or code == 57:
    return "Freezing Drizzle: Light and Dense Intensity"
  elif code == 61 or code == 63 or code == 65:
    return "Rain: Slight, Moderate and Heavy Intensity"
  elif code == 66 or code == 67:
    return "Freezing Rain: Light and Heavy Intensity"
  elif code == 71 or code == 73 or code == 75:
    return "Snow Fall: Slight, Moderate, and Heavy Intensity"
  elif code == 77:
    return "Snow Grains"
  elif code == 80 or code == 81 or code == 82:
    return "Rain Showers: Slight, Moderate, and Violent"
  elif code == 85 or code == 86:
    return "Snow Showers Slight and Heavy"
  elif code == 95:
    return "Thunderstorm: Slight or Moderate"
  elif code == 96 or code == 98:
    return "Thunderstorm with Slight and Heavy Hail"
  elif code == 99:
    return "Thunderstorm with Hail"
    
timezone = "GMT"
latitude = 51.5002
longitude = -0.1262

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
#print(json.dumps(user, indent=2))

weatherCode = user["daily"]["weathercode"][0]
min = user["daily"]["temperature_2m_min"][0]
max = user["daily"]["temperature_2m_max"][0]

print(f"{getcode(weatherCode)}\n🥵: {max}°C\t🥶: {min}°C")
