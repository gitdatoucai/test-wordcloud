import streamlit as st
import numpy as np
import pandas as np
from pyecharts.charts import WordCloud 
from streamlit_echarts import st_pyecharts

# 输入,暂时瞎编
words = [
        ("花鸟市场", 1446),
        ("汽车", 928),
        ("视频", 906),
        ("电视", 825),
        ("Lover Boy 88", 514),
        ("动漫", 486),
        ("音乐", 53),
        ("直播", 163),
        ("广播电台", 86),
        ("戏曲曲艺", 17),
        ("演出票务", 6),
        ("给陌生的你听", 1),
        ("资讯", 1437),
        ("商业财经", 422),
        ("娱乐八卦", 353),
        ("军事", 331),
        ("科技资讯", 313),
        ("社会时政", 307),
        ("时尚", 43),
        ("网络奇闻", 15),
        ("旅游出行", 438),
        ("景点类型", 957),
        ("国内游", 927),
        ("远途出行方式", 908),
        ("酒店", 693),
        ("关注景点", 611),
        ("旅游网站偏好", 512),
        ("出国游", 382),
        ("交通票务", 312),
        ("旅游方式", 187),
        ("旅游主题", 163),
        ("港澳台", 104),
        ("本地周边游", 3),
        ("香水", 50),
        ("个人护理", 46),
        ("美甲", 26),
        ("SPA美体", 21),
        ("花鸟萌宠", 914),
    ]

st.title('词云生成器')
uploaded_file = st.file_uploader("请上传文本文件")   # 传入文档
if uploaded_file is not None:
    string_data = uploaded_file.read().decode('utf-8')

col1, col2 = st.columns([5, 1])
with col2:
    shape_option = st.selectbox(
        "请选择词云图形",
        ( 'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star')) 


# 生成词云
with col1:
    c = (
        WordCloud()
        .add("", 
            words, 
            shape=shape_option,
            # mask_image=None,
            # word_gap=20, #词间间隔
            width = 800,
            height = 800,
            word_size_range=[5, 30]
            )
    )
    st_pyecharts(c)