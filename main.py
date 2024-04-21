import asyncio
import json
import time
from pynput import mouse, keyboard
import websockets
from loguru import logger
import tracemalloc
import sys
import random

tracemalloc.start()
# 请不要修改keyBoard的配置，因为实在没整明白键盘事件的异步，越写越懵，求pr QAQ
# 请自己写ws地址
# 日志等级不用改了，很简洁（
# i是强度，t是0.1秒
global config
config = {
    "ws": "ws://192.168.137.208:60536/1",
    "level": "INFO",
    "rand": {
        "t": 0,
        "i": 0.2
    },
    "mouseClick": {
        "left": {"i": 50, "t": 1},
        "right": {"i": 60, "t": 1}
    },
    "keyBoard": {}
}

class CaoFanNiController:
    def __init__(self, websocket):
        self.websocket = websocket

    async def send_caoFanNi(self, i, ticks):
        event = asyncio.Event()
        await self.caoFanNi(i, ticks, event)
        await event.wait()

    async def caoFanNi(self, i, ticks, event):
        global config
        if "rand" in config and config["rand"].get("t", 0) > 0 or config["rand"].get("i", 0) > 0:
            
            ticks_variation = ticks * random.uniform(-config["rand"]["t"], config["rand"]["t"])
            i_variation = i * random.uniform(-config["rand"]["i"], config["rand"]["i"])
            
            new_ticks = int(ticks + ticks_variation)
            new_i = int(i + i_variation)
            
            logger.warning(f"强度{i} 调整为{new_i} 持续{new_ticks/10}秒")
            await self.websocket.send(json.dumps({"cmd": "set_pattern", "pattern_name": "冲击", "intensity": new_i, "ticks": new_ticks}))
        else:
            logger.warning(f"强度{i} 持续{ticks/10}秒")
            await self.websocket.send(json.dumps({"cmd": "set_pattern", "pattern_name": "冲击", "intensity": i, "ticks": ticks}))
        
        await asyncio.sleep(new_ticks/10 if "new_ticks" in locals() else ticks/10)
        event.set()

class MouseListener:
    def __init__(self, websocket, caoFanNiController):
        self.button_pressed = None
        self.press_time = None
        self.websocket = websocket
        self.caoFanNiController = caoFanNiController
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def on_click(self, x, y, button, pressed):
        if pressed:
            if self.button_pressed is None:
                self.button_pressed = button
                self.press_time = time.time()
                logger.debug(f"{self.button_pressed} button pressed")
        else:
            if self.button_pressed == button:
                if self.press_time is not None:
                    elapsed_time = time.time() - self.press_time
                    button_name = 'left' if button == mouse.Button.left else 'right'
                    if elapsed_time > config['mouseClick'][button_name]['t']:
                        logger.debug(f"{self.button_pressed} button long pressed")
                        asyncio.run_coroutine_threadsafe(
                            self.caoFanNiController.send_caoFanNi(config['mouseClick'][button_name]['i'], config['mouseClick'][button_name]['t'] * 10),
                            loop
                        )
                    logger.debug(f"{self.button_pressed} button released")
                self.button_pressed = None
                self.press_time = None

    async def run(self):
        try:
            while True:
                if self.button_pressed and self.press_time:
                    try:
                        elapsed_time = time.time() - self.press_time
                        if elapsed_time > 0.1:
                            button_name = 'left' if self.button_pressed == mouse.Button.left else 'right'
                            logger.debug(f"{self.button_pressed} button starts long pressing")
                            await self.caoFanNiController.send_caoFanNi(config['mouseClick'][button_name]['i'], config['mouseClick'][button_name]['t'])
                            time.sleep(0.1)
                    except:
                        # 才不告诉你，这里有小bug，出了就电你一下喵~
                        await self.caoFanNiController.send_caoFanNi(config['mouseClick'][button_name]['i'], config['mouseClick'][button_name]['t'])
                else:
                    self.press_time = None
        except KeyboardInterrupt:
            self.listener.stop()


class KeyListener:
    def __init__(self, loop, caoFanNiController):
        self.loop = loop
        self.caoFanNiController = caoFanNiController
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name
        if key_name in config['keyBoard']:
            logger.debug(f"{key_name} key pressed")
            
            asyncio.run(
                self.caoFanNiController.send_caoFanNi(config['keyBoard'][key_name]['i'], config['keyBoard'][key_name]['t']),
                self.loop
            )


    def schedule_send_caoFanNi(self, key_name):
        logger.debug("start")
        asyncio.ensure_future(
            self.caoFanNiController.send_caoFanNi(config['keyBoard'][key_name]['i'], config['keyBoard'][key_name]['t'] * 10)
        )


    def on_release(self, key):
        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name
        if key_name in self.key_pressed:
            logger.debug(f"{key_name} key released")
            del self.key_pressed[key_name]

    async def run(self):
        pass

async def main_fn(ws):
    try:
        logger.info(f"尝试连接至{ws}")
        async with websockets.connect(ws) as websocket:
            loop = asyncio.get_event_loop()
            logger.success("Websocket连接成功")
            caoFanNiController = CaoFanNiController(websocket)
            mouse_listener = MouseListener(websocket, caoFanNiController)
            key_listener = KeyListener(loop, caoFanNiController)
            await asyncio.gather(mouse_listener.run(), key_listener.run())
    except websockets.exceptions.ConnectionClosed:
        logger.error("WebSocket连接已关闭")
    except Exception as e:
        logger.error(f"发生错误：{e}")
        
logger.remove()
handler_id = logger.add(sys.stderr, level=config["level"])
loop = asyncio.get_event_loop()
if loop.is_running():
    logger.debug("警告：事件循环已经在运行中")
else:
    loop.run_until_complete(main_fn(config["ws"]))
