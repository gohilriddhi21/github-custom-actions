import os

print("Exceuted entrypoint.py from action-1.")
print("WEATHER_API_KEY = ", os.environ.get("WEATHER_API_KEY"))
print("VAR_1 = ", os.environ.get("VAR_1"))