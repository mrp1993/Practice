import requests
import time
import sqlite3

def sql_connector():
    con = sqlite3.connect("weather_data.db")
    cur = con.cursor()
    return con, cur

def create_table(con , cur):
    cur.execute('''CREATE TABLE IF NOT EXISTS weather
                   (location TEXT, datetime TEXT, temperature_c REAL, humidity INTEGER)''')
    con.commit()

def insert_data(con, cur, data):
    cur.execute("INSERT INTO weather (location, datetime, temperature_c, humidity) VALUES (?, ?, ?, ?)",
                (data["location"], data["datetime"], data["temperature_c"], data["humidity"]))
    con.commit()

def get_weather_data(city, key="your API key"):
    url = "your API url"
    q = city
    querystring = {"key": key, "q": q}
    response = requests.get(url, params=querystring)
    return process_data(response.json())

def process_data(data):
    return {
        "location": data["location"]["name"],
        "datetime": data["location"]["localtime"],
        "temperature_c": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"],
    }


con, cur = sql_connector()
create_table(con, cur)


while True:
    weather_data = get_weather_data("tehran")
    print(weather_data)
    insert_data(con, cur, weather_data)
    time.sleep(5)

