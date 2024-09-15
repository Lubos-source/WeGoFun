from config import * 
from dotenv import load_dotenv
import os
import requests
import json
from datetime import datetime
from collections import Counter


def calculate_daily_statistics(data):
	minimal=min(data['temp'])
	maximal=max(data['temp'])
	avg_temp = round(sum(data['temp']) / len(data['temp']), 1)
	avg_temp_feel = round(sum(data['temp_feel']) / len(data['temp_feel']), 1)
	most_common_weather, most_common_icon = Counter(data['weather']).most_common(1)[0][0]

	if most_common_icon.endswith('n'):
		most_common_icon = most_common_icon[:-1] + 'd'

	return avg_temp, avg_temp_feel, minimal, maximal, most_common_weather, most_common_icon


def clean_text(text):
	znaky_k_odstraneni = ['-', '/', '"', "'", '#', '&', '|', '\\']
	for znak in znaky_k_odstraneni:
		clean = text.replace(znak, '')
	return clean

def save_to_file(file, records, weather, city, country):
	# Absolutní cesta k uložení souboru v persistentní složce /app/data
    current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
	# Zkontroluje, zda složka existuje, pokud ne, vytvoří ji
    if not os.path.exists(current_dir):
        os.makedirs(current_dir)
    # Kombinace aktuálního adresáře a názvu souboru
    absolutni_cesta = os.path.join(current_dir, file)

    with open(absolutni_cesta, "a", encoding="utf-8") as f:
        for record in records:
            if record.strip():  # Kontrola, zda záznam není prázdný
                clean = clean_text(record)
                # fromát pro uložení do souboru:
                save = f"{clean};;{weather};;{city};;{country}\n"
                f.write(save)



# Získání API_KEY z environment variables
load_dotenv() # for local testing - loading .env variables
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
AI_API_KEY = os.getenv('AI_API_KEY')

# print("This is Testing")
# print(f"Secret:{API_KEY}")
# print(f"Secret:{WEATHER_API_KEY}")
# print(f"dalsi:{DALSI}")

try:
	params = {'q': 'Prague,cz', 'units':'metric','lang':'cz', 'APPID': WEATHER_API_KEY}
	response = requests.get(WEATHER, params=params)
	resp = response.json()
except:
	print("Weather API error") # log

# predpoved 5 dni po 3 hodinach: # api.openweathermap.org/data/2.5/forecast?q=Prague,cz&units=metric&appid={APPI_KEY}
# časy měření předpovědi: 00:00, 03:00, 06:00, 09:00, 12:00, 15:00, 18:00, 21:00, 00:00
testingjson="""
{
	"cod": "200",
	"message": 0,
	"cnt": 40,
	"list": [
		{
			"dt": 1724576400,
			"main": {
				"temp": 23.84,
				"feels_like": 23.92,
				"temp_min": 23.07,
				"temp_max": 23.84,
				"pressure": 1016,
				"sea_level": 1016,
				"grnd_level": 985,
				"humidity": 63,
				"temp_kf": 0.77
			},
			"weather": [
				{
					"id": 802,
					"main": "Clouds",
					"description": "polojasno",
					"icon": "03d"
				}
			],
			"clouds": {
				"all": 29
			},
			"wind": {
				"speed": 5.6,
				"deg": 266,
				"gust": 6.74
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-25 09:00:00"
		},
		{
			"dt": 1724587200,
			"main": {
				"temp": 20.36,
				"feels_like": 20.33,
				"temp_min": 18.43,
				"temp_max": 20.36,
				"pressure": 1019,
				"sea_level": 1019,
				"grnd_level": 987,
				"humidity": 72,
				"temp_kf": 1.93
			},
			"weather": [
				{
					"id": 500,
					"main": "Rain",
					"description": "slabý déšť",
					"icon": "10d"
				}
			],
			"clouds": {
				"all": 61
			},
			"wind": {
				"speed": 2.28,
				"deg": 300,
				"gust": 4.43
			},
			"visibility": 10000,
			"pop": 0.88,
			"rain": {
				"3h": 1.03
			},
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-25 12:00:00"
		},
		{
			"dt": 1724598000,
			"main": {
				"temp": 20.22,
				"feels_like": 19.81,
				"temp_min": 20.22,
				"temp_max": 20.22,
				"pressure": 1021,
				"sea_level": 1021,
				"grnd_level": 987,
				"humidity": 58,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 500,
					"main": "Rain",
					"description": "slabý déšť",
					"icon": "10d"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 1.9,
				"deg": 316,
				"gust": 4.67
			},
			"visibility": 10000,
			"pop": 0.2,
			"rain": {
				"3h": 0.11
			},
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-25 15:00:00"
		},
		{
			"dt": 1724608800,
			"main": {
				"temp": 18.67,
				"feels_like": 18.11,
				"temp_min": 18.67,
				"temp_max": 18.67,
				"pressure": 1022,
				"sea_level": 1022,
				"grnd_level": 987,
				"humidity": 58,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04d"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 2.18,
				"deg": 39,
				"gust": 2.72
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-25 18:00:00"
		},
		{
			"dt": 1724619600,
			"main": {
				"temp": 17.36,
				"feels_like": 16.8,
				"temp_min": 17.36,
				"temp_max": 17.36,
				"pressure": 1023,
				"sea_level": 1023,
				"grnd_level": 988,
				"humidity": 63,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04n"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 0.4,
				"deg": 134,
				"gust": 0.52
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-25 21:00:00"
		},
		{
			"dt": 1724630400,
			"main": {
				"temp": 16.48,
				"feels_like": 15.99,
				"temp_min": 16.48,
				"temp_max": 16.48,
				"pressure": 1022,
				"sea_level": 1022,
				"grnd_level": 988,
				"humidity": 69,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04n"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 0.76,
				"deg": 207,
				"gust": 1.11
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-26 00:00:00"
		},
		{
			"dt": 1724641200,
			"main": {
				"temp": 16.51,
				"feels_like": 16.04,
				"temp_min": 16.51,
				"temp_max": 16.51,
				"pressure": 1022,
				"sea_level": 1022,
				"grnd_level": 987,
				"humidity": 70,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04n"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 0.42,
				"deg": 262,
				"gust": 0.57
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-26 03:00:00"
		},
		{
			"dt": 1724652000,
			"main": {
				"temp": 16.46,
				"feels_like": 16.12,
				"temp_min": 16.46,
				"temp_max": 16.46,
				"pressure": 1023,
				"sea_level": 1023,
				"grnd_level": 988,
				"humidity": 75,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 500,
					"main": "Rain",
					"description": "slabý déšť",
					"icon": "10d"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 1.4,
				"deg": 158,
				"gust": 1.62
			},
			"visibility": 10000,
			"pop": 0.27,
			"rain": {
				"3h": 0.15
			},
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-26 06:00:00"
		},
		{
			"dt": 1724662800,
			"main": {
				"temp": 17.13,
				"feels_like": 16.75,
				"temp_min": 17.13,
				"temp_max": 17.13,
				"pressure": 1023,
				"sea_level": 1023,
				"grnd_level": 988,
				"humidity": 71,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 500,
					"main": "Rain",
					"description": "slabý déšť",
					"icon": "10d"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 0.94,
				"deg": 202,
				"gust": 1.21
			},
			"visibility": 10000,
			"pop": 0.75,
			"rain": {
				"3h": 0.62
			},
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-26 09:00:00"
		},
		{
			"dt": 1724673600,
			"main": {
				"temp": 19,
				"feels_like": 18.57,
				"temp_min": 19,
				"temp_max": 19,
				"pressure": 1022,
				"sea_level": 1022,
				"grnd_level": 988,
				"humidity": 62,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 500,
					"main": "Rain",
					"description": "slabý déšť",
					"icon": "10d"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 0.94,
				"deg": 45,
				"gust": 2.01
			},
			"visibility": 10000,
			"pop": 0.73,
			"rain": {
				"3h": 0.35
			},
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-26 12:00:00"
		},
		{
			"dt": 1724684400,
			"main": {
				"temp": 19.48,
				"feels_like": 19.13,
				"temp_min": 19.48,
				"temp_max": 19.48,
				"pressure": 1022,
				"sea_level": 1022,
				"grnd_level": 987,
				"humidity": 63,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 500,
					"main": "Rain",
					"description": "slabý déšť",
					"icon": "10d"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 0.67,
				"deg": 349,
				"gust": 0.88
			},
			"visibility": 10000,
			"pop": 0.7,
			"rain": {
				"3h": 0.5
			},
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-26 15:00:00"
		},
		{
			"dt": 1724695200,
			"main": {
				"temp": 17.51,
				"feels_like": 17.25,
				"temp_min": 17.51,
				"temp_max": 17.51,
				"pressure": 1022,
				"sea_level": 1022,
				"grnd_level": 988,
				"humidity": 74,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 500,
					"main": "Rain",
					"description": "slabý déšť",
					"icon": "10n"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 1.11,
				"deg": 300,
				"gust": 1.31
			},
			"visibility": 10000,
			"pop": 0.45,
			"rain": {
				"3h": 0.15
			},
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-26 18:00:00"
		},
		{
			"dt": 1724706000,
			"main": {
				"temp": 16.19,
				"feels_like": 15.88,
				"temp_min": 16.19,
				"temp_max": 16.19,
				"pressure": 1023,
				"sea_level": 1023,
				"grnd_level": 988,
				"humidity": 77,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04n"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 0.92,
				"deg": 266,
				"gust": 0.9
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-26 21:00:00"
		},
		{
			"dt": 1724716800,
			"main": {
				"temp": 15.33,
				"feels_like": 14.98,
				"temp_min": 15.33,
				"temp_max": 15.33,
				"pressure": 1023,
				"sea_level": 1023,
				"grnd_level": 988,
				"humidity": 79,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04n"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 1.46,
				"deg": 268,
				"gust": 1.46
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-27 00:00:00"
		},
		{
			"dt": 1724727600,
			"main": {
				"temp": 14.91,
				"feels_like": 14.49,
				"temp_min": 14.91,
				"temp_max": 14.91,
				"pressure": 1022,
				"sea_level": 1022,
				"grnd_level": 988,
				"humidity": 78,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04n"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 0.44,
				"deg": 211,
				"gust": 0.33
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-27 03:00:00"
		},
		{
			"dt": 1724738400,
			"main": {
				"temp": 16.68,
				"feels_like": 16.26,
				"temp_min": 16.68,
				"temp_max": 16.68,
				"pressure": 1023,
				"sea_level": 1023,
				"grnd_level": 988,
				"humidity": 71,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04d"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 1.33,
				"deg": 343,
				"gust": 2.08
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-27 06:00:00"
		},
		{
			"dt": 1724749200,
			"main": {
				"temp": 21.68,
				"feels_like": 21.29,
				"temp_min": 21.68,
				"temp_max": 21.68,
				"pressure": 1023,
				"sea_level": 1023,
				"grnd_level": 989,
				"humidity": 53,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 802,
					"main": "Clouds",
					"description": "polojasno",
					"icon": "03d"
				}
			],
			"clouds": {
				"all": 47
			},
			"wind": {
				"speed": 2.32,
				"deg": 20,
				"gust": 3.15
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-27 09:00:00"
		},
		{
			"dt": 1724760000,
			"main": {
				"temp": 25.28,
				"feels_like": 25.06,
				"temp_min": 25.28,
				"temp_max": 25.28,
				"pressure": 1021,
				"sea_level": 1021,
				"grnd_level": 987,
				"humidity": 46,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 801,
					"main": "Clouds",
					"description": "skoro jasno",
					"icon": "02d"
				}
			],
			"clouds": {
				"all": 24
			},
			"wind": {
				"speed": 3.16,
				"deg": 60,
				"gust": 3.77
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-27 12:00:00"
		},
		{
			"dt": 1724770800,
			"main": {
				"temp": 26.89,
				"feels_like": 26.88,
				"temp_min": 26.89,
				"temp_max": 26.89,
				"pressure": 1020,
				"sea_level": 1020,
				"grnd_level": 986,
				"humidity": 42,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 801,
					"main": "Clouds",
					"description": "skoro jasno",
					"icon": "02d"
				}
			],
			"clouds": {
				"all": 14
			},
			"wind": {
				"speed": 4.21,
				"deg": 67,
				"gust": 4.97
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-27 15:00:00"
		},
		{
			"dt": 1724781600,
			"main": {
				"temp": 22.45,
				"feels_like": 22.19,
				"temp_min": 22.45,
				"temp_max": 22.45,
				"pressure": 1020,
				"sea_level": 1020,
				"grnd_level": 986,
				"humidity": 55,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 801,
					"main": "Clouds",
					"description": "skoro jasno",
					"icon": "02n"
				}
			],
			"clouds": {
				"all": 13
			},
			"wind": {
				"speed": 4.22,
				"deg": 80,
				"gust": 8.87
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-27 18:00:00"
		},
		{
			"dt": 1724792400,
			"main": {
				"temp": 19.85,
				"feels_like": 19.51,
				"temp_min": 19.85,
				"temp_max": 19.85,
				"pressure": 1021,
				"sea_level": 1021,
				"grnd_level": 987,
				"humidity": 62,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 800,
					"main": "Clear",
					"description": "jasno",
					"icon": "01n"
				}
			],
			"clouds": {
				"all": 5
			},
			"wind": {
				"speed": 3.02,
				"deg": 81,
				"gust": 6.23
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-27 21:00:00"
		},
		{
			"dt": 1724803200,
			"main": {
				"temp": 18.48,
				"feels_like": 18.13,
				"temp_min": 18.48,
				"temp_max": 18.48,
				"pressure": 1021,
				"sea_level": 1021,
				"grnd_level": 987,
				"humidity": 67,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 800,
					"main": "Clear",
					"description": "jasno",
					"icon": "01n"
				}
			],
			"clouds": {
				"all": 9
			},
			"wind": {
				"speed": 2.24,
				"deg": 67,
				"gust": 4.12
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-28 00:00:00"
		},
		{
			"dt": 1724814000,
			"main": {
				"temp": 17.49,
				"feels_like": 17.07,
				"temp_min": 17.49,
				"temp_max": 17.49,
				"pressure": 1020,
				"sea_level": 1020,
				"grnd_level": 986,
				"humidity": 68,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 800,
					"main": "Clear",
					"description": "jasno",
					"icon": "01n"
				}
			],
			"clouds": {
				"all": 9
			},
			"wind": {
				"speed": 1.87,
				"deg": 38,
				"gust": 3.15
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-28 03:00:00"
		},
		{
			"dt": 1724824800,
			"main": {
				"temp": 19.37,
				"feels_like": 18.98,
				"temp_min": 19.37,
				"temp_max": 19.37,
				"pressure": 1020,
				"sea_level": 1020,
				"grnd_level": 986,
				"humidity": 62,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 800,
					"main": "Clear",
					"description": "jasno",
					"icon": "01d"
				}
			],
			"clouds": {
				"all": 10
			},
			"wind": {
				"speed": 1.77,
				"deg": 61,
				"gust": 3.54
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-28 06:00:00"
		},
		{
			"dt": 1724835600,
			"main": {
				"temp": 25.26,
				"feels_like": 25.17,
				"temp_min": 25.26,
				"temp_max": 25.26,
				"pressure": 1020,
				"sea_level": 1020,
				"grnd_level": 986,
				"humidity": 51,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 801,
					"main": "Clouds",
					"description": "skoro jasno",
					"icon": "02d"
				}
			],
			"clouds": {
				"all": 11
			},
			"wind": {
				"speed": 3.48,
				"deg": 105,
				"gust": 4.72
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-28 09:00:00"
		},
		{
			"dt": 1724846400,
			"main": {
				"temp": 30.67,
				"feels_like": 30.49,
				"temp_min": 30.67,
				"temp_max": 30.67,
				"pressure": 1018,
				"sea_level": 1018,
				"grnd_level": 984,
				"humidity": 40,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 801,
					"main": "Clouds",
					"description": "skoro jasno",
					"icon": "02d"
				}
			],
			"clouds": {
				"all": 16
			},
			"wind": {
				"speed": 3.6,
				"deg": 115,
				"gust": 5.79
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-28 12:00:00"
		},
		{
			"dt": 1724857200,
			"main": {
				"temp": 31.99,
				"feels_like": 31.46,
				"temp_min": 31.99,
				"temp_max": 31.99,
				"pressure": 1017,
				"sea_level": 1017,
				"grnd_level": 983,
				"humidity": 35,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 802,
					"main": "Clouds",
					"description": "polojasno",
					"icon": "03d"
				}
			],
			"clouds": {
				"all": 25
			},
			"wind": {
				"speed": 3.92,
				"deg": 153,
				"gust": 5.41
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-28 15:00:00"
		},
		{
			"dt": 1724868000,
			"main": {
				"temp": 26.9,
				"feels_like": 27.15,
				"temp_min": 26.9,
				"temp_max": 26.9,
				"pressure": 1017,
				"sea_level": 1017,
				"grnd_level": 983,
				"humidity": 47,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 802,
					"main": "Clouds",
					"description": "polojasno",
					"icon": "03n"
				}
			],
			"clouds": {
				"all": 28
			},
			"wind": {
				"speed": 1.62,
				"deg": 97,
				"gust": 1.53
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-28 18:00:00"
		},
		{
			"dt": 1724878800,
			"main": {
				"temp": 23.51,
				"feels_like": 23.46,
				"temp_min": 23.51,
				"temp_max": 23.51,
				"pressure": 1018,
				"sea_level": 1018,
				"grnd_level": 984,
				"humidity": 59,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 803,
					"main": "Clouds",
					"description": "oblačno",
					"icon": "04n"
				}
			],
			"clouds": {
				"all": 59
			},
			"wind": {
				"speed": 2.55,
				"deg": 109,
				"gust": 6.1
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-28 21:00:00"
		},
		{
			"dt": 1724889600,
			"main": {
				"temp": 21.3,
				"feels_like": 21.26,
				"temp_min": 21.3,
				"temp_max": 21.3,
				"pressure": 1018,
				"sea_level": 1018,
				"grnd_level": 984,
				"humidity": 68,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 802,
					"main": "Clouds",
					"description": "polojasno",
					"icon": "03n"
				}
			],
			"clouds": {
				"all": 36
			},
			"wind": {
				"speed": 1.14,
				"deg": 145,
				"gust": 1.32
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-29 00:00:00"
		},
		{
			"dt": 1724900400,
			"main": {
				"temp": 20.3,
				"feels_like": 20.27,
				"temp_min": 20.3,
				"temp_max": 20.3,
				"pressure": 1018,
				"sea_level": 1018,
				"grnd_level": 984,
				"humidity": 72,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 800,
					"main": "Clear",
					"description": "jasno",
					"icon": "01n"
				}
			],
			"clouds": {
				"all": 7
			},
			"wind": {
				"speed": 1.04,
				"deg": 73,
				"gust": 0.98
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-29 03:00:00"
		},
		{
			"dt": 1724911200,
			"main": {
				"temp": 21.91,
				"feels_like": 21.91,
				"temp_min": 21.91,
				"temp_max": 21.91,
				"pressure": 1018,
				"sea_level": 1018,
				"grnd_level": 984,
				"humidity": 67,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 800,
					"main": "Clear",
					"description": "jasno",
					"icon": "01d"
				}
			],
			"clouds": {
				"all": 7
			},
			"wind": {
				"speed": 0.64,
				"deg": 178,
				"gust": 1.2
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-29 06:00:00"
		},
		{
			"dt": 1724922000,
			"main": {
				"temp": 27.56,
				"feels_like": 27.97,
				"temp_min": 27.56,
				"temp_max": 27.56,
				"pressure": 1018,
				"sea_level": 1018,
				"grnd_level": 984,
				"humidity": 50,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 800,
					"main": "Clear",
					"description": "jasno",
					"icon": "01d"
				}
			],
			"clouds": {
				"all": 9
			},
			"wind": {
				"speed": 0.87,
				"deg": 144,
				"gust": 1.21
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-29 09:00:00"
		},
		{
			"dt": 1724932800,
			"main": {
				"temp": 31.62,
				"feels_like": 31.43,
				"temp_min": 31.62,
				"temp_max": 31.62,
				"pressure": 1017,
				"sea_level": 1017,
				"grnd_level": 983,
				"humidity": 38,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 801,
					"main": "Clouds",
					"description": "skoro jasno",
					"icon": "02d"
				}
			],
			"clouds": {
				"all": 15
			},
			"wind": {
				"speed": 1.09,
				"deg": 133,
				"gust": 1.69
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-29 12:00:00"
		},
		{
			"dt": 1724943600,
			"main": {
				"temp": 32,
				"feels_like": 31.47,
				"temp_min": 32,
				"temp_max": 32,
				"pressure": 1016,
				"sea_level": 1016,
				"grnd_level": 983,
				"humidity": 35,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04d"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 0.43,
				"deg": 134,
				"gust": 1.47
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-29 15:00:00"
		},
		{
			"dt": 1724954400,
			"main": {
				"temp": 27.4,
				"feels_like": 27.53,
				"temp_min": 27.4,
				"temp_max": 27.4,
				"pressure": 1016,
				"sea_level": 1016,
				"grnd_level": 983,
				"humidity": 46,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04n"
				}
			],
			"clouds": {
				"all": 100
			},
			"wind": {
				"speed": 1.17,
				"deg": 358,
				"gust": 1.3
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-29 18:00:00"
		},
		{
			"dt": 1724965200,
			"main": {
				"temp": 23.67,
				"feels_like": 23.79,
				"temp_min": 23.67,
				"temp_max": 23.67,
				"pressure": 1018,
				"sea_level": 1018,
				"grnd_level": 984,
				"humidity": 65,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 500,
					"main": "Rain",
					"description": "slabý déšť",
					"icon": "10n"
				}
			],
			"clouds": {
				"all": 51
			},
			"wind": {
				"speed": 0.86,
				"deg": 81,
				"gust": 1.17
			},
			"visibility": 10000,
			"pop": 0.95,
			"rain": {
				"3h": 0.73
			},
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-29 21:00:00"
		},
		{
			"dt": 1724976000,
			"main": {
				"temp": 21.19,
				"feels_like": 21.32,
				"temp_min": 21.19,
				"temp_max": 21.19,
				"pressure": 1018,
				"sea_level": 1018,
				"grnd_level": 984,
				"humidity": 75,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 500,
					"main": "Rain",
					"description": "slabý déšť",
					"icon": "10n"
				}
			],
			"clouds": {
				"all": 30
			},
			"wind": {
				"speed": 0.72,
				"deg": 246,
				"gust": 1.41
			},
			"visibility": 10000,
			"pop": 0.88,
			"rain": {
				"3h": 0.21
			},
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-30 00:00:00"
		},
		{
			"dt": 1724986800,
			"main": {
				"temp": 20.48,
				"feels_like": 20.59,
				"temp_min": 20.48,
				"temp_max": 20.48,
				"pressure": 1018,
				"sea_level": 1018,
				"grnd_level": 984,
				"humidity": 77,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 803,
					"main": "Clouds",
					"description": "oblačno",
					"icon": "04n"
				}
			],
			"clouds": {
				"all": 71
			},
			"wind": {
				"speed": 0.28,
				"deg": 312,
				"gust": 0.58
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "n"
			},
			"dt_txt": "2024-08-30 03:00:00"
		},
		{
			"dt": 1724997600,
			"main": {
				"temp": 22.05,
				"feels_like": 22.19,
				"temp_min": 22.05,
				"temp_max": 22.05,
				"pressure": 1019,
				"sea_level": 1019,
				"grnd_level": 985,
				"humidity": 72,
				"temp_kf": 0
			},
			"weather": [
				{
					"id": 804,
					"main": "Clouds",
					"description": "zataženo",
					"icon": "04d"
				}
			],
			"clouds": {
				"all": 87
			},
			"wind": {
				"speed": 0.09,
				"deg": 252,
				"gust": 0.38
			},
			"visibility": 10000,
			"pop": 0,
			"sys": {
				"pod": "d"
			},
			"dt_txt": "2024-08-30 06:00:00"
		}
	],
	"city": {
		"id": 3067696,
		"name": "Prague",
		"coord": {
			"lat": 50.088,
			"lon": 14.4208
		},
		"country": "CZ",
		"population": 1165581,
		"timezone": 7200,
		"sunrise": 1724558838,
		"sunset": 1724608908
	}
}
"""

#resp = json.loads(testingjson)

# ICON urls: https://openweathermap.org/img/wn/{ICON ID} ex: 11d.png

daily_weather={}

city = resp["city"]["name"]
population = resp["city"]["population"]
country = resp["city"]["country"]

sunrise = resp["city"]["sunrise"]
sunset = resp["city"]["sunset"]

for measure in resp['list']:

	date = measure['dt_txt'].split()[0]
	hour = measure['dt_txt'].split()[1]
	#print(hour)
	
	if date not in daily_weather:
		daily_weather[date]={'weather':[],'temp':[], 'temp_feel':[]}

	weather = measure['weather'][0]['description']
	icon = measure['weather'][0]['icon'] # https://openweathermap.org/img/wn/

	temp = measure['main']['temp']
	temp_feel = measure['main']['feels_like']


	daily_weather[date]['weather'].append((weather, icon)) # ukládá tuple (pocasi, ikona)
	daily_weather[date]['temp'].append(temp)
	daily_weather[date]['temp_feel'].append(temp_feel)
	
# print(f"\t{country} --- {city}")
# print(f"populace\t\t{population:,}".replace(',', ' ')) # přidání formátu "," po 3 cifrách (a poté nahrazení "," za mezery) 
# print(f"\nvýchod\t\t\tzápad") # přidání formátu "," po 3 cifrách (a poté nahrazení "," za mezery) 
# print(f"{datetime.fromtimestamp(int(sunrise)).strftime('%H:%M')}\t\t\t{datetime.fromtimestamp(int(sunset)).strftime('%H:%M')}")
# print(35*"=")
# print(daily_weather)

for date, data in daily_weather.items():
	avg_temp, avg_temp_feel, minimal, maximal, most_common_weather, most_common_icon = calculate_daily_statistics(data) # výpočet prům teplot, nejčastějšího počasí v den + ikona

	daily_weather[date].update({
		"avg_temp": avg_temp,
		"avg_temp_feel": avg_temp_feel,
		"minimal": minimal,
		"maximal": maximal,
		"most_common_weather": most_common_weather,
		"most_common_icon": most_common_icon
	})
	
	""" více operací (náročnější):
	daily_weather[date]["avg_temp"]=avg_temp
	daily_weather[date]["avg_temp_feel"]=avg_temp_feel
	daily_weather[date]["most_common_weather"]=most_common_weather
	daily_weather[date]["most_common_icon"]=most_common_icon
	"""

	#print(f"Date:\t\t\t{date}")
	#print(f"Avg temp:\t\t{avg_temp:.1f}°C")
	#print(f"Avg feel:\t\t{avg_temp_feel:.1f}°C")
	#print(f"weather:\t\t{most_common_weather}")
	#print(f"Icon URL:\t\thttps://openweathermap.org/img/wn/{most_common_icon}.png")

#print(daily_weather)

today = next(iter(daily_weather)) # získání prvního záznamu (tedy záznam počasí pro dnešek)

prompt = get_prompts(city, daily_weather[today]["most_common_weather"], country)

if not prompt:
	print("Prompt generation failed.") # log
else:
	params = {'key': AI_API_KEY}
	try:
		response = requests.post(AI_API, params=params, data=prompt)
		
		aijsontesting = """
						{
						    "candidates": [
						        {
						            "content": {
						                "parts": [
						                    {
						                        "text": "- Zahrajte si online hru\\n- Podívejte se na film nebo seriál\\n- Přečtěte si knihu\\n- Navařte si něco dobrého\\n- Uvařte si lahodný čaj"
						                    }
						                ],
						                "role": "model"
						            },
						            "finishReason": "STOP",
						            "index": 0,
						            "safetyRatings": [
						                {
						                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
						                    "probability": "NEGLIGIBLE"
						                },
						                {
						                    "category": "HARM_CATEGORY_HATE_SPEECH",
						                    "probability": "NEGLIGIBLE"
						                },
						                {
						                    "category": "HARM_CATEGORY_HARASSMENT",
						                    "probability": "NEGLIGIBLE"
						                },
						                {
						                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
						                    "probability": "NEGLIGIBLE"
						                }
						            ]
						        }
						    ],
						    "usageMetadata": {
						        "promptTokenCount": 42,
						        "candidatesTokenCount": 47,
						        "totalTokenCount": 89
						    }
						}
						"""

		
		if (response.status_code == 200):
			response_json = response.json()

		#TESTING=True						# for TESTIG
		#if (TESTING):
			#response_json=json.loads(aijsontesting)
			#print(response_json)

			text = response_json["candidates"][0]["content"]["parts"][0]["text"]
			
			###################################
			# Save AI recomendation to file (persistant storage in docker) #
			zaznamy = text.split("\n")
			save_to_file("recomendations.txt",zaznamy,daily_weather[today]['most_common_weather'],city,country)
			###################################
			email_text = f"Dnes bude {daily_weather[today]['avg_temp']}°C - {daily_weather[today]['most_common_weather']}\nmin: {daily_weather[today]['minimal']}°C  max: {daily_weather[today]['maximal']}°C a proto doporučuji:\n{text}\n\n"

			email_text += "další dny bude:\n"
			for i, day in enumerate(daily_weather):
				if i == 0:
					continue
				email_text += f"{day}\n{daily_weather[day]['avg_temp']}°C - {daily_weather[day]['most_common_weather']}\nmin: {daily_weather[day]['minimal']}°C  max: {daily_weather[day]['maximal']}°C\n\n"
		else:
			print(f"FAIL: AI_API response: {response.status_code}") # log

	except:
		print("Chyba AI_API požadavek") # log

#print(f"Email: {email_text}")


email_html = f"""
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Denní přehled počasí</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            color: #333;
        }}
        .header {{
            font-size: 16px;
            margin-bottom: 20px;
        }}
        .header div {{
            margin-bottom: 10px;
        }}
        .weather-report {{
            margin-top: 20px;
        }}
        .weather-day {{
            margin-bottom: 10px;
        }}
        ul {{
            list-style-type: disc;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 5px;
        }}
        .divider {{
            margin: 20px 0;
            border-top: 2px solid #ccc;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div><strong>{country} : {city}</strong></div>
        <div>Populace: {population:,}</div>
        <div>Východ: {datetime.fromtimestamp(int(sunrise)).strftime('%H:%M')} | Západ: {datetime.fromtimestamp(int(sunset)).strftime('%H:%M')}</div>
        <div class="divider"></div>
    </div>
    <h1>Denní přehled počasí <img src="https://openweathermap.org/img/wn/{daily_weather[today]['most_common_icon']}.png" alt="{daily_weather[today]['most_common_weather']}"> </h1>
    <p>Dnes bude <strong>{daily_weather[today]['avg_temp']}°C - {daily_weather[today]['most_common_weather']}</strong> </p>
    <p><strong>min: {daily_weather[today]['minimal']}°C  max: {daily_weather[today]['maximal']}°C</strong> a proto doporučuji: </p>
    <ul>
        {''.join([f'<li>{item}</li>' for item in text.splitlines()])}
    </ul>
    <div class="weather-report">
        <h3>Další dny bude:</h3>
        {''.join([f'<div class="weather-day"><strong>{day}</strong>: {daily_weather[day]["avg_temp"]}°C - {daily_weather[day]["most_common_weather"]}<br/><p>min: {daily_weather[day]["minimal"]}°C  max: {daily_weather[day]["maximal"]}°C</p></div>' for day in daily_weather if day != today])}
    </div>
</body>
</html>
"""

# POZNAMKA: 
# [ ....... for day in daily_weather if day != today ] - list comprehension iteruje přes všechny dny a kontoluje že není dnešní datum, protože to už je zpracováno v první části zprávy
# join spojuje html řetězce aby mezi nimi nebyly další znaky

#####################
#### Email send: ####
#####################
DOMAIN = os.getenv('DOMAIN')
MAIL_API_KEY = os.getenv('MAIL_API_KEY')
MAIL_TO = os.getenv('MAIL_TO')

from_email = "WeGoFun <wegofundev@gmail.com>"
subject = "WeGoFun"
#text_body = "This will be the text-only version"
#html_body = "<html><body><b>This is the HTML version</b></body></html>"

# --------- EMAIL SEND ---------
try:
	response = requests.post(
	    mail(DOMAIN),
	    auth=('api', MAIL_API_KEY),
	    files={
	        'from': (None, from_email),
	        'to': (None, MAIL_TO),
	        'subject': (None, subject),
	        'text': (None, email_text),
	        'html': (None, email_html)
	    }
	)
	print(response.status_code)
	print(response.text)
except:
	print(f"Email send Error {response.status_code}") # log

# testing
#print("odeslání emailu - TESTING - pozastaveno")


#print(email_html)