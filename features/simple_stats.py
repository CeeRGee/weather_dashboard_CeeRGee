import csv
from datetime import datetime

def save_weather_data(city, temp, description, file_path="data/weather_log.csv"):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today, city, temp, description])

def load_last_7_days(file_path="data/weather_log.csv"):
    try:
        with open(file_path, mode='r') as file:
            rows = list(csv.reader(file))
            return rows[-7:]
    except FileNotFoundError:
        return []

def calculate_stats(weather_rows):
    temps = [float(row[2]) for row in weather_rows]
    types = [row[3] for row in weather_rows]
    return min(temps), max(temps), {t: types.count(t) for t in set(types)}
