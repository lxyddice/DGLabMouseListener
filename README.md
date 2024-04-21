# DGLabMouseListener
郊狼好玩喵~ 监听~键~鼠事件进行电击，可自定义配置强度和时间，来进行一些奇奇怪怪的play吧~
----

本项目依赖 [https://github.com/open-toys-controller/open-DGLAB-controller](https://github.com/open-toys-controller/open-DGLAB-controller) 的ws协议

请不要修改keyBoard的配置，因为实在没整明白键盘事件的异步，越写越懵，求pr QAQ

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
## 题外话

其实本来想着给卡拉比丘增加玩法的，比如开枪、换弹时......但是卡拉比丘有反作弊，会屏蔽程序获得键鼠的操作，写完才发现的QAQ

搜了一圈没人写这个玩法，那就我试试吧（） 写的很烂，求教

写的时候其实也开着>_< 被电的很爽（

## 请注意身体，不要玩过头了喵
