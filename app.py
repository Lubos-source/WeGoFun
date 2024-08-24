from config import * 
import os

# Získání API_KEY z environment variables
API_KEY = os.getenv('API_KEY')

print("This is Testing")
print(f"Secret:{API_KEY}")
print(f"dalsi:{DALSI}")
