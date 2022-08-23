#..............................UI design of Information Diffusion Page.....................................

# Importing necessary libraries

import streamlit as st # for User Interface design and visualization
import networkx as nx # for networkx graphs visualization
import matplotlib.pyplot as plt #for data manipulation and visualization of social media networks
import pandas as pd # for data frames manipulation
import plotly.express as px # for data visualization
from PIL import Image # to import images to User Interface (UI)
import requests # to assist importing images to User Interface (UI)
from io import BytesIO # to assist importing images to User Interface (UI)

import warnings
warnings.filterwarnings("ignore")

#.....................Polarity analysis of A/L Kuppiya Youtube channel comments...................

import pandas as pd

with open('likes_and_reactions_made_by_your_page.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile, orient='index')
print(df)

df.to_csv('likes_and_reactions_by_page2.csv', encoding='utf-8', index=True)

import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sma_dashboard_ud',
                                         user='root',
                                         password='Tesla@1234')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

 #   Python Fetch MySQL row using the column names

    sql_select_Query = "SELECT * FROM sma_dashboard_ud.friends_data"
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    print("Fetching each row using column name")
    for row in records:
        id = row["id"]
        name = row["name"]
        timestamp = row["timestamp"]
        insert_date = row["insert_date"]
        print(id, name, timestamp, insert_date)


except Error as e:
    print("Error while connecting to MySQL", e)
'''finally:
    if connection.is_connected():
        cursor.close()
        connection.close() 
        print("MySQL connection is closed")'''


import networkx as nx
import matplotlib.pyplot as plt
df = pd.read_csv (r'likes_and_reactions_by_page4.csv')
print (df)
G = nx.from_pandas_edgelist(df,source='post_owner',target="reaction_type",create_using = nx.Graph())
type(G)

G.nodes()

len(G.nodes())

G.edges()

len(G.edges())

nx.info(G)

nx.draw(G,with_labels=True)



pos = nx.spring_layout(G)
betCent = nx.betweenness_centrality(G, normalized=True, endpoints=True)
node_color = [20000.0 * G.degree(v) for v in G]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(G, pos=pos, with_labels=True,
node_color=node_color,
node_size=node_size )
plt.axis('off')
sorted(betCent, key=betCent.get, reverse=True)[:8]


pos = nx.spring_layout(G)
betCent = nx.degree_centrality(G)
node_color = [20000.0 * G.degree(v) for v in G]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(G, pos=pos, with_labels=True,
node_color=node_color,
node_size=node_size )
plt.axis('off')
sorted(betCent, key=betCent.get, reverse=True)[:8]


pos = nx.spring_layout(G)
betCent = nx.eigenvector_centrality(G)
node_color = [20000.0 * G.degree(v) for v in G]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20,20))
nx.draw_networkx(G, pos=pos, with_labels=True,
node_color=node_color,
node_size=node_size )
plt.axis('off')
sorted(betCent, key=betCent.get, reverse=True)[:8]


'''Information Diffusion of DFCC Bank Offical YouTube Channel'''

# Importing necessary libraries

from googleapiclient.discovery import build # for data extraction via google API
from google.oauth2 import service_account #to access the google service account
import networkx as nx # for networkx graphs visualization
import matplotlib.pyplot as plt #for data manipulation and visualization of social media networks
import pandas as pd # for data frames manipulation

#Data extraction via google API

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None

creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,scopes = SCOPES)

SPREADSHEET_ID = '1EhqijIfjQVtNHznhMadBE1lrzVXKHeIWOPptD8L9O_E'
