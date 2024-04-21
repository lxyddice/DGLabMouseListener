from quart import Quart, request
from loguru import logger
import json
import websockets
import asyncio

app = Quart(__name__)

async def caoFanNi(websocket, i, ticks, event):
    logger.warning(f"强度{i} 持续{ticks/10}秒")
    await websocket.send(json.dumps({"cmd": "set_pattern", "pattern_name": "冲击", "intensity": i, "ticks": ticks}))
    await asyncio.sleep(ticks/10)
    event.set()

async def send_caoFanNi(websocket, i, ticks, event):
    await caoFanNi(websocket, i, ticks, event)
    await event.wait()

@app.route("/s")
async def main_fn():
    i = request.args.get("i", type=int, default=20)
    ticks = request.args.get("t", type=int, default=10)
    
    try:
        async with websockets.connect('ws://192.168.137.208:60536/1') as websocket:
            logger.success("Websocket连接成功")
            event = asyncio.Event()
            await send_caoFanNi(websocket, i, ticks, event)
            
    except Exception as e:
        logger.error(e)
        return {"success":False, "message":e}
    return {"success":True}


if __name__ == "__main__":
    app.run()