<div align="center">
  <h1>python flask架站自我策展</h1>
  <p>python_falsk_web</p>
</div>


> 18级《Python》的每一位同学要展示总结其Python能力，以笔记及电子讲义的列表目录及说明页为入口，放在Github或Github架的Jekyll网站为主，并提交自我策展说明页 url。

|发布日期|2019年12月28日|
| ---------- | --- |
|产品名称|python_falsk_web|
|项目现状|已经基本完成|
|文件的主人|黄杰琪|
|领头的设计师|郑晓萍|
|领头的开发者|黄杰琪|
|版本号|v0.1|
|更新内容|增加评分标准与项目架构|

```
├── README.md                //项目文档
├── app
│	├──	__init__
│	├── views                     // 路由配置
│   ├── static
│   │	└── assets              // 网站样式
│  	│		 ├── css         	// 样式
│   │		 ├── fonts		    // 字体
│   │		 ├── img            // 图片
│   │		 └── js             // 脚本
│   └── templates         // html模板
│   	├── includes         // 
│   	├── layouts
│   	├── pages                // 配置控制
│   	└── pyecharts            // pyecharts图表
├── requirements                        // 第三方库文档
└── run
```


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
- :black_square_button:19.12.18-**19.1.05 提交最终 url** 19days is enough but we should in advance to spend time in holiday
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


## :warning:协作作品的要求（python部分）：

####[暂定]18级《python》评分点：
- 是否实现交互功能 (HTML表, 若17级不给力的话，至少做到表的交互没图的话)
- 是否实现在pythonanywhere布署可用
- 基本Readme.md技术文档之总结说明, 含項目之代码Github URL
- pythonanywhere URL/云服务器的域名提交 URL 数据传递描述 
- 基本交互功能的HTML5控件使用丰富性(加分项）
####（10%）github文档格式（包含基本的templates、static、app.py/main.py、数据文档（下载）/API数据）


####（20%）技术文档书写
- HTML档描述（30%）


- Python档描述（30%）


- Web App动作描述（40%）


####（40%）数据交互（数据复杂度（是否存在与合理））
- 是否含有复杂数据结构的循环（列表循环、字典循环、集合循环）（20%）



- 是否含有合适的数据结构嵌套（20%）



- 是否含有合适的推导式（20%）


- 是否含有适当的条件判断（20%）


- python 文档与html文档的数据交互（20%）


####（10%）自定义函数与模块功能（是否存在与合理)
- 函数和模块符合python PEP8标准（50%）



- 功能具有可扩展和丰富性（50%）


####（10%）HTML界面
- 实现数据的python——>HTML页面交互（如果Python有数据循环、复杂的数据结构，请务必检查前端是否正确接收到同样的数据传递结果）（80%）


- 符合jinja2标准（20%）


####（10%）上传pythonanywhere/提交域名完善的个人网站




链接：

- [markdown排版](https://github.com/wenjunmo/DataStory_Interactive-Visualization) 借鉴[Geek Jun](https://github.com/wenjunmo/)
- [markdown EMOJI](https://www.webfx.com/tools/emoji-cheat-sheet/) 
- [flask-bootstrap](https://flask-bootstrap-zh.readthedocs.io/zh/latest/)

- [flask-sqlalchemy](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)
- [python个人学习记录](https://github.com/huangjieqi/python_note)
- [pythonanywhere背景变色项目](http://huangjieqi.pythonanywhere.com/)
- [个人前端jekyll架站展示](https://huangjieqi.gitee.io/)
- [flask 学习视频](https://www.youtube.com/watch?v=RWviEK1Si68&list=PLDFBYdF-BxV1G4FBpG1EMyFtbsbZuJOvD)


