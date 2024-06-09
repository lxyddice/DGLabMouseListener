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
from DIY_patterns import DIY_patterns
from config import config

tracemalloc.start()

class MouseListener:
    def __init__(self, websocket, caoFanNiController):
        self.button_pressed = None
        self.press_time = None
        self.websocket = websocket
        self.caoFanNiController = caoFanNiController
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()
        self.level = config["initial_states"]["mouse_level"]
        self.tick = config["initial_states"]["mouse_tick"]
        self.soft_cap = config["soft_cap"]["mouse"]

    def on_click(self, x, y, button, pressed):
        if pressed:
            if self.button_pressed is None:
                self.button_pressed = button
                self.press_time = time.time()
                logger.debug(f"{self.button_pressed} button pressed")
                button_name = 'left' if button == mouse.Button.left else 'right'
                factor = config["output_factor"]["left_click"]
                channel = config["channels"]["left_click"]
                if channel == "both":
                    asyncio.run_coroutine_threadsafe(
                        self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                            1000, config["patterns"]["left_click"], "A"),
                        self.caoFanNiController.loop
                    )
                    asyncio.run_coroutine_threadsafe(
                        self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                            1000, config["patterns"]["left_click"], "B"),
                        self.caoFanNiController.loop
                    )
                else:
                    asyncio.run_coroutine_threadsafe(
                        self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                            1000, config["patterns"]["left_click"], channel),
                        self.caoFanNiController.loop
                    )

        else:
            if self.button_pressed == button:
                if self.press_time is not None:
                    elapsed_time = time.time() - self.press_time
                    button_name = 'left' if button == mouse.Button.left else 'right'
                    if elapsed_time > config['mouseClick'][button_name]['t']:
                        self.level += elapsed_time
                        self.tick += elapsed_time
                        factor = config["output_factor"]["long_click"]
                        channel = config["channels"]["long_click"]
                        if channel == "both":
                            asyncio.run_coroutine_threadsafe(
                                self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                                    self.tick * config["time_factor"]["long_click"], 
                                                                    config["patterns"]["long_click"], "A"),
                                self.caoFanNiController.loop
                            )
                            asyncio.run_coroutine_threadsafe(
                                self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                                    self.tick * config["time_factor"]["long_click"], 
                                                                    config["patterns"]["long_click"], "B"),
                                self.caoFanNiController.loop
                            )
                        else:
                            asyncio.run_coroutine_threadsafe(
                                self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                                    self.tick * config["time_factor"]["long_click"], 
                                                                    config["patterns"]["long_click"], channel),
                                self.caoFanNiController.loop
                            )
                    
                    else:
                        if button_name == "right":
                            self.level += config["delta_value_mouse"]["right_click_level"]
                            self.tick += config["delta_value_mouse"]["right_click_t"]
                            factor = config["output_factor"]["right_click"]
                            channel = config["channels"]["right_click"]
                            if channel == "both":
                                asyncio.run_coroutine_threadsafe(
                                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                                        self.tick * config["time_factor"]["right_click"], 
                                                                        config["patterns"]["right_click"], "A"),
                                    self.caoFanNiController.loop
                                )
                                asyncio.run_coroutine_threadsafe(
                                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                                        self.tick * config["time_factor"]["right_click"], 
                                                                        config["patterns"]["right_click"], "B"),
                                    self.caoFanNiController.loop
                                )
                            else:
                                asyncio.run_coroutine_threadsafe(
                                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                                        self.tick * config["time_factor"]["right_click"], 
                                                                        config["patterns"]["right_click"], channel),
                                    self.caoFanNiController.loop
                                )
                        else:
                            factor = config["output_factor"]["left_click"]
                            channel = config["channels"]["left_click"]
                            if channel == "both":
                                asyncio.run_coroutine_threadsafe(
                                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                                        self.tick * config["time_factor"]["left_click"], 
                                                                        config["patterns"]["left_click"], "A"),
                                    self.caoFanNiController.loop
                                )
                                asyncio.run_coroutine_threadsafe(
                                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                                        self.tick * config["time_factor"]["left_click"], 
                                                                        config["patterns"]["left_click"], "B"),
                                    self.caoFanNiController.loop
                                )
                            else:
                                asyncio.run_coroutine_threadsafe(
                                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                                        self.tick * config["time_factor"]["left_click"], 
                                                                        config["patterns"]["left_click"], channel),
                                    self.caoFanNiController.loop
                                )
                        
                    logger.debug(f"{self.button_pressed} button released")
                self.button_pressed = None
                self.press_time = None

        if self.level - self.soft_cap >= config["incerase_soft_cap"]["mouse_threshold"]:
            if self.soft_cap < config["hard_cap"]["mouse"]: 
                self.level = self.soft_cap
                self.soft_cap += config["incerase_soft_cap"]["mouse_delta"]
                logger.info(f"强度上限已提升,当前强度{self.level},当前软上限{self.soft_cap}")
                    
            else:
                self.level = self.soft_cap
                logger.info("已到达强度上限")
            
    async def run(self):
        try:
            while True:
                await asyncio.sleep(0.1)
        except KeyboardInterrupt:
            self.listener.stop()


class KeyListener:
    def __init__(self, loop, caoFanNiController):
        self.loop = loop
        self.caoFanNiController = caoFanNiController
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        self.level = config["initial_states"]["keyboard_level"]
        self.tick = config["initial_states"]["keyboard_tick"]
        self.soft_cap = config["soft_cap"]["keyboard"]

    def on_press(self, key):
        try:
            key_name = key.char
        except AttributeError:
            key_name = key.name
        if key_name in config['keyBoard_d']:
            logger.debug(f"{key_name} key pressed")
            factor = config["output_factor"]["keyboard_d"]
            channel = config["channels"]["keyboard_d"]
            if channel == "both":
                asyncio.run_coroutine_threadsafe(
                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                        self.tick * config["time_factor"]["keyboard_d"], 
                                                        config["patterns"]["keyboard_d"], "A"),
                    self.loop
                )
                asyncio.run_coroutine_threadsafe(
                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                        self.tick * config["time_factor"]["keyboard_d"], 
                                                        config["patterns"]["keyboard_d"], "B"),
                    self.loop
                )
            else:
                asyncio.run_coroutine_threadsafe(
                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                        self.tick * config["time_factor"]["keyboard_d"], 
                                                        config["patterns"]["keyboard_d"], channel),
                    self.loop
                )
        elif key_name in config['keyBoard_r']:
            self.level += 3
            self.tick += 1
            factor = config["output_factor"]["keyboard_r"]
            channel = config["channels"]["keyboard_r"]
            if channel == "both":
                asyncio.run_coroutine_threadsafe(
                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                        self.tick * config["time_factor"]["keyboard_r"], 
                                                        config["patterns"]["keyboard_r"], "A"),
                    self.loop
                )
                asyncio.run_coroutine_threadsafe(
                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                        self.tick * config["time_factor"]["keyboard_r"], 
                                                        config["patterns"]["keyboard_r"], "B"),
                    self.loop
                )
            else:
                asyncio.run_coroutine_threadsafe(
                    self.caoFanNiController.send_caoFanNi(int(min(self.level, self.soft_cap) * factor),
                                                        self.tick * config["time_factor"]["keyboard_r"], 
                                                        config["patterns"]["keyboard_r"], channel),
                    self.loop
                )

        if self.level - self.soft_cap >= config["incerase_soft_cap"]["keyboard_threshold"]:
            if self.soft_cap < config["hard_cap"]["keyboard"]:
                self.level = self.soft_cap
                self.soft_cap += config["incerase_soft_cap"]["ketboard_delta"]
                logger.info(f"强度上限已提升,当前强度{self.level},当前软上限{self.soft_cap}")

            else:
                self.level = self.soft_cap
                logger.info("已到达强度上限")
        

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
        self.A_priority = -1
        self.B_priority = -1
        self.A_high_priority_tick = 0
        self.B_high_priority_tick = 0
        self.A_high_priority_start = 0
        self.B_high_priority_start = 0
        self.init_priority()
        
    def init_priority(self):
        for pattern_name in list(DIY_patterns.keys()):
            if not pattern_name in list(config["priority"].keys()):
                config["priority"][pattern_name] = 1

    async def send_caoFanNi(self, i, ticks, pattern_name, channel="A"):
        if i == 61:
            print("inside")
        event = asyncio.Event()
        await self.caoFanNi(i, ticks, event, pattern_name, channel)
        await event.wait()

    async def caoFanNi(self, i, ticks, event, pattern_name, channel):
        working_channel = None
        if time.time() - self.A_high_priority_start >= self.A_high_priority_tick / 10:
            self.A_priority = -1
        if time.time() - self.B_high_priority_start >= self.B_high_priority_tick / 10:
            self.B_priority = -1
        if channel == "A":
            if config["priority"][pattern_name] >= self.A_priority: 
                self.A_priority = config["priority"][pattern_name]
                self.A_high_priority_tick = ticks
                self.A_high_priority_start = time.time()
                working_channel = "A"
        if channel == "B":
            if config["priority"][pattern_name] >= self.B_priority: 
                self.B_high_priority_start_priority = config["priority"][pattern_name]
                self.B_high_priority_tick = ticks
                self.B_high_priority_start = time.time()
                working_channel = "B"

        if not working_channel is None:
            if working_channel == "A":
                n_pattern = "A_pattern_name"
                pattern_units = "A_pattern_units"
                n_intensity = "A_intensity"
                n_ticks = "A_ticks"
            if working_channel == "B":
                n_pattern = "B_pattern_name"
                pattern_units = "B_pattern_units"
                n_intensity = "B_intensity"
                n_ticks = "B_ticks"

            if "rand" in config and config["rand"].get("t", 0) > 0 or config["rand"].get("i", 0) > 0:
                ticks_variation = ticks * random.uniform(-config["rand"]["t"], config["rand"]["t"])
                # ticks_variation = 0
                i_variation = i * random.uniform(-config["rand"]["i"], config["rand"]["i"])

                new_ticks = int(ticks + ticks_variation)
                new_i = int((i + i_variation) * config["channel_level_factor"][working_channel])

                logger.warning(f"通道{working_channel} 强度{i} 调整为{new_i} 持续{new_ticks/10}秒")
                if pattern_name in list(DIY_patterns.keys()):
                    await self.websocket.send(json.dumps({"cmd": "set_pattern", pattern_units: DIY_patterns[pattern_name],
                                                    n_intensity: new_i, n_ticks: new_ticks}))
                else:
                    await self.websocket.send(json.dumps({"cmd": "set_pattern", n_pattern: pattern_name,
                                                        n_intensity: new_i, n_ticks: new_ticks}))
            else:
                logger.warning(f"通道{working_channel} 强度{i} 持续{ticks/10}秒")
                i = int(i * config["channel_level_factor"][working_channel])
                if pattern_name in list(DIY_patterns.keys()):
                    await self.websocket.send(json.dumps({"cmd": "set_pattern", pattern_units: DIY_patterns[pattern_name],
                                                    n_intensity: i, n_ticks: ticks}))
                else:
                    await self.websocket.send(json.dumps({"cmd": "set_pattern", n_pattern: pattern_name,
                                                        n_intensity: i, n_ticks: ticks}))

        await asyncio.sleep(new_ticks/10 if "new_ticks" in locals() else ticks/10)
        event.set()

    async def get_max_intensive(self):
        event = asyncio.Event()
        await self.websocket.send(json.dumps({"cmd": "get_max_intensity"}))
        max_int = await self.websocket.recv()
        self.A_max, self.B_max = eval(max_int)["A_max"],  eval(max_int)["B_max"]
        await event.wait()
    
    async def send_change_max(self, delta):
        event = asyncio.Event()
        await self.websocket.send(json.dumps({"cmd":  "change_max_intensity",  "delta_intensity":delta}))
        event.set()

async def main_fn(ws):
    try:
        logger.info(f"尝试连接至{ws}")
        async with websockets.connect(ws) as websocket:
            loop = asyncio.get_event_loop()
            logger.success("Websocket连接成功")
            caoFanNiController = CaoFanNiController(websocket)
            # war_thunder = WarThunder(websocket, caoFanNiController, loop)
            key_listener = KeyListener(loop, caoFanNiController)
            mouse_listener = MouseListener(websocket, caoFanNiController)
            # await asyncio.gather(key_listener.run(), mouse_listener.run(), war_thunder.run())  ## War Thunder 没测试过，先注释了
            await asyncio.gather(key_listener.run(), mouse_listener.run())
    except websockets.exceptions.ConnectionClosed:
        logger.error("WebSocket连接已关闭")
    except Exception as e:
        logger.error(f"发生错误：{e}")


if __name__ == "__main__":
    logger.remove()
    handler_id = logger.add(sys.stderr, level=config["level"])
    loop = asyncio.get_event_loop()
    if loop.is_running():
        logger.debug("警告：事件循环已经在运行中")
    else:
        loop.run_until_complete(main_fn(config["ws"]))
