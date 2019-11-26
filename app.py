from flask import Flask
from flask import render_template
from flask import request
import mysql.connector as mc

app = Flask(__name__)


def get_connection():
    conn = mc.connect(user='root', password='7938008wang', host='127.0.0.1',
                      database='coincenter', auth_plugin='mysql_native_password')
    return conn


class user:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @app.route("/")
    def log_in():

        # conn = get_connection()
        # result = conn.cmd_query("select * from product")
        # rows = conn.get_rows()
        # conn.close()

        # product = rows[0]
        return render_template('main.html')

    @app.route("/Account.html")
    def show_acoount():
        return render_template('Account.html')


class market:

    @app.route("/showMarket")
    def get_market_value():
        return render_template('Market.html')


class trade:

    def __init__(self, q, p, s):
        self.quantity = q
        self.price = p
        self.symbol = s

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_q_value):
        self.quantity = new_q_value

    def get_price(self):
        return self.price

    def set_price(self, new_p_value):
        self.price = new_p_value

    def get_symbol(self):
        conn = get_connection()
        result = conn.cmd_query("select coin_name from coins where coin_id = 1")
        rows = conn.get_rows()
        conn.close()
        return str(rows[0])
        

    def set_symbol(self, new_s_value):
        self.symbol = new_s_value

    @app.route("/sell.html")
    def sell():
        conn = get_connection()
        cursor = conn.cursor()
        conn.close()
        return render_template('sell.html')
    
    @app.route('/buy.html')
    def buy():
        cointype = trade(1,10000,'Bitcoin')
        return render_template('buy.html')
    
    @app.route('/ordersuccess.html')
    def show_order():
        return render_template('ordersuccess.html')
    
    @app.route('/pnl.html')
    def show_pnl():
        return render_template('pnl.html')
    
    @app.route('/Market.html')
    def show_market():
        return render_template('Market.html')
    
    @app.route('/contact.html')
    def show_contact():
        return render_template('contact.html')
    
    
    

    


# @app.route("/showProducts")
# def show_products():

#     conn = get_connection()
#     result = conn.cmd_query("select * from product")
#     rows = conn.get_rows()
#     conn.close()
#     return str(rows[0])


# # @app.route("/submitstuff",methods=['post'])
# # def get_submission():
# #     #ms = request.args.get('mystuff')
# #     #myssn = request.args.get('myssn')
# #     ms = request.form['mystuff']
# #     myssn = request.form['myssn']
# #     print('my stuff is',ms)
# #     print('my ssn is',myssn)
# #     return "you sent in <b>" + ms + "</b>"


# @app.route("/")
# def main_page():

#     conn = get_connection()
#     result = conn.cmd_query("select * from product")
#     rows = conn.get_rows()
#     conn.close()

#     product = rows[0]
#     return render_template('main.html')


# @app.route("/showMarket", methods=['post'])
# def show_market():
#     return render_template('Market.html')


# @app.route("/userAccount")
# def show_acoount():
#     return render_template('Account.html')

# @app.route("/userAccount")
# def show_acoount():
#     return render_template('Account.html')
