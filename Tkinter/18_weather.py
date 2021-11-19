from tkinter import *
import requests
import json

root = Tk()
root.title('Codemy.com - Learn to Code')
root.geometry("400x32")
root.configure(background="green")


# create a requests variables

# dictionary to associate quality with color
category_color = {
    "Good": "green",
    "Moderate": "yellow",
    "Unhealthy for Sensitive Groups": "#FF7E00",
    "Unhealthy": "red",
    "Very Unhealthy": "#8F3F97",
    "Hazardous": "#7E0023",
    "Unavailable": "#E1EBF4"
}


api_url = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89104&date=2021-11-18&distance=5&API_KEY=D3C5E5E5-4893-4669-8819-58EBFFF1797D"
try:
    api_requests = requests.get(api_url)
    api = json.loads(api_requests.content)
    city = api[0]['ReportingArea']
    quality = str(api[0]['AQI'])
    category = api[0]['Category']['Name']
    my_label = Label(root, text=city + ": Quality " + quality
                     + " (" + category + ")", font=("Helvetica", 20),
                     background=category_color[category])
    my_label.pack()

except Exception as e:
    api = "Error..."


root.mainloop()
