from crypt import methods
from flask import*

app = Flask(__name__)

import pymysql
@app.route('/bookflight',methods=['POST','GET'])
def insert():
    if request.method== 'POST':
        #Establishing  a database connection
        connection = pymysql.connect(host="localhost",user="root",password="",database="Denzil-flight")
        # Testing the coonection 
        print("database connected succesfully")


        depart=request.form['departure']
        destination= request.form['destination']
        date= request.form['date']
        time= request.form['time']
        cursor = connection.cursor()
        sql = 'INSERT INTO bookings(depart,destination,date,time) VALUES(%s,%s,%s,%s)'
        cursor.execute(sql,(depart,destination,date,time))
        connection.commit()
        
        return 'WORKING'
    else:
        return render_template('book.html')
        

app.run(debug=True)