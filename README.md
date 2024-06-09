# DGLabMouseListener2.0
郊狼好玩喵~ 监听~键~鼠事件2.0全新升级，增加了大量可选项，允许A,B通道分别输出，添加DIY波形功能
----

本程序必须在电脑上运行，你至少需要一台Windows系统的电脑，其他系统没有测试，理论上linux应该可以用

从零开始的使用教程：

step0：准备工作

1. 下载并安装vscode  [Windows 10 (点我)](https://code.visualstudio.com/docs/?dv=win64user)   [其他系统请自行寻找相应的安装包](https://code.visualstudio.com/Download)   用来修改/运行代码

2. 下载并安装miniconda3 [Windows 10 (点我)](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)   [其他系统请自行寻找相应的安装包](https://docs.anaconda.com/free/miniconda/)   用来自动配置环境

step 1: 创建虚拟环境

1. 打开miniconda3（windows 10用户可以在开始菜单栏边上搜索miniconda3，然后点击打开），在弹出的Miniconda3框中输入conda create --name venv python=3.9(可以从下面复制，记得按回车确定输入), 即可创建一个名为venv的支持python3.9的虚拟环境

```shell
conda create --name venv python=3.9
```

如下图所示

![image](https://github.com/nobody-x-j/images/blob/main/conda_create.png)

按回车确定之后：

![image](https://github.com/nobody-x-j/images/blob/main/conda_create_yes.png)

输入 y， 然后回车

![image](https://github.com/nobody-x-j/images/blob/main/conda_create_success.png)

成功后应该长这样

step 2: 使用vscode下载代码

1. 在弹出的Miniconda3框中输入 code，也可以在开始菜单栏边上搜索vscode

```shell
code
```

![image](https://github.com/nobody-x-j/images/blob/main/code.png)

之后会弹出以下界面：

![image](https://github.com/nobody-x-j/images/blob/main/vscode_starting.png)

2. 选择 打开文件夹 -> 打开或者新建一个你想要存代码的文件夹

![image](https://github.com/nobody-x-j/images/blob/main/vscode_open_folder.png)

打开后应该是这样：

![image](https://github.com/nobody-x-j/images/blob/main/vscode_folder_opened.png)

3. 在打开的界面选择 "Terminal" -> "New Terminal" （英文界面） /  “终端” -> “新建终端” (中文界面) 如果看不到 "Terminal" / “终端” ，请把窗口全屏

![image](https://github.com/nobody-x-j/images/blob/main/vscode_new_terminal.png)

打开后应该是这样：

![image](https://github.com/nobody-x-j/images/blob/main/vscode_terminal_opened.png)

4. 在终端输入 git clone https://github.com/nobody-x-j/DGLabMouseListener2.git 从而复制本代码到之前选择的文件夹

```shell
git clone https://github.com/nobody-x-j/DGLabMouseListener2.git
```

![image](https://github.com/nobody-x-j/images/blob/main/vscode_terminal_clone.png)

按回车确认后终端应该会有如下信息，说明你成功将代码存入你的电脑

![image](https://github.com/nobody-x-j/images/blob/main/vscode_terminal_clone_done.png)

5. 在vscode窗口，按"ctrl + shift + p"(三个键同时按)，在跳出的窗口选择 “Python: Select Interpreter” -> 找到刚刚用miniconda3创建的虚拟环境venv -> "Terminal" -> "New Terminal" （英文界面） /  “终端” -> “新建终端” (中文界面) 此时新的终端的命令输入处最左侧出现（venv）则代表成功启动虚拟环境，否则请重启vscode，再 "Terminal" -> "New Terminal" （英文界面） /  “终端” -> “新建终端” (中文界面)， 若还是失败，请试着在miniconda3界面输入code启动vscode

![image](https://github.com/nobody-x-j/images/blob/main/vscode_ctrl_shift_p.png)

![image](https://github.com/nobody-x-j/images/blob/main/vscode_select_interpreter.png)

成功后的终端：

![image](https://github.com/nobody-x-j/images/blob/main/vscode_venv_success.png)

如果反复测试都不成功，尝试在终端输入：

```shell
conda activate venv
```

![image](https://github.com/nobody-x-j/images/blob/main/vscode_venv_manual_activate.png)

如果还不成功，说明之前的步骤操作有误，请删除miniconda3以及vscode，从step 0 重新开始

step 3: 安装以及设置

以下步骤必须确认终端的命令输入处最左侧出现（venv）方可进行

1. 在终端输入 cd DGLabMouseListener2 切换到目标文件夹

```shell
cd DGLabMouseListener2
```

![image](https://github.com/nobody-x-j/images/blob/main/vscode_cd.png)

按下回车后会看到：

![image](https://github.com/nobody-x-j/images/blob/main/vscode_cd_finish.png)

2. 在终端输入 pip install requests websockets loguru pynput 来安装必要的前置程序包

```shell
pip install requests websockets loguru pynput
```

![image](https://github.com/nobody-x-j/images/blob/main/vscode_pip_install.png)

成功安装应该是这样的：

![image](https://github.com/nobody-x-j/images/blob/main/vscode_pip_install_success.png)

3. 在vscode界面的最左端（如图）

![image](https://github.com/nobody-x-j/images/blob/main/vscode_config.png)

选中config.py，将ws 里面的内容根据OTC控制器显示的内容自行修改（注：OTC控制器是本程序需要配套的手机app，[点此下载](https://github.com/open-toys-controller/open-DGLAB-controller/releases/latest/download/app-release.apk) [OTC控制器官网](https://github.com/open-toys-controller/open-DGLAB-controller/releases/tag/V1.2.0)）

![image](https://github.com/lxyddice/DGLabMouseListener/assets/95132858/7f1879b3-bc43-4e10-b46d-3b0f3319c23e)

4. 链接设备，开启娱乐模式后，在终端输入 python main.py 即可启动

```shell
python main.py
```

点击鼠标就能看到手机app上显示相应通道有输出了

step 4: 再次开始游戏：

安装之后，再次开始游戏，只需要打开miniconda3，输入 code

```shell
code
```

一般默认打开上次的文件夹，如果没有，请选择打开文件夹，选取程序所在文件夹，打开终端，输入：

```shell
cd DGLabMouseListener2
```

然后输入

```shell
python main.py
```

step 5: 一些自定义选项：

在config.py文件中，有大量自定义项目，可阅读注释自行修改

在DIY_patterns.py文件中，可以自定义波形，具体格式请参考DIY_patterns.py文件中的注释


------------------------------------------以下是原来的说明----------------------------------------------


本项目依赖 [https://github.com/open-toys-controller/open-DGLAB-controller](https://github.com/open-toys-controller/open-DGLAB-controller) 的ws协议



请自己写ws地址，改IP就行

日志等级不用改了，很简洁（

i是强度，t是0.1秒

rand是随机化，t一般都是0，因为软件不接受小数，i可以适当填写，比如0.1即为 ±10% 强度

鼠标长按就一直电，T^T

![image](https://github.com/lxyddice/DGLabMouseListener/assets/95132858/7f1879b3-bc43-4e10-b46d-3b0f3319c23e)

<code>
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
</code>

----

## 2.py 把 ws 转为 http

需要 py > 3.8 

pip install quart

然后把25行的ws地址的ip改成你自己的，然后运行即可

访问http://127.0.0.1:5000/s?i=50&t=10

i 为 强度 t 为 ticks

----
## 题外话

其实本来想着给卡拉比丘增加玩法的，比如开枪、换弹时......但是卡拉比丘有反作弊，会屏蔽程序获得键鼠的操作，写完才发现的QAQ

搜了一圈没人写这个玩法，那就我试试吧（） 写的很烂，求教

写的时候其实也开着>_< 被电的很爽（

## 请注意身体，不要玩过头了喵
