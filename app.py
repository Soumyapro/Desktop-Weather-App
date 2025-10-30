import tkinter as tk
from tkinter import *
from weather import fetch_weather_data
import os

# API Key - set OPENWEATHER_API_KEY in your environment (do not hardcode)
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def create_search_widgets(root, search_callback):
    """Create search label, entry field, and buttons."""
    # Dark theme color scheme
    bg_color = '#1E1E1E'  # Dark background
    accent_color = '#4A90E2'  # Blue accent
    button_bg = '#2D2D2D'  # Dark button background
    button_hover = '#3D3D3D'  # Button hover
    text_color = '#E0E0E0'  # Light text
    entry_bg = '#2D2D2D'  # Dark entry background
    entry_fg = '#E0E0E0'  # Light entry text
    placeholder_fg = '#757575'  # Gray placeholder

    root.configure(bg=bg_color)

    # Creating a title label on its own row for better visibility
    title_label = Label(root, text="🌤️ Check Today's Weather",
                        font=('Segoe UI', 18, 'bold'),
                        bg=bg_color, fg=text_color)
    title_label.grid(row=0, column=0, columnspan=4, pady=(20, 10))

    # Adding a textfield to input the city name
    city_label = Label(root, text="City:", font=('Segoe UI', 11),
                       bg=bg_color, fg=text_color)
    city_label.grid(row=1, column=0, padx=(15, 5), pady=15, sticky='e')

    text_entry = Entry(root, width=30, font=('Segoe UI', 11),
                       bg=entry_bg, fg=entry_fg,
                       relief=FLAT, borderwidth=2,
                       insertbackground=text_color,
                       highlightbackground=accent_color,
                       highlightthickness=2,
                       highlightcolor=accent_color)
    text_entry.grid(row=1, column=1, padx=10, pady=15, sticky='w')
    text_entry.insert(0, "Enter city name...")
    text_entry.config(fg=placeholder_fg)

    # Add placeholder functionality
    def on_entry_focus_in(event):
        if text_entry.get() == "Enter city name...":
            text_entry.delete(0, END)
            text_entry.config(fg=entry_fg)

    def on_entry_focus_out(event):
        if not text_entry.get():
            text_entry.insert(0, "Enter city name...")
            text_entry.config(fg=placeholder_fg)

    text_entry.bind('<FocusIn>', on_entry_focus_in)
    text_entry.bind('<FocusOut>', on_entry_focus_out)

    # Adding buttons with dark theme styling
    button_style = {
        'font': ('Segoe UI', 11, 'bold'),
        'bg': button_bg,
        'fg': text_color,
        'activebackground': button_hover,
        'activeforeground': text_color,
        'relief': RAISED,
        'borderwidth': 2,
        'highlightbackground': accent_color,
        'highlightthickness': 1,
        'padx': 20,
        'pady': 8,
        'cursor': 'hand2'
    }

    button = Button(root, text="🔍 Search",
                    command=search_callback, **button_style)
    quit_button = Button(root, text='✖ Quit', command=root.quit,
                         font=('Segoe UI', 11, 'bold'),
                         bg=button_bg,
                         fg='#E57373',
                         activebackground=button_hover,
                         activeforeground='#E57373',
                         relief=RAISED,
                         borderwidth=2,
                         highlightbackground='#E57373',
                         highlightthickness=1,
                         padx=20,
                         pady=8,
                         cursor='hand2')

    button.grid(row=1, column=2, padx=10, pady=15)
    quit_button.grid(row=1, column=3, padx=10, pady=15)

    return text_entry, button


def create_weather_display(root):
    """Create frame and labels to display weather data."""
    # Dark theme color palette
    bg_color = '#1E1E1E'  # Main background (matching root)
    frame_bg = '#2D2D2D'  # Dark frame background
    label_bg = frame_bg
    text_color = '#E0E0E0'  # Light text
    accent_color = '#4A90E2'  # Blue accent for temperature

    # Creating weather frame with dark theme styling
    weather_frame = Frame(root, bg=frame_bg, relief=FLAT, bd=1)
    weather_frame.grid(row=2, column=0, columnspan=4,
                       padx=20, pady=20, sticky='ew')

    # Configure column weights for better spacing
    root.columnconfigure(0, weight=1)
    for i in range(4):
        root.columnconfigure(i, weight=1)

    # Creating labels to display weather data with beautiful fonts
    label_font = ('Segoe UI', 11, 'normal')
    value_font = ('Segoe UI', 12, 'bold')

    # City label (prominent)
    city_label = Label(weather_frame, text="City: ",
                       font=label_font, bg=label_bg, fg=text_color)
    city_label.grid(row=0, column=0, padx=15, pady=12, sticky='w')

    # Temperature label (large and prominent)
    temperature_label = Label(weather_frame, text="Temperature: ",
                              font=label_font, bg=label_bg, fg=text_color)
    temperature_label.grid(row=1, column=0, padx=15, pady=12, sticky='w')

    # Feels like label
    feels_like_label = Label(weather_frame, text="Feels Like: ",
                             font=label_font, bg=label_bg, fg=text_color)
    feels_like_label.grid(row=2, column=0, padx=15, pady=12, sticky='w')

    # Main weather condition
    main_label = Label(weather_frame, text="Main: ",
                       font=label_font, bg=label_bg, fg=text_color)
    main_label.grid(row=3, column=0, padx=15, pady=12, sticky='w')

    # Description
    description_label = Label(weather_frame, text="Description: ",
                              font=label_font, bg=label_bg, fg=text_color)
    description_label.grid(row=4, column=0, padx=15, pady=12, sticky='w')

    # Humidity
    humidity_label = Label(weather_frame, text="Humidity: ",
                           font=label_font, bg=label_bg, fg=text_color)
    humidity_label.grid(row=5, column=0, padx=15, pady=12, sticky='w')

    # Wind speed
    wind_speed_label = Label(weather_frame, text="Wind Speed: ",
                             font=label_font, bg=label_bg, fg=text_color)
    wind_speed_label.grid(row=6, column=0, padx=15, pady=12, sticky='w')

    return {
        'city': city_label,
        'temperature': temperature_label,
        'feels_like': feels_like_label,
        'main': main_label,
        'description': description_label,
        'humidity': humidity_label,
        'wind_speed': wind_speed_label
    }


def search_weather(text_entry, weather_labels):
    """Function to handle button click and fetch weather data."""
    city = text_entry.get()

    # Handle placeholder text
    if city == "Enter city name..." or not city.strip():
        print("City not found. Please enter a city name.")
        weather_labels['city'].config(
            text="City: Please enter a city name", fg='#E57373')
        return None

    api_key = API_KEY

    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("API key not configured.")
        weather_labels['city'].config(
            text="City: Please set OPENWEATHER_API_KEY environment variable", fg='#E57373')
        return None

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    weather_data = fetch_weather_data(url)

    if weather_data:
        # Convert temperature from Kelvin to Celsius
        temp_celsius = round(weather_data['temperature'] - 273.15, 1)
        feels_like_c = round(weather_data['feels_like'] - 273.15, 1)

        print(f"Weather data for {weather_data['city']}: {temp_celsius}°C")

        # Update labels with weather data (keeping label text + adding values)
        text_color = '#E0E0E0'  # Light text for dark theme
        accent_color = '#4A90E2'  # Blue accent for temperature
        error_color = '#E57373'  # Light red for errors

        weather_labels['city'].config(
            text=f"City: {weather_data['city']}", fg=text_color)
        weather_labels['temperature'].config(
            text=f"Temperature: {temp_celsius}°C", fg=accent_color)
        weather_labels['feels_like'].config(
            text=f"Feels Like: {feels_like_c}°C", fg=text_color)
        weather_labels['main'].config(
            text=f"Main: {weather_data['main']}", fg=text_color)
        weather_labels['description'].config(
            text=f"Description: {weather_data['description'].title()}", fg=text_color)
        weather_labels['humidity'].config(
            text=f"Humidity: {weather_data['humidity']}%", fg=text_color)
        weather_labels['wind_speed'].config(
            text=f"Wind Speed: {weather_data['wind_speed']} m/s", fg=text_color)
    else:
        print("Failed to fetch weather data.")
        # Show error message while keeping label text
        error_color = '#E57373'
        text_color = '#E0E0E0'
        weather_labels['city'].config(
            text="City: Failed to fetch weather data. Please try again.", fg=error_color)
        weather_labels['temperature'].config(
            text="Temperature: ", fg=text_color)
        weather_labels['feels_like'].config(text="Feels Like: ", fg=text_color)
        weather_labels['main'].config(text="Main: ", fg=text_color)
        weather_labels['description'].config(
            text="Description: ", fg=text_color)
        weather_labels['humidity'].config(text="Humidity: ", fg=text_color)
        weather_labels['wind_speed'].config(text="Wind Speed: ", fg=text_color)


def main():
    """Main function to initialize and run the weather application."""

    # Basic configuration for window with dark theme
    root = Tk()
    root.title("☀️ Desktop Weather App")
    root.geometry("700x500")
    root.configure(bg='#1E1E1E')  # Dark background
    root.resizable(True, True)

    # Create weather display labels
    weather_labels = create_weather_display(root)

    # Create search widgets and get text entry and button references
    # We'll set the command after text_entry is created
    text_entry, search_button = create_search_widgets(root, None)

    # Set up the search callback after text_entry is created
    def search_callback():
        search_weather(text_entry, weather_labels)

    # Update the search button command
    search_button.config(command=search_callback)

    # Start the GUI event loop
    root.mainloop()


if __name__ == '__main__':
    main()
