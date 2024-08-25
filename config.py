DALSI = "dalsi nastaveni napr URLs"
WEATHER_TEST = "http://api.openweathermap.org/data/2.5/weather"
WEATHER = "http://api.openweathermap.org/data/2.5/forecast"
AI_API = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"

def get_prompts(city, day, lang):

    prompt = f"""
    {{"contents":
     [
         {{"role": "user",
        "parts":[
                {{"text": "Give me five activities (each on line starting with -) (in country code: '{lang}' language) what to do in {city} (or home) if it is {lang}:'{day}' day ?"}}
            ]
         }}
     ]
    }}
    """
    return prompt
