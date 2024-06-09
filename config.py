"""
设置文档,所有的自定义设置都在这了
!!! 一定要确保打开OTC控制器的手机和运行本程序的电脑处在同一个wifi内部 !!!
!!! 一定要记得修改"ws" !!!
!!! "ws" 里的 :60536/1 一定要保留，不然连接不上 !!!

"""

config = {
    "ws": "ws://192.168.8.129:60536/1", # 必须修改！必须修改！必须修改！
    "level": "INFO",
    "rand": {"t": 0, "i": 0.2},
    "mouseClick": {"left": {"i": 60, "t": 1}, "right": {"i": 80, "t": 1}},

    # 2.0 新增内容
    # 鼠标按键分为左键"left_click"，右键"right_click"，长按"long_click"，长按的时间判定阈值是"mouseClick"中"left"或"right"的“t”值，默认为1秒
    # 鼠标左键为一般事件，按下触发短暂，普通强度
    # 鼠标右键，长按为特殊事件，按下会有更大惩罚，高强度，长时间，此外同时会永久导致之后的所有按键强度和时间增加，
    # 可以根据自己喜好，随意添加或者修改按键
    "keyBoard_d": ["a","s","d","w","e","g","v","z","x","c","space","shift","up","down","left","right"], # 一般键盘按键，一般是方向键，交互键，确定键，按下触发短暂，普通强度
    "keyBoard_r": ["r","enter","esc"], # 特殊键盘按键，如换弹，菜单，按下会有更大惩罚，高强度，长时间，此外同时会永久导致之后的所有按键强度和时间增加，
    "channels":{                       # 每一种按键所对应的通道，可以填"A","B","both" <- 注意大小写，以及引号是英文引号，建议直接复制来填写
                "right_click": "A",
                "left_click": "A",
                "long_click": "both",   
                "keyboard_d": "A",
                "keyboard_r": "both",
    },
    "channel_level_factor": {"A": 1, "B": 0.1,}, # 鉴于不同道具输出的强度不同，为不同通道设置了等级系数， ##默认值：A通道：橡胶环 B通道：金属塞子
    "patterns": {                       # 对不同事件采用的波形，需注意波形名称必须正确，否则将一律视为“经典” 
                "right_click": "flirting_1",
                "left_click": "冲击",
                "long_click": "榨汁",   ## 注意，添加DIY的波形时，记得要在"priority"为它附加相应的优先级,否则优先级默认为1
                "keyboard_d": "压缩",
                "keyboard_r": "经典",
                }, 
    "priority": {"经典": 3,             # 输出波形的优先级，只有优先级大于等于当前正在输出的波形，才会输出           
                 "炼狱2.0": 0,
                 "打屁股":0,
                 "冲击": 1,   
                 "flirting_1":2,        ## 注意，添加DIY的波形时，记得要在"priority"为它附加相应的优先级,否则优先级默认为1
                 "flirting_2":0,
                 "榨汁":4,
                 "压缩":0
                 }, 
    "output_factor":{"right_click":1, "left_click":0.8, "long_click":1, "keyboard_d":0.8, "keyboard_r":1.2}, # 不同事件输出强度的调整因子
    "initial_states":{"mouse_level":30, "keyboard_level":30,  # 初始输出强度 ##输出强度范围为0~100，强度为100时对应OTC控制器中设定的通道最大强度
                      "mouse_tick":10, "keyboard_tick":10},   # 初始输出时间，单位tick，10tick为1秒
    "soft_cap": {"mouse":50, "keyboard":40}, # 当强度抵达soft_cap之后提升速度大幅度减慢
    "incerase_soft_cap": {"mouse_threshold":30, "keyboard_threshold":30, "mouse_delta":3, "ketboard_delta":2}, # 当目前level大于soft_cap + threshold 时，soft_cap提升delta
    "hard_cap": {"mouse":70, "keyboard":60}, # 当强度抵达hard_cap之后，不再提升
    "time_factor":{                          # 事件的时间惩罚倍率
                    "left_click": 1,
                    "long_click": 8, 
                    "right_click": 8, 
                    "keyboard_d": 1,
                    "keyboard_r": 6,
                }, 
    "delta_value_mouse":{"long_click_t":1, "long_click_level": 1, "right_click_t":1, "right_click_level": 1 }, # 鼠标特殊事件触发的永久时间/强度增值 ## 长按默认和按下时间挂钩，如果要用这里的值，需要修改代码
    "delta_value_keyBoard":{"r_key_t":1, "r_key_level":2}, # 键盘特殊事件触发的永久时间/强度增值
    # "max_intensity": {},
}