from flask import *
import pymysql
#start
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book',methods=['POST','GET'])

def book():
    if request.method=='POST':
         connection =pymysql.connect(host='localhost',user='root',password='',database='Denzil-flight')

         
         departure= request.form['departure']
         destination= request.form['destination']
         date= request.form['date']
         time= request.form['time']

         cursor=connection.cursor()
         sql='INSERT INTO bookings( depart,destination,date,time) VALUES(%s,%s,%s,%s)'
         cursor.execute(sql,(departure,destination,date,time))
         connection.commit()

         return 'Successfully booked your flight'
    else:
        return render_template('book.html')



        
# SIGNING UP PROCEDURE
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        connection=pymysql.connect(host='localhost',user='root',password='',database='Denzil-flight')

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        cursor = connection.cursor()
        sql = 'INSERT INTO register (first_name,last_name,email,password) VALUES(%s,%s,%s,%s)'
        cursor.execute(sql,(first_name,last_name,email,password))
        connection.commit()

        return'You have registered successfuly'

    else:

        return render_template('register.html')

#LOG IN PROCEDURE FOR CODING

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        connection=pymysql.connect(host='localhost',user='root',password='',database='Denzil-flight')

        email    = request.form['email']
        password = request.form['password']

        cursor =connection.cursor()
        sql ='SELECT*FROM register WHERE email= %s AND password= %s'
        cursor.execute(sql,(email,password))
        
        if cursor.rowcount==0:
            return render_template('login.html',msg='ERROR, Wrong credentials')
        elif cursor.rowcount==1:
            return redirect('/book')
        else:
            return render_template('login.html', msg='something went wrong')
            

    else:
         return render_template('login.html')


# FETCHING DATA
@app.route('/passengers')
def passengers():
   connection= pymysql.connect(host='localhost', user='root', password='', database='Denzil-flight' )
   cursor= connection.cursor()
   sql= 'SELECT*FROM bookings'
   cursor.execute(sql)

   data= cursor.fetchall()
   return render_template('passenger.html',rows=data)

# HIRE   
@app.route('/hire')
def hire():
    connection =pymysql.connect(host='localhost', user='root', password='', database='test-denzil')
    
    cursor= connection.cursor()

    sql='SELECT * FROM hire'
    cursor.execute(sql)

    if cursor.rowcount ==0:
        return render_template ('hire.html', message='no cars available for hire today')

    else:
        data = cursor.fetchall()
        return render_template('hire.html', rows=data)


#MPESA PAYMENT METHOD
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth
@app.route('/mpesa', methods = ['POST','GET'])
def mpesa():
        if request.method == 'POST':
            phone = str(request.form['phone'])
            amount = str(request.form['amount'])
            # GENERATING THE ACCESS TOKEN
            consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
            consumer_secret = "amFbAoUByPV2rM5A"

            api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" #AUTH URL
            r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

            data = r.json()
            access_token = "Bearer" + ' ' + data['access_token']

            #  GETTING THE PASSWORD
            timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
            passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
            business_short_code = "174379"
            data = business_short_code + passkey + timestamp
            encoded = base64.b64encode(data.encode())
            password = encoded.decode('utf-8')


            # BODY OR PAYLOAD
            payload = {
                "BusinessShortCode": "174379",
                "Password": "{}".format(password),
                "Timestamp": "{}".format(timestamp),
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,  # use 1 when testing
                "PartyA": phone,  # change to your number
                "PartyB": "174379",
                "PhoneNumber": phone,
                "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
                "AccountReference": "account",
                "TransactionDesc": "account"
            }

            # POPULAING THE HTTP HEADER
            headers = {
                "Authorization": access_token,
                "Content-Type": "application/json"
            }

            url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #C2B URL

            response = requests.post(url, json=payload, headers=headers)
            print (response.text)
            return render_template('complete.html')
        else:
            return redirect('/hire')

#justpaste.it/7rk4w - mpesa option link
#github.com/bigboyfreezy/system

app.run(debug=True)

#End
