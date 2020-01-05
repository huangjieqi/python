# 作者：黄杰琪
from app import app
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
app1 = dash.Dash(__name__, server=app, url_base_pathname='/dash/')
app1.layout = html.Div(
    children = [
        html.H1('你好，Dash'),
        html.Div('''Dash: Python网络应用框架'''),
        dcc.Graph(
            id='example-graph',
            figure = dict(
                data = [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': '北京'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': '上海'}],
                layout = dict(title = 'Dash数据可视化')
            )
        )
    ]
)

