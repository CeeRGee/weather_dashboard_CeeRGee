import tkinter as tk
import requests
from config import API_KEY, DEFAULT_CITY
from features.simple_stats import save_weather_data, load_last_7_days, calculate_stats

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300+100+100")


# 🏷️ Main display label
label = tk.Label(root, text="Welcome to my Weather App", font=("Arial", 12))
label.pack(pady=20)

# 🌦️ Fetch weather from OpenWeatherMap
def fetch_weather():
    city = DEFAULT_CITY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]

            # 🧠 Feature #1: Save & analyze data
            save_weather_data(city, temp, description)
            rows = load_last_7_days()
            min_temp, max_temp, weather_counts = calculate_stats(rows)

            label.config(
                text=f"{city}: {temp}°F, {description}\n"
                     f"Min: {min_temp}°F | Max: {max_temp}°F"
            )

            print("Weather Type Counts:", weather_counts)

        else:
            label.config(text="Error: " + data.get("message", "Unknown error"))

    except Exception as e:
        label.config(text="Error fetching data.")
        print("Exception:", e)

# 🔘 Button to fetch weather
button = tk.Button(root, text="Get Weather", command=fetch_weather)
button.pack()

print("Launching GUI...")
print("Root is:", root)
root.mainloop()
