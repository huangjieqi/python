# # 作者：黄杰琪
# from app import app
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# app1 = dash.Dash(__name__, server=app, url_base_pathname='/dash/')
# app1.layout = html.Div(
#     children = [
#         html.H1('你好，Dash'),
#         html.Div('''Dash: Python网络应用框架'''),
#         dcc.Graph(
#             id='example-graph',
#             figure = dict(
#                 data = [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': '北京'},
#                         {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': '上海'}],
#                 layout = dict(title = 'Dash数据可视化')
#             )
#         )
#     ]
# )




import requests
from datetime import date, datetime

from json import decoder, loads
from json.decoder import JSONDecodeError
from os import getenv
from traceback import format_exc
import pandas as pd
from requests import post

"""
新代码 教务系统查询函数

"""
def get_jw_token(student_id: int, password: str = '', count: int = 0) -> str:
    """
    登陆教务系统
    :param count:
    :param student_id: 学号
    :param password: 密码，默认为空字符串
    :return token:
    """

    url = 'http://ecampus.nfu.edu.cn:2929/jw-privilegei/User/r-login'
    data = {
        'username': student_id,
        'password': password,
        'rd': ''
    }

    try:
        response = post(url, data=data, timeout=10)
        token = loads(response.text)['msg']
    except (OSError, decoder.JSONDecodeError):
        if count >= 5:
            raise NFUError('教务系统登录接口错误，请稍后再试')
        else:
            return get_jw_token(student_id, password, count + 1)

    if not token:
        raise NFUError('学号或密码错误!')

    return token



def get_class_schedule_try(token: str,  count: int = 0) -> list:
    """
    向教务系统请求课程表数据

    :param count:
    :param token:
    :param school_year:
    :param semester:
    school_year: int, semester: int,
    :return:
    """
    course_data = []
    url = 'http://ecampus.nfu.edu.cn:2929/jw-cssi/CssStudent/r-listJxb'
    data = {
#         'xn': school_year,
#         'xq': semester,
        'jwloginToken': token
    }

    response = post(url, data=data, timeout=10)
    course_list = loads(response.text)['msg']
    return course_list


def get_geade_data(student_id: int, password: str = ''):
	"""整合上面两个函数
	"""
	return pd.json_normalize(get_class_schedule_try(token=get_jw_token(student_id=student_id, password=password)))