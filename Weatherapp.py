from tkinter import *  # Importing tkinter for GUI elements
from tkinter import ttk  # Importing ttk for the combobox widget
import requests  # Importing requests to handle HTTP requests

def get_data():
    city = city_name.get()  # Get the city name from the combobox
    # Make an API call to OpenWeatherMap to fetch weather data for the selected city
    data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=6f79c199a09efc93709b9f1bf81ea4ec").json()
    
    # Check if the response is successful
    if data["cod"] == 200:  
        # Update the labels with the fetched weather data
        w_label1.config(text=data["weather"][0]["main"])  # Main weather condition
        wb_label1.config(text=data["weather"][0]["description"])  # Detailed weather description
        temp_label1.config(text=str(round(data["main"]["temp"] - 273.15, 2)) + " °C")  # Temperature in Celsius
        per_label1.config(text=str(data["main"]["pressure"]) + " hPa")  # Atmospheric pressure in hPa
    else:
        # If the city is not found, set all labels to "N/A"
        w_label1.config(text="N/A")
        wb_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        per_label1.config(text="N/A")

# Create the main window
win = Tk()
win.title("Tkinter's GUI")  # Set the window title
win.config(bg="sky blue")  # Set the background color of the window
win.geometry("500x550")  # Set the window size

# Create and place the main title label
name_label = Label(win, text="Weather App", font=("Time New Roman", 40, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()  # Create a StringVar to hold the selected city name

# List of Indian states for the combobox
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chattisgarh", "Goa", "Gujarat", "Haryana", 
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", 
             "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

# Create and place the combobox for selecting a city
com = ttk.Combobox(win, values=list_name, font=("Time New Roman", 25, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

# Create and place the "Done" button that triggers the get_data function
done_button = Button(win, text="Done", font=("Time New Roman", 25, "bold"), command=get_data)
done_button.place(y=190, height=50, width=100, x=200)

# Create and place the weather climate label and its value label
w_label = Label(win, text="Weather Climate", font=("Time New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Time New Roman", 15, "bold"))
w_label1.place(x=250, y=260, height=50, width=210)

# Create and place the weather description label and its value label
wb_label = Label(win, text="Weather Description", font=("Time New Roman", 17))
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(win, text="", font=("Time New Roman", 17))
wb_label1.place(x=250, y=330, height=50, width=210)

# Create and place the temperature label and its value label
temp_label = Label(win, text="Temperature", font=("Time New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text="", font=("Time New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

# Create and place the pressure label and its value label
per_label = Label(win, text="Pressure", font=("Time New Roman", 20))
per_label.place(x=25, y=470, height=50, width=210)
per_label1 = Label(win, text="", font=("Time New Roman", 20))
per_label1.place(x=250, y=470, height=50, width=210)

win.mainloop()  # Run the main event loop to display the window
