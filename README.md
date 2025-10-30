## Desktop Weather App

Beautiful, minimal desktop app to check today's weather by city. Built with Python `tkinter` and the OpenWeather API.

### Features
- **Clean dark UI** with highlighted temperature
- **Fast search** by city name
- **Robust error handling** and helpful messages

## Getting Started

### Prerequisites
- Python 3.8+
- An OpenWeather API key (free): `https://openweathermap.org/api`

### Install
```bash
pip install -r requirements.txt
```

### Configure your API key
Set an environment variable named `OPENWEATHER_API_KEY`.

PowerShell (Windows):
```powershell
$env:OPENWEATHER_API_KEY = "your_api_key_here"
```

Command Prompt (Windows):
```bat
set OPENWEATHER_API_KEY=your_api_key_here
```

Unix/macOS (bash/zsh):
```bash
export OPENWEATHER_API_KEY=your_api_key_here
```

Alternatively, create a `.env` file (not committed) at the project root:
```env
OPENWEATHER_API_KEY=your_api_key_here
```

### Run the app
```bash
python app.py
```

---

## Build a Windows executable (optional)
If you want a single-file `.exe` for easy distribution on Windows, use the provided script:

```bat
build_executable.bat
```

Make sure your `OPENWEATHER_API_KEY` is set in the environment before building.

---

## Project Structure
```text
app.py                  # Tkinter UI and app entrypoint
weather.py              # HTTP request and response parsing
requirements.txt        # Python dependencies
build_executable.bat    # Helper script to produce a Windows .exe (optional)
.gitignore              # Excludes build artifacts and secrets
```

---

## Notes
- Do not commit your `.env` or API keys to version control.
- The app reads the API key via `OPENWEATHER_API_KEY`.

---

## Troubleshooting
- "API key not configured": ensure `OPENWEATHER_API_KEY` is set in your shell or `.env`.
- Network errors: check your internet connection and try again.





