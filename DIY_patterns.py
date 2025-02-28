"""
这里存放了自定义的波形,可随意DIY  注： ## 后内容为注释,用于说明格式 (本注释内容仅服务于完全不会编程的使用者,python熟练者可以完全无视)
建议直接复制粘贴后只修改pattern_intensity 以及 frequency
复制和粘贴时注意缩进,python缩进使用TAB键(Q左边那个)

格式：
DIY_patterns = {           ## DIY_patterns 是一个字典格式的数据
    "flirting_1" : [        ## DIY_patterns 中的每一个子元素的名称是字符串格式,格式为  "（波形名称,可以用中文英文都可以）"  <- (英文引号);  ###注意,DIY波形名称不能和OTC控制器中的波形名称重复
                                其对应内容是一个list,用[](英文方括号)包裹,需注意【】和[]是不同的,只有[]是正确的,且[]必须成对（中间可随意换行）
                {"pattern_intensity":0, "frequency":83},     ## 从这里开始是自定义波形的每一个脉冲元的一根竖条(参考郊狼app里面),每一行代表0.1秒,
                {"pattern_intensity":25, "frequency":71},    ## 同样要注意{}需要是英文大括号,且必须成对,}之后必须有英文逗号
                {"pattern_intensity":50, "frequency":63},    ## "pattern_intensity"是强度,与郊狼app完全一致,
                {"pattern_intensity":75, "frequency":55},    ## "frequency"是频率,单位是HZ,范围是0-100(),!!!注意这里是频率,郊狼app上虽然写的是频率,但是调的是周期,单位是ms
                {"pattern_intensity":100, "frequency":50},   ## 两者换算关系为 Hz = 1000/ms, 郊狼app上显示为10ms,这里就应该是1000/10=100Hz,
                {"pattern_intensity":100, "frequency":45},   ## 郊狼app上显示为20ms,这里就应该是1000/20=50Hz    !!!注意换算！！！
                ......
                ],                                           ## 第一个自定义波形就此结束,注意要加"]"以及","(英文 ] 以及英文 , )
    "flirting_2" : [                                         ## 第二个自定义波形开始,书写规则同上  ###注意,DIY波形名称不能和OTC控制器中的波形名称重复
                {"pattern_intensity":10, "frequency":27},  
                {"pattern_intensity":20, "frequency":39},  
                {"pattern_intensity":30, "frequency":32}, 
                {"pattern_intensity":40, "frequency":34}, 
                ......
                ],                                           ## 这个自定义波形就此结束,注意要加"]"以及","(英文 ] 以及英文 , )
    ......
            }                                                ## DIY_patterns就此结束,注意后面不要加任何内容,也不要换行加任何内容
"""

## 以下为DIY_patterns和几个示例波形

DIY_patterns = {
    "flirting_1" : [ 

                {"pattern_intensity":0, "frequency":83},  
                {"pattern_intensity":25, "frequency":71},  
                {"pattern_intensity":50, "frequency":63}, 
                {"pattern_intensity":75, "frequency":55}, 
                {"pattern_intensity":100, "frequency":50},  
                {"pattern_intensity":100, "frequency":45},  
                {"pattern_intensity":100, "frequency":41}, 
                {"pattern_intensity":0, "frequency":38}, 
                {"pattern_intensity":0, "frequency":35},  
                {"pattern_intensity":0, "frequency":33},
                {"pattern_intensity":0, "frequency":83},  
                {"pattern_intensity":25, "frequency":71},  
                {"pattern_intensity":50, "frequency":63}, 
                {"pattern_intensity":75, "frequency":55}, 
                {"pattern_intensity":100, "frequency":50},  
                {"pattern_intensity":100, "frequency":45},  
                {"pattern_intensity":100, "frequency":41}, 
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":0, "frequency":10}, 
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},  
                {"pattern_intensity":0, "frequency":10},
                {"pattern_intensity":0, "frequency":10}, 
                ],

    "flirting_2" : [ 
                {"pattern_intensity":0, "frequency":25},
                {"pattern_intensity":10, "frequency":27},  
                {"pattern_intensity":20, "frequency":29},  
                {"pattern_intensity":30, "frequency":32}, 
                {"pattern_intensity":40, "frequency":34}, 
                {"pattern_intensity":50, "frequency":37},  
                {"pattern_intensity":60, "frequency":40},  
                {"pattern_intensity":70, "frequency":43}, 
                {"pattern_intensity":80, "frequency":47}, 
                {"pattern_intensity":90, "frequency":52},  
                {"pattern_intensity":100, "frequency":58},
                {"pattern_intensity":0, "frequency":25},
                {"pattern_intensity":10, "frequency":27},  
                {"pattern_intensity":20, "frequency":39},  
                {"pattern_intensity":30, "frequency":32}, 
                {"pattern_intensity":40, "frequency":34}, 
                {"pattern_intensity":50, "frequency":37},  
                {"pattern_intensity":60, "frequency":40},  
                {"pattern_intensity":70, "frequency":43}, 
                {"pattern_intensity":80, "frequency":47}, 
                {"pattern_intensity":90, "frequency":52},  
                {"pattern_intensity":100, "frequency":58},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":0, "frequency":96}, 
                {"pattern_intensity":100, "frequency":92}, 
                {"pattern_intensity":0, "frequency":88}, 
                {"pattern_intensity":100, "frequency":84}, 
                {"pattern_intensity":0, "frequency":80}, 
                {"pattern_intensity":100, "frequency":76}, 
                {"pattern_intensity":0, "frequency":72}, 
                {"pattern_intensity":100, "frequency":68}, 
                {"pattern_intensity":0, "frequency":64}, 
                {"pattern_intensity":100, "frequency":60}, 
                {"pattern_intensity":0, "frequency":56}, 
                {"pattern_intensity":100, "frequency":52}, 
                {"pattern_intensity":0, "frequency":48}, 
                {"pattern_intensity":100, "frequency":44}, 
                {"pattern_intensity":0, "frequency":40}, 
                {"pattern_intensity":100, "frequency":36}, 
                {"pattern_intensity":0, "frequency":32}, 
                {"pattern_intensity":0, "frequency":10},  
                {"pattern_intensity":0, "frequency":10},  
                {"pattern_intensity":0, "frequency":10},
                ],

    "压缩" : [ 
                {"pattern_intensity":100, "frequency":14},
                {"pattern_intensity":100, "frequency":16},  
                {"pattern_intensity":100, "frequency":18},  
                {"pattern_intensity":100, "frequency":21}, 
                {"pattern_intensity":100, "frequency":23}, 
                {"pattern_intensity":100, "frequency":25},  
                {"pattern_intensity":100, "frequency":28}, 
                {"pattern_intensity":100, "frequency":30}, 
                {"pattern_intensity":100, "frequency":32}, 
                {"pattern_intensity":100, "frequency":35}, 
                {"pattern_intensity":100, "frequency":38},  
                {"pattern_intensity":100, "frequency":100}, 
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                {"pattern_intensity":100, "frequency":100},
                ],

    "榨汁" : [ 
                {"pattern_intensity":100, "frequency":100},  
                {"pattern_intensity":100, "frequency":99},  
                {"pattern_intensity":100, "frequency":98}, 
                {"pattern_intensity":100, "frequency":97}, 
                {"pattern_intensity":100, "frequency":96},  
                {"pattern_intensity":100, "frequency":95},  
                {"pattern_intensity":100, "frequency":94}, 
                {"pattern_intensity":100, "frequency":93}, 
                {"pattern_intensity":100, "frequency":92},  
                {"pattern_intensity":100, "frequency":91},
                {"pattern_intensity":100, "frequency":90},  
                {"pattern_intensity":100, "frequency":89},  
                {"pattern_intensity":100, "frequency":88}, 
                {"pattern_intensity":100, "frequency":87}, 
                {"pattern_intensity":100, "frequency":86},  
                {"pattern_intensity":100, "frequency":85},  
                {"pattern_intensity":100, "frequency":84}, 
                {"pattern_intensity":100, "frequency":83}, 
                {"pattern_intensity":100, "frequency":82},  
                {"pattern_intensity":100, "frequency":81},
                {"pattern_intensity":100, "frequency":80},  
                {"pattern_intensity":100, "frequency":79},  
                {"pattern_intensity":100, "frequency":78}, 
                {"pattern_intensity":100, "frequency":77}, 
                {"pattern_intensity":100, "frequency":76},  
                {"pattern_intensity":100, "frequency":75},  
                {"pattern_intensity":100, "frequency":74}, 
                {"pattern_intensity":100, "frequency":73}, 
                {"pattern_intensity":100, "frequency":72},  
                {"pattern_intensity":100, "frequency":71},
                {"pattern_intensity":100, "frequency":70},  
                {"pattern_intensity":100, "frequency":69},  
                {"pattern_intensity":100, "frequency":68}, 
                {"pattern_intensity":100, "frequency":67}, 
                {"pattern_intensity":100, "frequency":66},  
                {"pattern_intensity":100, "frequency":65},  
                {"pattern_intensity":100, "frequency":64}, 
                {"pattern_intensity":100, "frequency":63}, 
                {"pattern_intensity":100, "frequency":62},  
                {"pattern_intensity":100, "frequency":61},
                {"pattern_intensity":100, "frequency":60},  
                {"pattern_intensity":100, "frequency":59},  
                {"pattern_intensity":100, "frequency":58}, 
                {"pattern_intensity":100, "frequency":57}, 
                {"pattern_intensity":100, "frequency":56},  
                {"pattern_intensity":100, "frequency":55},  
                {"pattern_intensity":100, "frequency":54}, 
                {"pattern_intensity":100, "frequency":53}, 
                {"pattern_intensity":100, "frequency":52},  
                {"pattern_intensity":100, "frequency":51},
                {"pattern_intensity":100, "frequency":50},  
                {"pattern_intensity":100, "frequency":51},  
                {"pattern_intensity":100, "frequency":52}, 
                {"pattern_intensity":100, "frequency":53}, 
                {"pattern_intensity":100, "frequency":54},  
                {"pattern_intensity":100, "frequency":55},  
                {"pattern_intensity":100, "frequency":56}, 
                {"pattern_intensity":100, "frequency":57}, 
                {"pattern_intensity":100, "frequency":58},  
                {"pattern_intensity":100, "frequency":59},
                {"pattern_intensity":100, "frequency":60},  
                {"pattern_intensity":100, "frequency":61},  
                {"pattern_intensity":100, "frequency":62}, 
                {"pattern_intensity":100, "frequency":63}, 
                {"pattern_intensity":100, "frequency":64},  
                {"pattern_intensity":100, "frequency":65},  
                {"pattern_intensity":100, "frequency":66}, 
                {"pattern_intensity":100, "frequency":67}, 
                {"pattern_intensity":100, "frequency":68},  
                {"pattern_intensity":100, "frequency":69},
                {"pattern_intensity":100, "frequency":70},  
                {"pattern_intensity":100, "frequency":71},  
                {"pattern_intensity":100, "frequency":72}, 
                {"pattern_intensity":100, "frequency":73}, 
                {"pattern_intensity":100, "frequency":74},  
                {"pattern_intensity":100, "frequency":75},  
                {"pattern_intensity":100, "frequency":76}, 
                {"pattern_intensity":100, "frequency":77}, 
                {"pattern_intensity":100, "frequency":78},  
                {"pattern_intensity":100, "frequency":79},
                {"pattern_intensity":100, "frequency":80},  
                {"pattern_intensity":100, "frequency":81},  
                {"pattern_intensity":100, "frequency":82}, 
                {"pattern_intensity":100, "frequency":83}, 
                {"pattern_intensity":100, "frequency":84},  
                {"pattern_intensity":100, "frequency":85},  
                {"pattern_intensity":100, "frequency":86}, 
                {"pattern_intensity":100, "frequency":87}, 
                {"pattern_intensity":100, "frequency":88},  
                {"pattern_intensity":100, "frequency":89},
                {"pattern_intensity":100, "frequency":90},  
                {"pattern_intensity":100, "frequency":91},  
                {"pattern_intensity":100, "frequency":92}, 
                {"pattern_intensity":100, "frequency":93}, 
                {"pattern_intensity":100, "frequency":94},  
                {"pattern_intensity":100, "frequency":95},  
                {"pattern_intensity":100, "frequency":96}, 
                {"pattern_intensity":100, "frequency":97}, 
                {"pattern_intensity":100, "frequency":98},  
                {"pattern_intensity":100, "frequency":99},
                {"pattern_intensity":100, "frequency":100},  
                ],
}
