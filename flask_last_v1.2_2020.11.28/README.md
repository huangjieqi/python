# [Flask Dashboard Argon](https://appseed.us/admin-dashboards/flask-dashboard-argon)

**[Open-Source Admin Dashboard](https://appseed.us/admin-dashboards/flask-dashboard-argon)** coded in **Flask Framework** on top of **Argon Dashboard** design. **Features**:

<br />

- SQLite database
- SQLAlchemy ORM
- Session-Based authentication flow (login, register)
- UI Kit: [Argon Dashboard](https://github.com/app-generator/fork-argon-dashboard-html) by **Creative-Tim**

<br />

![Flask Dashboard Argon - Open-Source Flask Dashboard.](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-argon-intro.gif)

<br />

```
├── Readme.md                   // help
├── app                         // 应用
├── config                      // 配置
│   ├── default.json
│   ├── dev.json                // 开发环境
│   ├── experiment.json         // 实验
│   ├── index.js                // 配置控制
│   ├── local.json              // 本地
│   ├── production.json         // 生产环境
│   └── test.json               // 测试环境
├── data
├── doc                         // 文档
├── environment
├── gulpfile.js
├── locales
├── logger-service.js           // 启动日志配置
├── node_modules
├── package.json
├── app-service.js              // 启动应用配置
├── static                      // web静态资源加载
│   └── initjson
│       └── config.js         // 提供给前端的配置
├── test
├── test-service.js
└── tools
```


```ash
$ # Clone the sources
$ git clone https://github.com/app-generator/flask-argon-dashboard.git
$ cd flask-argon-dashboard
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv --no-site-packages env
$ # .\env\Scripts\activate
$ 
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the application
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the app in browser: http://127.0.0.1:5000/
```

<br />

## Want more? Go PRO!

<br />

| [Flask Dashboard Material](https://appseed.us/admin-dashboards/flask-dashboard-material-pro) | [Flask Dashboard Argon](https://appseed.us/admin-dashboards/flask-dashboard-argon-pro) | [Flask Dashboard Black](https://appseed.us/admin-dashboards/flask-dashboard-black-pro) |
| --- | --- | --- |
| [![Flask Dashboard Material PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-material-pro-intro.gif)](https://appseed.us/admin-dashboards/flask-dashboard-material-pro)  | [![Flask Dashboard Argon PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-argon-pro-intro.gif)](https://appseed.us/admin-dashboards/flask-dashboard-argon-pro) | [![Flask Dashboard Black PRO](https://raw.githubusercontent.com/app-generator/static/master/products/flask-dashboard-black-pro-intro.gif)](https://appseed.us/admin-dashboards/flask-dashboard-black-pro)

<br />

## Support

- Free support via eMail < [support @ appseed.us](https://appseed.us/support) > and **Github** issues tracker
- 24/7 Live Support via [Discord](https://discord.gg/fZC6hup) for paid plans and commercial products.

<br />

## Credits & Links

- [Flask Dashboard Argon](https://appseed.us/admin-dashboards/flask-dashboard-argon) - Product page
- [Flask Dashboard Argon](https://flask-argon-dashboard.appseed.us/) - Live DEMO
- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The offcial website
- [Flask Dashboard - Open-Source Boilerplates](https://dev.to/sm0ke/flask-dashboard-open-source-boilerplates-dkg) - A popular article published on Dev.to platform
- [Flask Dashboard](https://admin-dashboards.com/tags/flask-dashboard) - Index provided by **Admin-Dashboards.com**

<br />

## License

@MIT

<br />

---
[Flask Dashboard Argon](https://appseed.us/admin-dashboards/flask-dashboard-argon) provided by **AppSeed**
