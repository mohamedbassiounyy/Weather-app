import tkinter as tk
from tkinter import messagebox
import requests

# Define the function to get weather data
def get_weather():
    api_key = "fba0391567846017269fb1db85a5ff19"  # Your OpenWeatherMap API key
    location = location_entry.get()

    if not location:
        messagebox.showerror("Error", "Please enter a location")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
            return

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        precipitation = data.get('rain', {}).get('1h', 0)

        temperature_label.config(text=f"Temperature: {temperature}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} km/h")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        precipitation_label.config(text=f"Precipitation: {precipitation} mm")

    except Exception as e:
        messagebox.showerror("Error", "Could not retrieve weather data")
        print(e)

# Initialize the GUI window
root = tk.Tk()
root.title("Weather Forecast")

# Create input field for location
tk.Label(root, text="Location:").grid(row=0, column=0, padx=20, pady=20)
location_entry = tk.Entry(root)
location_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a search button
search_button = tk.Button(root, text="Search", command=get_weather)
search_button.grid(row=0, column=2, padx=10, pady=10)

# Create labels for weather data
temperature_label = tk.Label(root, text="Temperature: --°C")
temperature_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

humidity_label = tk.Label(root, text="Humidity: --%")
humidity_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

wind_speed_label = tk.Label(root, text="Wind Speed: -- km/h")
wind_speed_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

pressure_label = tk.Label(root, text="Pressure: -- hPa")
pressure_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

precipitation_label = tk.Label(root, text="Precipitation: -- mm")
precipitation_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI loop
root.mainloop()
