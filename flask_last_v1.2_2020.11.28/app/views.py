# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
import time,threading
from app.jiaohu import *
from app.grade import *

# Python modules
import os, logging 
import pandas as pd
import cufflinks as cf
import plotly as py

# Flask modules
from flask               import make_response,render_template, request, url_for, redirect, send_from_directory
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort

# App modules
from app        import app, lm, db, bc
from app.models import User
from app.forms  import LoginForm, RegisterForm

#df = pd.read_csv('word_now.csv', encoding='utf-8')
regions_available = df.columns.values.tolist()[8:]
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()

# provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Logout user
@app.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Register a new user
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    
    # declare the Registration Form
    form = RegisterForm(request.form)

    msg = None

    if request.method == 'GET': 

        return render_template('layouts/auth-default.html',
                                content=render_template( 'pages/register.html', form=form, msg=msg ) )

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 
        email    = request.form.get('email'   , '', type=str) 

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = User.query.filter_by(email=email).first()

        if user or user_by_email:
            msg = '错误: 用户已存在！'
        
        else:         

            pw_hash = password #bc.generate_password_hash(password)

            user = User(username, email, pw_hash)

            user.save()

            msg = '注册成功, 请按此处 <a href="' + url_for('login') + '">登录</a>'

    else:
        msg = 'Input error'     

    return render_template('layouts/auth-default.html',
                            content=render_template( 'pages/register.html', form=form, msg=msg ) )

# Authenticate user
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    
    # Declare the login form
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        if user:
            
            #if bc.check_password_hash(user.password, password):
            if user.password == password:
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "密码错误，请重新输入"
        else:
            msg = "没有这个用户"

    return render_template('layouts/auth-default.html',
                            content=render_template( 'pages/login.html', form=form, msg=msg ) )


with open("render.html", encoding="utf8", mode="r") as f:
    plot_all = "".join(f.readlines())
# App main route + generic routing
@app.route('/', defaults={'path': 'profile.html'})
@app.route('/<path>',methods=['GET', 'POST'])
def index(path):

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    content = None

    try:
        if path == 'map.html':
            return render_template('layouts/default.html',
                            content=render_template('pages/map.html',the_plot_all=render_template('pyecharts/teb.html') ))

        elif path == 'profile.html':
            if path == 'map.html':
                return 'ok'
            else:
                return render_template('layouts/default.html',
                                       content=render_template('pages/' + path))

            # if request.form['wxdl'] == '微信登录':
            #     return render_template('layouts/default.html',
            #                     content=render_template('pages/map.html', the_plot_all=plot_all))
            # else:
            #     # try to match the pages defined in -> pages/<input file>
            #     return render_template('layouts/default.html',
            #                            content=render_template('pages/' + path))




        else:
            # try to match the pages defined in -> pages/<input file>
            return render_template('layouts/default.html',
                                   content=render_template('pages/' + path))

    except:
        
        return render_template('layouts/auth-default.html',
                                content=render_template( 'pages/404.html' ) )

# Return sitemap 
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')





@app.route('/profile/1',methods=['GET', 'POST'])
def wx():
    wxdl = request.values.to_dict()
    print(wxdl['wxdl'])
    if wxdl['wxdl'] == '微信登录':
        # threading.Thread(target=run_wxpy).start()
         #bot = Bot(qr_path=r'C:\Users\Administrator\Downloads\flask-argon-dashboard-master\app\static\assets\img\theme/QR.png')
        #
        #bot.join()
        return render_template('layouts/default.html',
                               content=render_template('pages/profile.html',wxdl=wxdl))
    return render_template('layouts/default.html',
                           content=render_template('pages/profile.html'))

@app.route('/hurun',methods=['GET', 'POST'])
def hr():
    df = pd.read_csv('hurun.csv', encoding='utf-8', delimiter="\t")
    # df = df.set_index('Index')
    regions_available = list(df.region.dropna().unique())
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    data_str = df.to_html(classes='table align-items-center table-flush')
    return render_template('layouts/default.html',
                               content=render_template('pyecharts/index.html',the_res = data_str))

@app.route('/oldall',methods=['GET', 'POST'])
def oldall():


    return render_template('layouts/default.html',
                               content=render_template('pages/story.html',
                                                       the_plot_all =render_template('pyecharts/word.html'),
                                                       sy_1=render_template('pyecharts/bat_line.html'),
                                                       sy_2=render_template('pyecharts/zg_sy.html')))

@app.route('/select_start',methods=['GET', 'POST'])
def select():


    return render_template('layouts/default.html',
                           content= render_template('pages/select.html',

                                                    the_select_region=regions_available,
                                                    ))
# @app.route('/select_end',methods=['GET', 'POST'])
# def select():
#
#
#     return render_template('layouts/default.html',
#                            content= render_template('pages/select.html',
#                                                     the_select_region=regions_available,
#                                                     the_select_region_1=regions_available_1
#                                                     ))
@app.route('/word',methods=['GET', 'POST'])
def word():
    with open("app/templates/pyecharts/第五次人口普查金字塔.html", encoding="utf8", mode="r") as f:
        word_3 = "".join(f.readlines())


    return render_template('layouts/default.html',
                           content= render_template('pages/story_1.html',
                                                    word=render_template('pyecharts/word_800.html'),
                                                    word_1 =render_template('pyecharts/word_1_800.html'),
                                                    word_2 = render_template('pyecharts/word_2_800.html'),
                                                    word_3=word_3,
                                                    word_4=render_template('pyecharts/第六次人口普查金字塔.html'),
                                                    word_5=render_template('pyecharts/近十年中国抚养比情况.html'),
                                                    word_6=render_template('pyecharts/老年人健康情况玫瑰图.html'),
                                                    word_7=render_template('pyecharts/结婚离婚堆叠图.html'),

                                                    ))

#数据故事一
@app.route('/word/1',methods=['GET', 'POST'])
def word_1():
    with open("app/templates/pyecharts/第五次人口普查金字塔.html", encoding="utf8", mode="r") as f:
        word_3 = "".join(f.readlines())


    return render_template('layouts/default.html',
                           content= render_template('pages/story_2.html',
                                                    word=render_template('pyecharts/word_800.html'),
                                                    word_1 =render_template('pyecharts/word_1_800.html'),
                                                    word_2 = render_template('pyecharts/word_2_800.html'),


                                                    ))
@app.route('/word/2',methods=['GET', 'POST'])
def word_2():
    with open("app/templates/pyecharts/第五次人口普查金字塔.html", encoding="utf8", mode="r") as f:
        word_3 = "".join(f.readlines())


    return render_template('layouts/default.html',
                           content= render_template('pages/story_3.html',
                                                    word_3=word_3,
                                                    word_4=render_template('pyecharts/第六次人口普查金字塔.html'),
                                                    word_5=render_template('pyecharts/近十年中国抚养比情况.html'),
                                                    word_6=render_template('pyecharts/老年人健康情况玫瑰图.html'),
                                                    word_7=render_template('pyecharts/结婚离婚堆叠图.html'),

                                                    ))


#数据故事二
@app.route('/fpgy',methods=['GET', 'POST'])
def fpgy():


    return render_template('layouts/default.html',
                           content= render_template('pages/story_fpgy.html',
                                                    fp_1=render_template('pyecharts/fpgy/fp_1.html'),
                                                    fp_2 =render_template('pyecharts/fpgy/fp_5.html'),
                                                    fp_3 = render_template('pyecharts/fpgy/fp_3.html'),
                                                    fp_4=render_template('pyecharts/fpgy/fp_4.html'),
                                                    fp_5=render_template('pyecharts/fpgy/fp_2.html'),
                                                    fp_6=render_template('pyecharts/fpgy/城乡就业人员的变化.html'),

                                                    ))


@app.route('/fpgy/1', methods=['GET', 'POST'])
def fpgy_1():
    return render_template('layouts/default.html',
                           content=render_template('pages/story_fpgy_0.html',
                                                   fp_1=render_template('pyecharts/fpgy/fp_1.html'),
                                                   fp_4=render_template('pyecharts/fpgy/fp_4.html'),
                                                   fp_5=render_template('pyecharts/fpgy/fp_2.html'),
                                                   ))


@app.route('/fpgy/2',methods=['GET', 'POST'])
def fpgy_2():


    return render_template('layouts/default.html',
                           content= render_template('pages/story_fpgy_1.html',
                                                    fp_1=render_template('pyecharts/fpgy/fp_3.html'),
                                                    fp_2 =render_template('pyecharts/fpgy/fp_5.html'),
                                                    fp_3 =render_template('pyecharts/fpgy/城乡就业人员的变化.html'),

                                                    ))

#交互功能
@app.route('/jiaohu/',methods=['GET'])
def jiaohu():
    jiaohu_b1 = df.T.to_html(classes='table align-items-center table-flush')
    jiaohu_b2= pd.DataFrame(df.iloc[list(df["country"]).index("{}".format('China'))]).to_html(classes='table align-items-center table-flush')
    jiaohu_selected_2 = list(df["country"])

    #
    #
    # wxdl = request.values.to_dict()
    # jiaohu_s1 = request.form["width"]
    # jiaohu_s2 = request.form["height"]
    overlap_line_scatter("China")
    timeline_map()
    renkoujinzita_0()
    with open("app/templates/pyecharts/jiaohu/jiaohu_t1.html", encoding="utf8", mode="r") as f:
        jiaohu_t1 = "".join(f.readlines())
    with open("app/templates/pyecharts/jiaohu/jiaohu_t2.html", encoding="utf8", mode="r") as f:
        jiaohu_t2 = "".join(f.readlines())
    with open("app/templates/pyecharts/jiaohu/jiaohu_t4.html", encoding="utf8", mode="r") as f:
        jiaohu_t3 = "".join(f.readlines())

    # print(wxdl,jiaohu_s1,jiaohu_s2)


    return render_template('layouts/default.html',
                           content= render_template('pages/jiaohu_1.html',
                                                     jiaohu_t1=jiaohu_t1,
                                                     jiaohu_t2 =jiaohu_t2,
                                                    jiaohu_t3=jiaohu_t3,
                                                    jiaohu_selected_2 = jiaohu_selected_2,
                                                     jiaohu_b1 =jiaohu_b1,
                                                    jiaohu_b2=jiaohu_b2,
                                                    # fp_3 =render_template('pyecharts/fpgy/城乡就业人员的变化.html'),

                                                    ))
#功能页面
@app.route('/jiaohu_1/',methods=['POST'])
def jiaohu_1():
    jiaohu_selected_2 = list(df["country"])
    jiaohu_b1 = df.T.to_html(classes='table align-items-center table-flush')
    jiaohu_b2 = pd.DataFrame(df.iloc[list(df["country"]).index("{}".format('China'))]).to_html(classes='table align-items-center table-flush')
    if 'jiaohu_selected_1' in list(request.values.to_dict().keys()):
        jiaohu_s1 = request.form["width"]
        jiaohu_s2 = request.form["height"]
        timeline_map(width=jiaohu_s1, height=jiaohu_s2)
        with open("app/templates/pyecharts/jiaohu/jiaohu_t1.html", encoding="utf8", mode="r") as f:
            jiaohu_t1 = "".join(f.readlines())
        with open("app/templates/pyecharts/jiaohu/jiaohu_t2.html", encoding="utf8", mode="r") as f:
            jiaohu_t2 = "".join(f.readlines())
        with open("app/templates/pyecharts/jiaohu/jiaohu_t3.html", encoding="utf8", mode="r") as f:
            jiaohu_t3 = "".join(f.readlines())

        return render_template('layouts/default.html',
                               content=render_template('pages/jiaohu_1.html',
                                                       jiaohu_t1=jiaohu_t1,
                                                       jiaohu_b1=jiaohu_b1,
                                                       jiaohu_b2=jiaohu_b2,
                                                       jiaohu_t2=jiaohu_t2,
                                                       jiaohu_t3=jiaohu_t3,
                                                       jiaohu_selected_2=jiaohu_selected_2,
                                                       ))
    elif list(request.values.to_dict().keys())[0] == 'jiaohu_selected_2':

        Country = request.form['jiaohu_selected_2']
        jiaohu_b2 = pd.DataFrame(df.iloc[list(df["country"]).index("{}".format(Country))]).to_html(
            classes='table align-items-center table-flush')
        overlap_line_scatter(Country)
        with open("app/templates/pyecharts/jiaohu/jiaohu_t1.html", encoding="utf8", mode="r") as f:
            jiaohu_t1 = "".join(f.readlines())
        with open("app/templates/pyecharts/jiaohu/jiaohu_t2.html", encoding="utf8", mode="r") as f:
            jiaohu_t2 = "".join(f.readlines())
        with open("app/templates/pyecharts/jiaohu/jiaohu_t3.html", encoding="utf8", mode="r") as f:
            jiaohu_t3 = "".join(f.readlines())
        return render_template('layouts/default.html',
                               content=render_template('pages/jiaohu_1.html',
                                                       jiaohu_t1=jiaohu_t1,
                                                       jiaohu_b1=jiaohu_b1,
                                                       jiaohu_t2=jiaohu_t2,
                                                       jiaohu_b2=jiaohu_b2,
                                                       jiaohu_t3=jiaohu_t3,
                                                       jiaohu_selected_2=jiaohu_selected_2,

                                                       ))
    elif list(request.values.to_dict().keys())[0] == 'jiaohu_selected_3':
        jiaohu_b2 = pd.DataFrame(df.iloc[list(df["country"]).index("{}".format("China"))]).to_html(
            classes='table align-items-center table-flush')
        overlap_line_scatter('China')
        with open("app/templates/pyecharts/jiaohu/jiaohu_t1.html", encoding="utf8", mode="r") as f:
            jiaohu_t1 = "".join(f.readlines())
        with open("app/templates/pyecharts/jiaohu/jiaohu_t2.html", encoding="utf8", mode="r") as f:
            jiaohu_t2 = "".join(f.readlines())
        with open("app/templates/pyecharts/jiaohu/jiaohu_t3.html", encoding="utf8", mode="r") as f:
            jiaohu_t3 = "".join(f.readlines())
        return render_template('layouts/default.html',
                               content=render_template('pages/jiaohu_1.html',
                                                       jiaohu_t1=jiaohu_t1,
                                                       jiaohu_b1=jiaohu_b1,
                                                       jiaohu_t2=jiaohu_t2,
                                                       jiaohu_b2=jiaohu_b2,
                                                       jiaohu_t3=jiaohu_t3,
                                                       jiaohu_selected_2=jiaohu_selected_2,

                                                       ))


#成绩查询
@app.route('/grade_data/',methods=['POST'])
def grade_data():
    账号 = request.form["zhanghao"]
    密码 = request.form["mima"]
    
    
    msg = None
    try:
        data = get_geade_data(账号,密码)
        data = data.loc[:,["name","kcxf","l3mc"]]
        data_add = data
        data_add["l2kcxz"] = [i[:-1] for i in data_add.l3mc.to_list()]
        data_add["l2kcxz"].replace("思政必修", "公共必修",inplace = True)
        data_add["l2kcxz"].replace("通识必修", "公共必修",inplace = True)
        data_add["l2kcxz"].replace("专业方向", "专业必修",inplace = True)
        data_add["l2kcxz"].replace("专业核心", "专业必修",inplace = True)
        data_add["l2kcxz"].replace("大学体育", "公共必修",inplace = True)
        data_add["l2kcxz"].replace("大学英语", "公共必修",inplace = True)
            
        大类 = data_add.groupby('l2kcxz').sum().to_dict()['kcxf']
        小类 = data_add.drop_duplicates('name').groupby('l3mc').sum().to_dict()['kcxf']

        # 已修
        
        已修_公共必修 = int(大类['公共必修'])
        已修_公共选修 = int(大类['公共选修'])
        已修_专业核心 = int(小类['专业核心课'])
        已修_专业方向 = int(小类['专业方向课'])
        已修_实习_论文 = 0
        已修_专业选修 = int(小类['专业选修课'])
        已修_成长必修课 = int(大类['成长必修'])
        已修_总学分 = 已修_公共必修+已修_公共选修+已修_专业核心+已修_专业方向+已修_实习_论文+已修_专业选修+已修_成长必修课 


        # 待修
        待修_总学分 = (150-已修_总学分)
        待修_公共必修 = (40-已修_公共必修)
        待修_公共选修 = (5-已修_公共选修)
        待修_专业核心 = (30-已修_专业核心)
        待修_专业方向 = (20-已修_专业方向)
        待修_实习_论文 = 7
        待修_专业选修 = (40-已修_专业选修)
        待修_成长必修课 = (8-已修_成长必修课)

        data_add.columns = ["课程名称","课程学分","课程性质（小类）","课程性质（大类）"]

        return render_template('layouts/default.html',
                               content= render_template('pages/grade.html',
                                                         data_all = data_add.to_html(classes = "table table-bordered"),
                                                         yx_1 = 已修_总学分,
                                                         yx_2 = 已修_公共必修,
                                                         yx_3 = 已修_公共选修,
                                                         yx_4 = 已修_专业核心,
                                                         yx_5 = 已修_专业方向,
                                                         yx_6 = 已修_实习_论文,
                                                         yx_7 = 已修_专业选修,
                                                         yx_8 = 已修_成长必修课,

                                                         dx_1 = 待修_总学分,
                                                         dx_2 = 待修_公共必修,
                                                         dx_3 = 待修_公共选修,
                                                         dx_4 = 待修_专业核心,
                                                         dx_5 = 待修_专业方向,
                                                         dx_6 = 待修_实习_论文,
                                                         dx_7 = 待修_专业选修,
                                                         dx_8 = 待修_成长必修课,                                                 
                                                        ))

    except:
        msg = '学号或密码错误!'
        return render_template('layouts/default.html',
                           content= render_template('pages/jiaohu_2.html',msg = msg))





    # wxdl = request.values.to_dict()
    #
    #
    # print(wxdl,request.values.to_dict().keys())







# @app.route('/profile/2',methods=['GET', 'POST'])
# def nb():
#     import pandas as pd
#     import matplotlib as mpl
#     import matplotlib.pyplot as plt
#     import matplotlib.ticker as ticker
#     import matplotlib.animation as animation
#     from IPython.display import HTML
#     fig, ax = plt.subplots(figsize=(15, 8))
#
#     def draw_barchart(year):
#         dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
#         ax.clear()
#         ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
#         dx = dff['value'].max() / 200
#         for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
#             ax.text(value - dx, i, name, size=14, weight=600, ha='right', va='bottom')
#             ax.text(value - dx, i - .25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
#             ax.text(value + dx, i, f'{value:,.0f}', size=14, ha='left', va='center')
#         # ... polished styles
#         ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
#         ax.text(0, 1.06, 'Population (thousands)', transform=ax.transAxes, size=12, color='#777777')
#         ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
#         ax.xaxis.set_ticks_position('top')
#         ax.tick_params(axis='x', colors='#777777', labelsize=12)
#         ax.set_yticks([])
#         ax.margins(0, 0.01)
#         ax.grid(which='major', axis='x', linestyle='-')
#         ax.set_axisbelow(True)
#         ax.text(0, 1.12, 'The most populous cities in the world from 1500 to 2018',
#                 transform=ax.transAxes, size=24, weight=600, ha='left')
#         #     ax.text(1, 0, 'by QIML', transform=ax.transAxes, ha='right',
#         #             color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
#         plt.box(False)
#
#     df = pd.read_csv('Metadata_Indicator_API_SP.DYN.LE00.IN_DS2_zh_csv_v2_628227.csv',
#                      usecols=['name', 'group', 'year', 'value'])
#     mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
#     mpl.rcParams['axes.unicode_minus'] = False
#     current_year = 2017
#     dff = (df[df['year'].eq(current_year)]
#            .sort_values(by='value', ascending=True)
#            .head(10))
#     colors = dict(zip(
#         ['中高等收入国家', '高收入国家', '关岛', '捷克共和国',
#          '美属维京群岛', '巴巴多斯', '北美'],
#         ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
#          '#aafbff', '#f7bb5f', '#eafb50']
#     ))
#     group_lk = df.set_index('name')['group'].to_dict()
#     import matplotlib.animation as animation
#     from IPython.display import HTML
#     fig, ax = plt.subplots(figsize=(15, 8))
#     animator = animation.FuncAnimation(fig, draw_barchart, frames=range(196, 2019))
#     h5 = animator.to_jshtml()
#     return render_template(h5)