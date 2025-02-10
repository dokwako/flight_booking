import pymysql
def insert():
    connection= pymysql.connect(host="localhost",user="root",password="",database="Denzil-flight")
    print("database connected succesfully")

    cargo_id ="500132"
    cargo_name = "poltry"
    cargo_weight="10 tonnes"
    cargo_destination ="nairobi"

    cursor = connection.cursor()
    sql= 'INSERT INTO cargo(cargo_name,cargo_weight,cargo_destination) VALUES(%s,%s,%s)'
    cursor.execute (sql,(cargo_name,cargo_weight,cargo_destination))
    connection.commit()

    print("YEES")
    
insert()


x= ' YEES'
def myfunc():
    print("python is my languge"+ x)

myfunc()

x= 'GO HOME'
def myfunc():
    global x
    x=' I WILL COME'

    print("DENZIL"+ x)
myfunc()

