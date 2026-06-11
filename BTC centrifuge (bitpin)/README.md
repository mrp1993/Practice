# BTC Alarm - Bitpin Realtime Price Listener

A simple Python project for receiving realtime BTC price updates from **Bitpin** using **WebSocket/Centrifugo**.

## Overview

This project connects to Bitpin's realtime WebSocket endpoint and subscribes to the `market:BTC_IRT` channel to receive live market publications.

Bitpin WebSocket is **not a plain raw WebSocket feed**.  
It uses the **Centrifugo protocol**, so a dedicated client library is required.

## Features

- Connects to Bitpin realtime WebSocket
- Subscribes to BTC/IRT market channel
- Prints incoming realtime publications
- Ready to be extended into a price alarm bot

## Tech Stack

- Python 3.12
- `asyncio`
- `centrifuge-python`

## Installation

Install the required package using the same Python interpreter you use to run the script:
```powershell
C:/Users/Mr.Mrp/AppData/Local/Programs/Python/Python312/python.exe -m pip install centrifuge-python
