import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
endpoint=os.getenv("DB_HOST")
username=os.getenv("DB_USERNAME")
password=os.getenv("DB_PASSWORD")
database_name=os.getenv("DB_NAME")

connection = pymysql.connect(endpoint, user=username, passwd=password, db=database_name)

def lambda_handler(event, context) :
    

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM orders')

    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))