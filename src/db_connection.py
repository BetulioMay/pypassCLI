import mysql.connector
from src.keys import keys

mydb = mysql.connector.connect(
    host='localhost',
    user=keys['user'],
    password=keys['password'],
    database=keys['database']
)

mycursor = mydb.cursor()
