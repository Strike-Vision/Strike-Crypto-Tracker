from flask import Flask, render_template, request
import yfinance as yf
import json
from datetime import datetime, timedelta
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    symbol = None
    chart_data = None
    start = end = interval = currency = None
    past24 = False
    if request.method == "POST":
        symbol = request.form.get("symbol")
        currency = request.form.get("currency") or "USD"
        interval = request.form.get("interval") or "5m"
        past24 = request.form.get("past24") == "on"
        if past24:
            yf_symbol = f"{symbol.upper()}-{currency.upper()}"
            df = yf.download(
                yf_symbol,
                period="2d",  # Get 2 days to ensure we have enough data
                interval=interval
            )
            # Filter for the last 24 hours
            if not df.empty:
                now = pd.Timestamp.utcnow()
                last_24h = now - pd.Timedelta(hours=24)
                df = df[df.index >= last_24h]
            start = end = None  # Clear dates for template
        else:
            start = request.form.get("start")
            end = request.form.get("end")
            if symbol:
                yf_symbol = f"{symbol.upper()}-{currency.upper()}"
                # Add one day to end date if provided
                yf_end = None
                if end:
                    try:
                        yf_end = (datetime.strptime(end, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
                    except Exception:
                        yf_end = end  # fallback if parsing fails
                df = yf.download(
                    yf_symbol,
                    start=start if start else None,
                    end=yf_end if yf_end else None,
                    interval=interval
                )
        if not df.empty and interval == "1d" and start and end:
            all_days = pd.date_range(start=start, end=end).normalize()
            df.index = pd.to_datetime(df.index).normalize()
            df = df.reindex(all_days)
            df.index.name = 'Date'

        if symbol and currency and 'df' in locals() and not df.empty:
            if isinstance(df.columns[0], tuple):
                df.columns = ['_'.join([str(i) for i in col if i]) for col in df.columns]
            def find_col(name):
                for col in df.columns:
                    if name in col.lower():
                        return col
                raise KeyError(name)
            try:
                chart_data = {
                    "dates": df.index.strftime('%Y-%m-%d %H:%M').tolist() if interval != "1d" else df.index.strftime('%Y-%m-%d').tolist(),
                    "open": df[find_col("open")].tolist(),
                    "high": df[find_col("high")].tolist(),
                    "low": df[find_col("low")].tolist(),
                    "close": df[find_col("close")].tolist(),
                    "volume": df[find_col("volume")].tolist(),
                }
            except KeyError as e:
                print(f"Missing column in data: {e}")
                chart_data = None
    refresh_seconds = 300  # 5 minutes
    return render_template(
        "home.html",
        symbol=symbol,
        currency=currency,
        chart_data=json.dumps(chart_data) if chart_data else None,
        start=start,
        end=end,
        interval=interval,
        past24=past24,
        refresh_seconds=refresh_seconds
    )

@app.route("/about")
def about():
    return render_template("about.html")
