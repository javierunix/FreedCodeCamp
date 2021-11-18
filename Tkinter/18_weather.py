from tkinter import *
import requests
import json

root = Tk()
root.title('Codemy.com - Learn to Code')
root.geometry("400x32")
root.configure(background="green")



# create a requests variables

api_url = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89104&date=2021-11-18&distance=5&API_KEY=D3C5E5E5-4893-4669-8819-58EBFFF1797D"
try:
    api_requests = requests.get(api_url)
    api = json.loads(api_requests.content)
    city = api[0]['ReportingArea']
    quality = str(api[0]['AQI'])
    category = api[0]['Category']['Name']

except Exception as e:
    api = "Error..."

my_label = Label(root, text=city + ": Quality " + quality
    + " (" + category + ")", font=("Helvetica", 20), background="green")
my_label.pack()

root.mainloop()




