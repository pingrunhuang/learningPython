import websocket
import asyncio
import json
import zlib
from websocket._abnf import ABNF

channels = ["index/candle60s:BTC-USD"]

param = {"op": "subscribe", "args": channels}
str_param = json.dumps(param)

url = "wss://real.okex.com:8443/ws/v3"

# async def get():
#     msg = {"op": "subscribe", "args": ["index/candle60s:BTC-USD"]}
#     async with websockets.connect("wss://real.okex.com:8443/ws/v3") as ws:
#         await ws.send(msg)
#         ret = await ws.recv()
#         ret_str = ret.decode("gbk")
#         with open("response.txt", 'w') as f:
#             f.write(ret_str)

def inflate(data):
    decompress = zlib.decompressobj(
            -zlib.MAX_WBITS  # see above
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

# async def subscribe_without_login(url, channels):
#     async with websockets.connect(url) as websocket:
#         sub_param = {"op": "subscribe", "args": channels}
#         sub_str = json.dumps(sub_param)
#         await  websocket.send(sub_str)
#         print(f"send: {sub_str}")

#         print("receive:")
#         res = await websocket.recv()
#         res = inflate(res)
#         print(f"{res}")

#         res = await websocket.recv()
#         res = inflate(res)
#         print(f"{res}")
# asyncio.get_event_loop().run_until_complete(subscribe_without_login("wss://real.okex.com:8443/ws/v3", ["index/candle60s:BTC-USD"]))


import websocket
from websocket import ABNF
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send(str_param)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())

def on_data(ws, message, ABNF.OPCODE_BINARY, 0):
    res = inflate(message)
    print(res)
    

if __name__ == "__main__":
    websocket.enableTrace(True)

    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              on_data=on_data)
    ws.on_open = on_open
    ws.run_forever()