<div align="center">
  <h1><a href="http://zxpzxp.cn/">python flask架站自我策展</a></h1>

  <p>python_falsk_web</p>
</div>

# 项目地址[zxpzxp.cn](http://zxpzxp.cn/)
> 18级《Python》的每一位同学要展示总结其Python能力，以笔记及电子讲义的列表目录及说明页为入口，放在Github或Github架的Jekyll网站为主，并提交自我策展说明页 url。

|发布日期|2020年1月5日|
| ---------- | --- |
|产品名称|python_falsk_web|
|项目现状|项目完成|
|文件的主人|黄杰琪|
|领头的设计师|郑晓萍|
|领头的开发者|黄杰琪|
|版本号|v1.1|
|更新内容|代码上传与技术文档撰写|





## :warning:协作作品的要求（python部分）：

- 是否实现交互功能 (HTML表, 若17级不给力的话，至少做到表的交互没图的话)
- 是否实现在pythonanywhere布署可用
- 基本Readme.md技术文档之总结说明, 含項目之代码Github URL
- pythonanywhere URL/云服务器的域名提交 URL 数据传递描述 
- 基本交互功能的HTML5控件使用丰富性(加分项）
#### github文档格式（包含基本的templates、static、app.py/main.py、数据文档（下载）/API数据）

- 项目主要架构
```
├── README.md                //项目文档
├── data                     //图表数据
├── app
│   ├──__init__
│   ├── views                     // 路由配置
│   ├── static
│   │	└── assets              // 网站样式
│   │	│		
│   │	├── css         	// 样式
│   │   ├── fonts		    // 字体
│   │	├── img            // 图片
│   │   └── js             // 脚本
│   └── templates         // html模板
│   	├── includes         // html组件
│   	├── layouts
│   	├── pages                // 配置控制
│   	└── pyecharts            // pyecharts图表
├── requirements                        // 第三方库文档
└── run
```



### 技术文档书写
#### HTML档描述
>基于[Argon - Design System](https://demos.creative-tim.com/argon-dashboard/docs/getting-started/overview.html)框架进行开发：
   - [Bootstrap 4](https://getbootstrap.com/)-开源前端框架
   - [jQuery-快速](https://jquery.com/https://jquery.com/)，小型和功能丰富的JavaScript库
   - [Open Sans字体](https://fonts.google.com/specimen/Open+Sans) -Google的开源字体
   - [条纹元素 -表单](https://github.com/stripe/elements-examples/#example-1)，按钮和元素

#### Python档描述/自定义函数与模块功能
##### python项目结构
  >样板代码采用模块化结构构建,下面列出了最重要的文件/目录：
  ```
  < ROOT > - Flask Dashboard Argon  # application root folder
    |
    |--- app/                     # application folder  
    |--- app/__init__.py          # application constructor  
    |--- app/configuration.py     # application config  
    |--- app/forms.py             # application forms  
    |--- app/models.py            # application models  
    |--- app/views.py             # application routing
    |  
    |--- requirements.txt         # Requirements for development - SQLite storage
    |--- run.py                   # bootstrap the app
    |
    |-----------------------------
  ```
  - 含有以下主要功能：
	- SQLite数据库
	- SQLAlchemy ORM
	- 基于会话的身份验证流程（登录，注册）
	- 可视化图表生成
	- 可视化图表数据查询
	- 可视化图表尺寸定义

  



####  Web App动作描述、数据交互（数据复杂度（是否存在与合理））

- 基于会话的身份验证流程（登录，注册）
 - login.html页面可进行登录
 - register.html页面进行注册，注册后会弹出提示，点击链接跳转到登陆页面
 


- 功能页面（/jiaohu）表单运用列表循环进行选择是否含有复杂数据结构的循环（列表循环、字典循环、集合循环）



- 功能页面前两个功能均由Datafarm数据框通过pands操作转换成字典、或列表进行函数构造（是否含有合适的数据结构嵌套）


- jiaohu.py中的第三个函数运用推导式将列表中的正值转换为负值以便做出人口金字塔图表(是否含有合适的推导式)


- 利用if判断实现登录的验证判断、功能页面三个功能的from提交数据接受判断与返回判断(是否含有适当的条件判断)
- 通过`list(request.values.to_dict().keys())[0]`、`jiaohu_s1 = request.form["width"]`、`list(request.values.to_dict().keys())[0]`
去进行数据交互与数据判断，通过`with open`的方式将文件直接转换成html数据，通过jinja2的过滤器进行渲染，解决数据交互带来的缓存问题（python文档与html文档的数据交互）
```python
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

```


#### 上传pythonanywhere/提交域名完善的个人网站

##### [zxpzxp.cn](http://zxpzxp.cn/)


## :hammer: python基础阶段展示

- [python环境、数据类型、运算符](https://github.com/huangjieqi/python_note/blob/master/task1.md)
- [列表、元组、字符串](https://github.com/huangjieqi/python_note/blob/master/text2.md)
- [字典、集合、判断、循环](https://github.com/huangjieqi/python_note/blob/master/task3.md)
- [函数、文件操作](https://github.com/huangjieqi/python_note/blob/master/task4.md)
- [类与对象](https://github.com/huangjieqi/python_note/blob/master/task5.md)

## :wrench: python flask项目架站技术总结分析
- [pythonanywhere背景变色项目](http://huangjieqi.pythonanywhere.com/)
  - pythonanywhere进行后端服务器部署，具有已安装好的多个flask扩展库，免费服务器
  - html前端部分[个人前端jekyll架站展示](https://huangjieqi.gitee.io/)

- 利用[flask-bootstrap](https://flask-bootstrap-zh.readthedocs.io/zh/latest/)进行页面布局与排版，时间导航页面进行数据前后端交互时的跳转

- [flask-sqlalchemy](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)可以进行数据库连接与数据库Model搭建，进行日志查询与数据存储




## :calendar: 产品进度

- :ballot_box_with_check: 19.12.13-**19.12.15 数据产品或者是数据可视化项目的点子放在Github上面**，将url填在腾讯文档上面，在12.15周日晚23点之前提交
- :ballot_box_with_check: 19.12.15-**19.12.18 组建团队**
    - < 15Days Pitch DataStory Product in PRD-MD to GitHub 
    - < 15Days Show python ability in Jekyll to GitHub
- :ballot_box_with_check:19.12.18-**19.1.05 提交最终 url** 19days is enough but we should in advance to spend time in holiday
    - 12.18-12.22 实现见评分要求
    - 12.23-**12.29 结束最终 url 放假** 最终提交各自负责的入口url进行项目及文档提交
- :black_square_button:19.1.06-**19.1.07 互评阶段**，要求见评分要求

> 共同作品要求：
1. 自己提供数据，但数据量>250个
2. Html5界面设计包含CSS样式
3. 必须部署在 pythonanywhere 并可用

- :black_square_button:19.1.08-19.1.10 互评公示及异议，要求见评分要求

## :warning: 评分要求

18级评分点：
- 实现 **交互功能** (Html表，至少做到表的交互没图假设下)
- 实现 **部署在 pythonanywhere 可用
- 基本README.md技术文档总结项目说明
  - 代码 **GitHub URL**
  - **pythonanywhere url**
  - **数据传输描述**
- 基本交互功能 **Html控件使用丰富**(加分项)

17级评分点：
- **数据清洗和收集难度，数据集丰富程度**
- **交互功能**对于强化数据产品或者数据故事**表现力的程度**
- 交互界面 **美观得体**(使用Pyecharts、Plotly、CSS包含在内)
- 整体数据产品/数据故事是否**有洞见**，给用户交互产生洞见的引导及可能性

简述之：
- 共同要求：hurun数据/自己提供数据-国家统计局+H5页面设计包含CSS样式+pythonanywhere.com，是否有说服力和数据洞见-数据库,Flask
- 18级评分：交互功能能否实现最基本的数据传递+是否上传到Pythonanywhere(最终提交github和pythonanywhere网址)+交互功能的丰富性(加分项)
- 17级评分：交互功能对于强化数据产品或者数据故事的程度+交互界面是否好看plotly、pyecharts、网页CSS等渠道实现都可+数据产品/数据故事是否有洞见+数据清洗和收集难度，数据集丰富程度

## :computer: 开发人员:

- 前后端(基本：仅表)交互的代码实践及文档写作
- Html文档结构及交互控件实现及交互变数实践

### :bar_chart: 产品经理/交互设计师：

- 最小可行性的交互式数据可视化产品设计
- 完成PRD及至少2份成功交互且交互意义相关联（以超链接活交互达成）的交互式界面(至少1份含地图)的产品原型或完整产品，包括使用Pyecharts/Plotly模块等整合外观样式及数据科学代码实践，外观样式前端CSS及JS库的调用实践(Bootstrap)






链接：
- [Argon Dashboard UI](https://www.creative-tim.com/product/argon-dashboard) - crafted by Creative-Tim agency
- [Flask Gentelella](https://github.com/afourmy/flask-gentelella) - author **Antoine Fourmy**
- [Flask Boilerplate Dashboard Argon](https://appseed.us/admin-dashboards/flask-boilerplate-dashboard-argon) - Product page
- [Flask Boilerplate Dashboard Argon](https://www.youtube.com/watch?v=bnCuQzDE3Ks/) - Video presentation (Youtube)
- [Flask Framework](https://www.palletsprojects.com/p/flask/) - Offcial website
- [Flask Dashboard - Open-Source Boilerplates](https://dev.to/sm0ke/flask-dashboard-open-source-boilerplates-dkg) - A popular article published on Dev.to platform
- [Flask Dashboard](https://admin-dashboards.com/tags/flask-dashboard) - Index provided by **Admin-Dashboards.com**
- [markdown排版](https://github.com/wenjunmo/DataStory_Interactive-Visualization) 借鉴[Geek Jun](https://github.com/wenjunmo/)
- [markdown EMOJI](https://www.webfx.com/tools/emoji-cheat-sheet/) 
- [flask-bootstrap](https://flask-bootstrap-zh.readthedocs.io/zh/latest/)
- [flask-sqlalchemy](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)
- [python个人学习记录](https://github.com/huangjieqi/python_note)
- [pythonanywhere背景变色项目](http://huangjieqi.pythonanywhere.com/)
- [个人前端jekyll架站展示](https://huangjieqi.gitee.io/)
- [flask 学习视频](https://www.youtube.com/watch?v=RWviEK1Si68&list=PLDFBYdF-BxV1G4FBpG1EMyFtbsbZuJOvD)


