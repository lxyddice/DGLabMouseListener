import asyncio
import json
import re
import time
import requests
import random
import websockets
from loguru import logger
import sys
from pynput import mouse, keyboard
import tracemalloc

tracemalloc.start()

global config
config = {
    "ws": "ws://192.168.10.247:60536/1",
    "level": "INFO",
    "rand": {"t": 0, "i": 0.2},
    "mouseClick": {"left": {"i": 60, "t": 1000}, "right": {"i": 0, "t": 1}},
    "killEvent": {"kill": {"i": 61, "t": 10}, "killed": {"i": 100, "t": 1000}},
    "keyBoard": {}
}

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
                            self.caoFanNiController.send_caoFanNi(config['mouseClick'][button_name]['i'],
                                                                  config['mouseClick'][button_name]['t'] * 10),
                            self.caoFanNiController.loop
                        )
                    logger.debug(f"{self.button_pressed} button released")
                self.button_pressed = None
                self.press_time = None

    async def run(self):
        try:
            while True:
                await asyncio.sleep(0.1)
        except KeyboardInterrupt:
            self.listener.stop()

class WarThunder:
    def __init__(self, websocket, caoFanNiController, loop):
        self.websocket = websocket
        self.caoFanNiController = caoFanNiController
        self.loop = loop
        self.url = "http://localhost:8111/hudmsg?lastEvt=0&lastDmg=0"
        self.id = 0

    def getKilled(self, text):
        strs1 = '玩\t家'
        substring2 = "击\t毁\t了"
        pattern = re.escape(strs1) + r'.*' + re.escape(substring2)
        match = re.search(pattern, text)
        if match:
            return True
        else:
            return False

    def get_stat(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            data = response.json()
            events = data["events"]
            damage = data["damage"]

            for event in events:
                print(event)
            if damage[-1]['id'] > self.id:
                msg = damage[-1]['msg']
                if '玩\t家' in msg:
                    logger.warning(f"Event: {msg} You killed an enemy")
                    if self.getKilled(text=msg):
                        asyncio.run_coroutine_threadsafe(
                            self.caoFanNiController.send_caoFanNi(config['killEvent']['kill']['i'],
                                                                  config['killEvent']['kill']['t'] * 10),
                            self.loop
                        )
                        self.id=damage[-1]['id']
                    else:
                        asyncio.run_coroutine_threadsafe(
                            self.caoFanNiController.send_caoFanNi(config['killEvent']['killed']['i'],
                                                                  config['killEvent']['killed']['t'] * 10),
                            self.loop
                        )
                        self.id=damage[-1]['id']

                else:
                    self.id=damage[-1]['id']

    async def run(self):
        try:
            while True:
                self.get_stat()
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            pass

class CaoFanNiController:
    def __init__(self, websocket):
        self.websocket = websocket
        self.loop = asyncio.get_event_loop()

    async def send_caoFanNi(self, i, ticks):
        if i == 61:
            print("inside")
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
            await self.websocket.send(json.dumps({"cmd": "set_pattern", "pattern_name": "冲击",
                                                  "intensity": new_i, "ticks": new_ticks}))
        else:
            logger.warning(f"强度{i} 持续{ticks/10}秒")
            await self.websocket.send(json.dumps({"cmd": "set_pattern", "pattern_name": "冲击",
                                                  "intensity": i, "ticks": ticks}))

        await asyncio.sleep(new_ticks/10 if "new_ticks" in locals() else ticks/10)
        event.set()

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

            asyncio.run_coroutine_threadsafe(
                self.caoFanNiController.send_caoFanNi(config['keyBoard'][key_name]['i'],
                                                      config['keyBoard'][key_name]['t']),
                self.loop
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
        try:
            while True:
                await asyncio.sleep(0.1)
        except KeyboardInterrupt:
            pass

async def main_fn(ws):
    try:
        logger.info(f"尝试连接至{ws}")
        async with websockets.connect(ws) as websocket:
            loop = asyncio.get_event_loop()
            logger.success("Websocket连接成功")
            caoFanNiController = CaoFanNiController(websocket)
            war_thunder = WarThunder(websocket, caoFanNiController, loop)
            key_listener = KeyListener(loop, caoFanNiController)
            mouse_listener = MouseListener(websocket, caoFanNiController)
            await asyncio.gather(key_listener.run(), war_thunder.run(), mouse_listener.run())
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
