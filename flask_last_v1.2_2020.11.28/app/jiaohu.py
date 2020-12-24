from app import app
import plotly as py
import plotly.graph_objs as go
from pyecharts.charts import Bar,Line,Map,Timeline,Grid,Scatter#引入图表制作所需要的一些函数
from pyecharts import options as opts #利用as将函数options制定为opts，方便下面的调用，此函数用于图表的各种配置
import pandas as pd #引入pandas
import numpy as np
from pyecharts.globals import ThemeType
#导入所有数据
df = pd.read_csv("data/word_old.csv",encoding = 'utf-8')
df1 =  pd.read_csv("data/word_now.csv",encoding = 'utf-8')
df2 = pd.read_csv("data/第五次人口普查男女比重 .csv")
df3 = pd.read_csv("data/第六次人口普查男女比重.csv")


def timeline_map(width='800px', height='500px') -> Timeline:
    year = df.columns.values.tolist()[7:]
    tl = Timeline(opts.InitOpts(width=width, height=height, theme=ThemeType.INFOGRAPHIC))
    for i in year:
        map0 = (
            Map()
                .add(
                "生育率", list(zip(list(df.country), list(df["{}".format(i)]))), "world", is_map_symbol_show=False
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年世界生育率".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                # 设置副标题样式，进行图例说明
                visualmap_opts=opts.VisualMapOpts(max_=8),

            )
        )
        tl.add(map0, "{}年".format(i))
    return tl.render('app/templates/pyecharts/jiaohu/jiaohu_t1.html')


def overlap_line_scatter(Country) -> Bar:
    Country_index = list(df["country"]).index("{}".format(Country))
    df_c = df.iloc[Country_index].to_dict()
    df_k = list(df_c.keys())[7:]
    df_v = list(df_c.values())[7:]
    bar = (
        Bar(opts.InitOpts(width='800px', height='550px'))  # opts.InitOpts(width = '810px',height = '500px')
            .add_xaxis(df_k)
            .add_yaxis("{}生育率/%".format(Country), df_v)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # .add_yaxis)("商家B", Faker.values()
            .set_global_opts(title_opts=opts.TitleOpts(subtitle="{}生育率历年趋势".format(Country),
                                                       subtitle_textstyle_opts=opts.TextStyleOpts(color="red",
                                                                                                  font_size=14,
                                                                                                  font_style="italic")),
                             legend_opts=opts.LegendOpts(pos_right="15%")
                             )

    )
    line = (
        Line()
            .add_xaxis(df_k)
            .add_yaxis("{}生育率/%".format(Country), df_v)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    )
    bar.overlap(line)
    return bar.render('app/templates/pyecharts/jiaohu/jiaohu_t2.html')


def renkoujinzita():
    women_bins = df2.女
    men_bins = [float('-' + str(df2.男[i])) for i in range(len(df2.男))]

    y = df2['年龄']

    layout = go.Layout(yaxis=go.layout.YAxis(title='年龄'),
                       xaxis=go.layout.XAxis(
                           range=[-6, 6],
                           tickvals=[-6, -3, -1, 0, 1, 3, 6],
                           ticktext=[6, 3, 1, 0, 1, 3, 6],
                           title='第五次人口普查金字塔'),
                       barmode='overlay',
                       bargap=0.1)

    data = [go.Bar(y=y,
                   x=men_bins,
                   orientation='h',#水平条形图需设置，竖直条形图不用设置
                   name='男性',
                   hoverinfo='x',
                   marker=dict(color='#5793f3')#设置颜色
                   ),
            go.Bar(y=y,
                   x=women_bins,
                   orientation='h',#水平条形图需设置，竖直条形图不用设置
                   name='女性',
                   text=-1 * women_bins.astype('float'),#women的数据标签
                   hoverinfo='text',
                   marker=dict(color='#d14a61')
                   )]

    fig = dict(data=data, layout=layout)
    return py.offline.plot(fig,filename='app/templates/pyecharts/jiaohu/jiaohu_t3.html',auto_open=False)


def renkoujinzita_0():
    women_bins = df3.女
    men_bins = [float('-' + str(df3.男[i])) for i in range(len(df3.男))]

    y = df3['年龄']

    layout = go.Layout(yaxis=go.layout.YAxis(title='年龄'),
                       xaxis=go.layout.XAxis(
                           range=[-6, 6],
                           tickvals=[-6, -3, -1, 0, 1, 3, 6],
                           ticktext=[6, 3, 1, 0, 1, 3, 6],
                           title='第六次人口普查金字塔'),
                       barmode='overlay',
                       bargap=0.1)

    data = [go.Bar(y=y,
                   x=men_bins,
                   orientation='h',#水平条形图需设置，竖直条形图不用设置
                   name='男性',
                   hoverinfo='x',
                   marker=dict(color='#5793f3')#设置颜色
                   ),
            go.Bar(y=y,
                   x=women_bins,
                   orientation='h',#水平条形图需设置，竖直条形图不用设置
                   name='女性',
                   text=-1 * women_bins.astype('float'),#women的数据标签
                   hoverinfo='text',
                   marker=dict(color='#d14a61')
                   )]

    fig = dict(data=data, layout=layout)
    return py.offline.plot(fig,filename='app/templates/pyecharts/jiaohu/jiaohu_t4.html',auto_open=False)





