import mysql.connector
from mysql.connector import Error
import pandas as pd


#covid_db=mysql.connector.connect(host="localhost", user='root',password="12345678", database="covid19_Tweets")

#my_cursor=covid_db.cursor()
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password

        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


pw = "" # IMPORTANT! Put your MySQL Terminal password here.
db = "covid19_Tweets" # This is the name of the database we will create in the next step - call it whatever you like.

connection = create_server_connection("localhost", "root", pw)



def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


create_database_query = "CREATE DATABASE covid19_Tweets"
create_database(connection, create_database_query)


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection



def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


create_tweets_table = """
CREATE TABLE tweets (
    id INT NOT NULL AUTO_INCREMENT,
    created_at DATE NOT NULL,
    source VARCHAR(200) NOT NULL,
    original_text TEXT DEFAULT NULL,
    polarity FLOAT DEFAULT NULL,
    subjectivity FLOAT DEFAULT NULL,
    lang TEXT DEFAULT NULL,
    favorite_count INT DEFAULT NULL,
    retweet_count INT DEFAULT NULL,
    original_author TEXT DEFAULT NULL,
    followers_count INT DEFAULT NULL,
    friends_count INT DEFAULT NULL,
    possibly_sensitive TEXT DEFAULT NULL,
    hashtags TEXT DEFAULT NULL,
    user_mentions TEXT DEFAULT NULL,
    place TEXT DEFAULT NULL,
    clean_text TEXT DEFAULT NULL,
    PRIMARY KEY (id)
  );
 """

connection = create_db_connection("localhost", "root", pw, db) # Connect to the Database
execute_query(connection, create_tweets_table) # Execute our defined query