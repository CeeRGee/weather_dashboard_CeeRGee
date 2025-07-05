import matplotlib.pyplot as plt
import csv
from datetime import datetime

def show_temperature_graph(file_path="data/weather_log.csv"):
    dates = []
    temps = []

    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)[-7:]  # Get last 7 rows (days)

            for row in rows:
                date_str = row[0]
                temp = float(row[2])
                dates.append(datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d"))
                temps.append(temp)

        plt.figure(figsize=(8, 4))
        plt.plot(dates, temps, marker='o', linestyle='-', color='teal')
        plt.title("Last 7 Days of Temperatures")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°F)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("No weather log found. Click 'Get Weather' at least once first.")
