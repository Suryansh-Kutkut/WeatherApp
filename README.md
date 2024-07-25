Explanation:
Imports: Import necessary libraries (tkinter for the GUI, ttk for the combo box, and requests for fetching data from the web).
get_data Function:
Fetches weather data from the OpenWeatherMap API based on the selected city.
Updates the GUI labels with the fetched data (weather climate, description, temperature in Celsius, and pressure in hPa).
Handles the case where the city is not found by setting all labels to "N/A".
Main Window Setup:
Sets up the main application window with a title, background color, and size.
Adds a title label for the application.
Creates a combo box for selecting the city from a predefined list of Indian states.
Adds a "Done" button that calls the get_data function to fetch and display weather data.
Adds labels to display weather information (climate, description, temperature, and pressure) and places them appropriately in the window.
This code provides a clear and understandable structure for your weather information application.
