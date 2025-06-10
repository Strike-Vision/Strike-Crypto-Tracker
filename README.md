# Flask Crypto Tracker

A simple Flask web application to track cryptocurrency prices and visualize candlestick charts using yfinance and Plotly.

## Features
- Track any cryptocurrency symbol against a chosen currency (e.g., BTC-USD, ETH-EUR).
- Select custom date ranges or view the past 24 hours.
- Choose data intervals: 5m, 15m, 30m, 1h, or 1d.
- Interactive candlestick and volume charts rendered with Plotly.
- Responsive and minimal UI.

## Project Structure
```
flask-crypto-tracker/
├── app.py                 # Main application logic
├── templates/             # HTML templates for the web interface
│   └── index.html        # Main page with form and chart display
├── static/               # Static files (e.g., CSS for styling)
│   └── style.css
├── tests/                # Test files for the application
│   └── test_app.py
├── requirements.txt       # Required Python packages
├── requirements-dev.txt   # Additional packages for development and testing
└── LICENSE               # MIT License file
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Strike-Vision/strike-crypto.git
   cd strike-crypto
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. For development and testing, install additional dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Usage
1. Run the Flask app:
   ```bash
   python app.py
   ```
   or
   ```bash
   flask run
   ```

2. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. Use the form to enter a crypto symbol (e.g., BTC-USD), currency, date range, and interval. Submit to view the interactive candlestick and volume charts.

## Testing
Run the tests using pytest:
```bash
pytest
```

## Configuration
- The main application logic is in `app.py`.
- Templates are stored in the `templates` directory (e.g., `index.html` for the main page).
- Static files, such as CSS, are in the `static` directory.
- Tests are located in the `tests` directory.

## License
MIT License. See [LICENSE](LICENSE) for details.

## Built With
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [yfinance](https://github.com/ranaroussi/yfinance) - Financial data retrieval
- [Plotly](https://plotly.com/python/) - Interactive charting library