import requests
import json
from datetime import date
from datetime import datetime
import mysql.connector 
bbc_url = ('http://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=8c14e125c1ec43099823d66473dc9f43')
bbc_response = requests.get(bbc_url)
bbc_articles = bbc_response.json()["articles"]
fox_url = ('http://newsapi.org/v2/top-headlines?'
       'sources=fox-news&'
       'apiKey=8c14e125c1ec43099823d66473dc9f43')
fox_response = requests.get(fox_url)
fox_articles = fox_response.json()["articles"]
cnn_url = ('http://newsapi.org/v2/top-headlines?'
       'sources=cnn&'
       'apiKey=8c14e125c1ec43099823d66473dc9f43')
cnn_response = requests.get(cnn_url)
cnn_articles = cnn_response.json()["articles"]
mydb = mysql.connector.connect(
  host="contentgen.c5qqgnfc1gnd.us-east-1.rds.amazonaws.com",
  user="admin",
  password="Kutya11!",
  database="content"
)
mycursor = mydb.cursor()
def transform(obj):
    source = obj["source"]["id"]
    title = obj["title"]
    description = obj["description"]
    url = obj["url"]
    url_content = obj["urlToImage"]
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    formatted_date
    out = (source,title,description,url,url_content,formatted_date)
    return out

def insert(mycursor,values):
    try:
        sql = "insert into page_content(source,title,description,url,url_content,date) values (%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,values)
    except:
        print("error with sql")

def delete(mycursor):
    sql = "delete from page_content"
    mycursor.execute(sql)
    
for article in cnn_articles:
    insert(mycursor,transform(article))
for article in bbc_articles:
    insert(mycursor,transform(article))
for article in fox_articles:
    insert(mycursor,transform(article))
mydb.commit()

