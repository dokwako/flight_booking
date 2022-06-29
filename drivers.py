from flask import *
import pymysql

app = Flask(__name__)
@app.route('/save', methods=['POST','GET'])
def save():
    if request.method=='POST':
        connection=pymysql.connect(host='localhost',user='root',password='',database='Denzil-flight')        
        driver_name=request.form['driver_name']
        driver_phone=request.form['driver_phone']
        idnumber=request.form['idnumber']
        car_assigned=request.form['car_assigned']

        cursor=connection.cursor()
        sql='INSERT INTO driver(driver_name,driver_phone,idnumber,car_assigned) VALUES(%s,%s,%s,%s)'
        cursor.execute(sql,(driver_name,driver_phone,idnumber,car_assigned))
        connection.commit()
        return render_template('/savedriver.html', message= 'SAVED SUCCUESSFULLY')      

    else:
        return render_template('/savedriver.html')

app.route('/all')
def all():
    connection=pymysql.connect(host='localhost',user='root',password='',database='Denzil-flight')
    




app.run(debug=True)