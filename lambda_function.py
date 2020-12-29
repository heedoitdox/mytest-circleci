import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
endpoint=os.Getenv("DB_HOST")
username=os.Getenv("DB_USERNAME")
password=os.Getenv("DB_PASSWORD")
database_name=os.Getenv("DB_NAME")

connection = pymysql.connect(os.Getenv("DB_HOST"), user=username, passwd=password, db=database_name)

def lambda_handler(event, context) :
    

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM orders')

    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))