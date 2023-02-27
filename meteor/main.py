from typing import Union
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from services.database import get_sqlite_db

app = FastAPI()

# setup cors
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

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
            <p>See <a href="/docs">here for documentation</a>
        </body>
    </html>
    """

# Weather


@app.get('/weather/')
async def get_weather(start_date: Union[str, None] = None, end_date: Union[str, None] = None):
    """Returns all weather in a date range as JSON.
    By default, it returns all of the last day's weather recordings. 
    """
    # TODO: start date calculations suck. Fix them.
    start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S") \
        if start_date is not None \
        else datetime.strptime(datetime.now(timezone.utc).strftime("%Y-%m-%d 00:00:00"), "%Y-%m-%d 00:00:00")
    start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")

    end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S") \
        if end_date is not None \
        else datetime.now(timezone.utc)
    end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

    # connect to database
    conn = get_sqlite_db(db_path=db_path)
    cursor = conn.cursor()

    # fetch info from database
    query_str = f"""
                   SELECT *
                   FROM weather
                   WHERE DATETIME(created_at) BETWEEN '{start_date_str}' AND '{end_date_str}'
                   ORDER BY created_at DESC;
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


@app.get('/weather/now')
async def get_weather_now():
    """Returns the most recent weather 
    information from the SQLite database.
    """

    # connect to database
    conn = get_sqlite_db(db_path=db_path)
    cursor = conn.cursor()
    query_string = """
        SELECT recording_id, temperature_hum, temperature_pres, humidity, pressure, MAX(created_at) as created_at
        FROM weather;
    """
    cursor.execute(query_string)
    rows = cursor.fetchmany()

    results = [zip(row.keys(), row) for row in rows]

    return {
        "meta": {
            "type": "weather",
        },
        "data": results[0]
    }


@app.get('/weather/average')
async def get_weather_average(start_date: Union[str, None] = None, end_date: Union[str, None] = None):
    """Returns all weather averages in a date range.
    By default, it returns the last days weather.
    """
    # TODO: start date calculations suck. Fix them.
    start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S") \
        if start_date is not None \
        else datetime.strptime(datetime.now(timezone.utc).strftime("%Y-%m-%d 00:00:00"), "%Y-%m-%d 00:00:00")
    start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")

    end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S") \
        if end_date is not None \
        else datetime.now(timezone.utc)
    end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

    # connect to database
    conn = get_sqlite_db(db_path=db_path)
    cursor = conn.cursor()

    # fetch info from database
    query_str = f"""
                    SELECT avg(temperature_hum) temperature_hum,
                           avg(temperature_pres) temperature_pres,
                           avg(humidity) humidity,
                           avg(pressure) pressure
                    FROM weather
                    WHERE DATETIME(created_at) BETWEEN '{start_date_str}' and '{end_date_str}';
                    """
    cursor.execute(query_str)
    rows = cursor.fetchall()

    # zip the results with their row keys
    results = [zip(row.keys(), row) for row in rows]

    # return the data
    return {
        "meta": {
            "type": "weather:average",
            "start_date": start_date_str,
            "end_date": end_date_str
        },
        "data": results
    }
