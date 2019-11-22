from flask import Flask
from flask import render_template
from flask import request
import mysql.connector as mc

app = Flask(__name__)


@app.route("/showProducts")
def show_products():

    conn = get_connection()
    result = conn.cmd_query("select * from product")
    rows = conn.get_rows()
    conn.close()
    return str(rows[0])


# @app.route("/submitstuff",methods=['post'])
# def get_submission():
#     #ms = request.args.get('mystuff')
#     #myssn = request.args.get('myssn')
#     ms = request.form['mystuff']
#     myssn = request.form['myssn']
#     print('my stuff is',ms)
#     print('my ssn is',myssn)
#     return "you sent in <b>" + ms + "</b>"


@app.route("/")
def hello_world():

    conn = get_connection()
    result = conn.cmd_query("select * from product")
    rows = conn.get_rows()
    conn.close()

    product = rows[0]
    return render_template('main.html')


def get_connection():
    conn = mc.connect(user='root', password='lyqNYU617?', host='127.0.0.1',
                      database='coincenter', auth_plugin='mysql_native_password')
    return conn
