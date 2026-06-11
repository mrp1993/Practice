import asyncio
import json
from centrifuge import Client, ClientEventHandler, SubscriptionEventHandler

SOCKET_URL = "wss://centrifugo.bitpin.ir/connection/websocket"
CHANNEL = "market:BTC_IRT"

class MyClientHandler(ClientEventHandler):
    async def on_connected(self, event):
        print(f"✅ Connected to Bitpin! Client ID: {event.client}")

    async def on_error(self, event):
        print(f"❌ Client Error: {event.error}")

    async def on_disconnected(self, event):
        print(f"⚠️ Disconnected: {event.reason}")

class MySubscriptionHandler(SubscriptionEventHandler):
    async def on_publication(self, event):
        data = event.pub.data

        # اگر داده bytes بود، decode کن
        if isinstance(data, bytes):
            data = data.decode("utf-8")
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                pass

        print("📈 New Update:")
        if isinstance(data, (dict, list)):
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            print(data)

async def main():
    client = Client(SOCKET_URL, events=MyClientHandler())
    sub = client.new_subscription(CHANNEL, events=MySubscriptionHandler())

    await client.connect()
    await sub.subscribe()

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped by user")



# 📈 New Update:
# {
#   "candles": [
#     {
#       "open": 11370378980.0,
#       "close": 11386231578.0,
#       "low": "11386231578",
#       "high": "11386231578",
#       "volume": "0.00149999",
#       "ts": 1781182680.0,
#       "resolution": "1m",
#       "time": 1781182680000
#     },
#     {
#       "open": 11386231578.0,
#       "close": 11379465211.0,
#       "low": "11379465211",
#       "high": "11379465211",
#       "volume": "0.00119736",
#       "ts": 1781182740.0,
#       "resolution": "1m",
#       "time": 1781182740000
#     },
#     {
#       "open": 11370378980.0,
#       "close": 11370378980.0,
#       "low": "11370378980",
#       "high": "11370378980",
#       "volume": "0.00061750",
#       "ts": 1781182200.0,
#       "resolution": "5m",
#       "time": 1781182200000
#     },
#     {
#       "open": 11370378980.0,
#       "close": 11379465211.0,
#       "low": "11370378980",
#       "high": "11386231578",
#       "volume": "0.00269735",
#       "ts": 1781182500.0,
#       "resolution": "5m",
#       "time": 1781182500000
#     },
#     {
#       "open": 11327716838.0,
#       "close": 11360088034.0,
#       "low": "11315566576",
#       "high": "11362569234",
#       "volume": "0.04504535",
#       "ts": 1781181000.0,
#       "resolution": "15m",
#       "time": 1781181000000
#     },
#     {
#       "open": 11360088034.0,
#       "close": 11379465211.0,
#       "low": "11360088034",
#       "high": "11386231578",
#       "volume": "0.00418276",
#       "ts": 1781181900.0,
#       "resolution": "15m",
#       "time": 1781181900000
#     },
#     {
#       "open": 11413000000.0,
#       "close": 11327716838.0,
#       "low": "11315566576",
#       "high": "11420175957",
#       "volume": "0.16880815",
#       "ts": 1781179200.0,
#       "resolution": "30m",
#       "time": 1781179200000
#     },
#     {
#       "open": 11327716838.0,
#       "close": 11379465211.0,
#       "low": "11315566576",
#       "high": "11386231578",
#       "volume": "0.04922811",
#       "ts": 1781181000.0,
#       "resolution": "30m",
#       "time": 1781181000000
#     },
#     {
#       "open": 11405000000.0,
#       "close": 11327716838.0,
#       "low": "11315566576",
#       "high": "11441079324",
#       "volume": "0.23798552",
#       "ts": 1781177400.0,
#       "resolution": "1h",
#       "time": 1781177400000
#     },
#     {
#       "open": 11327716838.0,
#       "close": 11379465211.0,
#       "low": "11315566576",
#       "high": "11386231578",
#       "volume": "0.04922811",
#       "ts": 1781181000.0,
#       "resolution": "1h",
#       "time": 1781181000000
#     },
#     {
#       "open": 11350000000.0,
#       "close": 11405000000.0,
#       "low": "11319331001",
#       "high": "11422851657",
#       "volume": "0.34774548",
#       "ts": 1781166600.0,
#       "resolution": "3h",
#       "time": 1781166600000
#     },
#     {
#       "open": 11405000000.0,
#       "close": 11379465211.0,
#       "low": "11315566576",
#       "high": "11441079324",
#       "volume": "0.28721363",
#       "ts": 1781177400.0,
#       "resolution": "3h",
#       "time": 1781177400000
#     },
#     {
#       "open": 11350000000.0,
#       "close": 11327716838.0,
#       "low": "11315566576",
#       "high": "11441079324",
#       "volume": "0.59327609",
#       "ts": 1781166600.0,
#       "resolution": "4h",
#       "time": 1781166600000
#     },
#     {
#       "open": 11327716838.0,
#       "close": 11379465211.0,
#       "low": "11315566576",
#       "high": "11386231578",
#       "volume": "0.04922811",
#       "ts": 1781181000.0,
#       "resolution": "4h",
#       "time": 1781181000000
#     },
#     {
#       "open": 11202461541.0,
#       "close": 11350000000.0,
#       "low": "11164848576",
#       "high": "11350000000",
#       "volume": "0.49154599",
#       "ts": 1781145000.0,
#       "resolution": "6h",
#       "time": 1781145000000
#     },
#     {
#       "open": 11350000000.0,
#       "close": 11379465211.0,
#       "low": "11315566576",
#       "high": "11441079324",
#       "volume": "0.63495911",
#       "ts": 1781166600.0,
#       "resolution": "6h",
#       "time": 1781166600000
#     },
#     {
#       "open": 11038579974.0,
#       "close": 11115775579.0,
#       "low": "10829691570",
#       "high": "11273933198",
#       "volume": "4.42435211",
#       "ts": 1781037000.0,
#       "resolution": "1d",
#       "time": 1781123400000
#     },
#     {
#       "open": 11115775579.0,
#       "close": 11379465211.0,
#       "low": "11039613217",
#       "high": "11441079324",
#       "volume": "1.69900112",
#       "ts": 1781123400.0,
#       "resolution": "1d",
#       "time": 1781209800000
#     },
#     {
#       "open": 12644104564.0,
#       "close": 10972186861.0,
#       "low": "10500000000",
#       "high": "12713486656",
#       "volume": "29.88296776",
#       "ts": 1780259400.0,
#       "resolution": "1w",
#       "time": 1780864200000
#     },
#     {
#       "open": 10972186861.0,
#       "close": 11379465211.0,
#       "low": "10733588729",
#       "high": "11450269932",
#       "volume": "15.89870462",
#       "ts": 1780864200.0,
#       "resolution": "1w",
#       "time": 1781469000000
#     },
#     {
#       "open": 13445548222.0,
#       "close": 12644104564.0,
#       "low": "12524856900",
#       "high": "15299888926",
#       "volume": "81.402675689110707909",
#       "ts": 1777581000.0,
#       "resolution": "1M",
#       "time": 1780259400000
#     },
#     {
#       "open": 12644104564.0,
#       "close": 11379465211.0,
#       "low": "10500000000",
#       "high": "12713486656",
#       "volume": "45.77821527",
#       "ts": 1780259400.0,
#       "resolution": "1M",
#       "time": 1782851400000
#     }
#   ],
#   "market": {
#     "id": 1,
#     "code": "BTC_IRT"
#   },
#   "event": "candle_update",
#   "event_time": "2026-06-11T12:59:45.263627Z"
# }