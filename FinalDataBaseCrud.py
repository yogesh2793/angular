import sqlite3 as sql
def create_connection(dataBaseName):

    try:
        conn = sql.connect(dataBaseName+".db")
        sqlite3.connect("dataBaseName")
        return conn
    except Error as e:
        print(e)
    return None

def createTable(conn):
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(name TEXT,phone Int)''')
    conn.commit()


def insertData(conn):
    cur=conn.cursor()
    size=int(input("enter how many data\n"))
    for i in range(size):
        name=input("enter a name:")
        phone=input("enter phone:")
        cur.execute('''INSERT INTO users(name, phone) VALUES(?,?)''', (name,phone))
        conn.commit()
    print(' user  inserted')
def readData(conn):
    cur=conn.cursor()
    cur.execute("select * from users") #row=cur.fetchall()
    for i in cur:
        name=i[0]
        phone=i[1]
        print("name is {} and phone number is {}".format(name,phone))
    conn.commit()

def updateData(conn):
    cur=conn.cursor()
    Name=input("enter newName ")
    NewPhone=int(input("enter Newphone"))
    cur.execute('''UPDATE users SET phone = ? WHERE name = ? ''',(NewPhone, Name))
    conn.commit()


def deleteData(conn):
    cur=conn.cursor()
    name =input("enter name to delete\n")
    cur.execute('''DELETE FROM users WHERE name = ? ''', (name,))
    conn.commit()


def mainFunction():
    dataBaseName=input("Enter dataBaseName\n")
    conn=create_connection(dataBaseName)
    #createTable(conn)
    #insertData(conn)
    #readData(conn)
    #updateData(conn)
    #deleteData(conn)
    #readData(conn)
mainFunction()
