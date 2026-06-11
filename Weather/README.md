# Weather Data Collector

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)
![Requests](https://img.shields.io/badge/HTTP-Requests-green)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange)

A simple Python project that fetches current weather data from the WeatherAPI service and stores it in a local SQLite database at regular intervals.

---

## Overview

This project periodically requests live weather data for a selected city and saves a subset of the response into a local SQLite database.

Stored fields:

- `location`
- `datetime`
- `temperature_c`
- `humidity`

The script currently fetches weather data for **Tehran** and inserts a new row every **5 seconds**.

---

## Features

- Fetch current weather data from WeatherAPI
- Store weather records in SQLite
- Automatically create the database table if it does not exist
- Run continuously in a timed loop
- Save selected weather fields for later analysis

---

## Requirements

To run this project, you need:

- Python 3.x
- `requests`
- Built-in Python modules:
  - `time`
  - `sqlite3`

---

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
