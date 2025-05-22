import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    api_key = "902f74c63b7f4205a9171109252205"
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            temp = data['current']['temp_c']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            last_updated = data['current']['last_updated']

            result = (
                f"Weather in {city}:\n"
                f"Condition: {condition}\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Last updated: {last_updated}"
            )

            result_label.config(text=result)

        else:
            message = response.json().get("error", {}).get("message", "API error")
            messagebox.showerror("API Error", message)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Failed", str(e))

# GUI setup
root = tk.Tk()
root.configure(bg="#2e2e2e")  
root.title("Shadab's Weather App")

city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()


city_entry = tk.Entry(root, font=("Sans Serif", 14))
city_entry.pack(padx=10, pady=10)
city_entry.focus()
city_entry.bind("<Return>", lambda event: get_weather())


get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_btn.pack(padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Sans Serif", 12), justify="left")
result_label.pack(padx=10, pady=10)


copyright_label = tk.Label(
    root,
    text="© Shadab",
    bg="#2e2e2e",
    fg="#777777",
    font=("Sans Serif", 8)
)
copyright_label.pack(side="bottom", pady=5)

root.mainloop()
