# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:39:04 2024

@author: zliu442
"""

import mysql.connector

myconn = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='bemysql',
    database='world'
    )

mycursor = myconn.cursor()

mycursor.execute("SELECT*FROM country")

myresult = mycursor.fetchall()

for x in myresult:
    print (x)
    
import panda as pd

sql = "SELECT * FROM country where Continent= 'Oceania'"

df = pd.read_sql_query(sql,myconn)

from sqlalchemy import create_engine

myengine = create_engine("mysql+mysqconnector://root:bemysql@localhost:3307//world")

df = pd.read_sql_table("country",myengine)
