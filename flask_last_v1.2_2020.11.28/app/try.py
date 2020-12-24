# from wxpy import *
# import os
# def qrCallback(uuid,status,qrcode):
#     print('正在保存二维码')
#     if status == '0':
#         global qrSource
#         qrSource = qrcode
#     elif status == '200':
#         qrSource = 'Logged in!'
#     elif status == '201':
#         qrSource = 'Confirm'
# # print(os.getcwd())
# bot = Bot(qr_path=r'C:\Users\Administrator\Downloads\flask-argon-dashboard-master\app\static\assets\img\theme/QR.png')
from flask import Flask,render_template




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():

    return render_template('pages/try.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
# print(JupyterDash.__html__(app1))
# print(JupyterDash.__html__(app1).split('"'))



