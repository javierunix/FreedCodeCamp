from tkinter import Tk, Label, Entry, Button
import requests
import json

root = Tk()
root.title('Codemy.com - Learn to Code')
root.geometry("600x100")


# dictionary to associate quality with color
categoryColor = {
    "Good": "#00FF00",
    "Moderate": "#FFFF00",
    "Unhealthy for Sensitive Groups": "#FF7E00",
    "Unhealthy": "#FA0000",
    "Very Unhealthy": "#8F3F97",
    "Hazardous": "#7E0023",
    "Unavailable": "#E1EBF4"
}


def zipCodeLookUp():

    try:
        url = "https://www.airnowapi.org/aq/forecast/zipCode/" + \
            "?format=application/json&zipCode=" + zipCode.get() + \
            "&date=2021-11-20&distance=25&" +\
            "API_KEY=D3C5E5E5-4893-4669-8819-58EBFFF1797D"

        apiRequests = requests.get(url)
        api = json.loads(apiRequests.content)
        city = api[0]['ReportingArea']
        quality = str(api[0]['AQI'])
        category = api[0]['Category']['Name']
        root.configure(background=categoryColor[category])

        myLabel = Label(root, text=city + ": Quality " + quality
                        + " (" + category + ")", font=("Helvetica", 20),
                        background=categoryColor[category])
        myLabel.grid(row=1, column=0, columnspan=2)

    except Exception:
        api = "Error..."


zipCode = Entry(root)
zipCode.grid(row=0, column=0)

zipCodeButton = Button(root, text="Lookup Zipcode", command=zipCodeLookUp)
zipCodeButton.grid(row=0, column=1)


root.mainloop()
