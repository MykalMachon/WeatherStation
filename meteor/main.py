from typing import Union
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from services.database import get_sqlite_db

app = FastAPI()

# generics to be used throughout
db_path = f"{Path(__file__).parent.resolve().parent.resolve()}/weather.db"


@app.get("/", response_class=HTMLResponse)
async def get_home():
    return """
    <html>
        <head>
            <title>Meteor 🌠</title>
            <style>* { font-family: monospace; }</style>
        </head>
        <body>
            <h1>Meteor API</h1>
            <p>This is the Meteor API used in WeatherStation</p>
        </body>
    </html>
    """


@app.get("/status")
async def get_status():
    return {
        "web": True,
        "data": True,
        "misc": True
    }

# Weather


@app.get('/weather/')
async def get_weather(start_date: Union[str, None] = None, end_date: Union[str, None] = None):
    """Returns all weather in a date range as JSON.
    By default, it returns the last days weather.
    """
    # TODO: start date calculations suck. Fix them.
    start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S") \
        if start_date is not None \
        else datetime.strptime(datetime.now().strftime("%Y-%m-%d 00:00:00"), "%Y-%m-%d 00:00:00")
    start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")

    end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S") \
        if end_date is not None \
        else datetime.now()
    end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

    # connect to database
    conn = get_sqlite_db(db_path=db_path)
    cursor = conn.cursor()

    # fetch info from database
    query_str = f"""
                   SELECT * 
                   FROM weather
                   WHERE DATETIME(created_at) BETWEEN '{start_date_str}' AND '{end_date_str}';
                   """

    cursor.execute(query_str)
    rows = cursor.fetchall()

    # zip the results with their row keys
    results = [zip(row.keys(), row) for row in rows]

    # return the data
    return {
        "meta": {
            "type": "weather",
            "start_date": start_date_str,
            "end_date": end_date_str
        },
        "data": results
    }


@app.get('/weather/temperature')
async def get_temperature():
    return {}


@app.get('/weather/humidity')
async def get_humidity():
    return {}


@app.get('/weather/pressure')
async def get_pressure():
    return {}
