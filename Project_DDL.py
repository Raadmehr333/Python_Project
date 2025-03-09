import mysql.connector
from config import *

config = {"user": databse_user, "password": databse_password, "host": "localhost", "database": database_name}

def create_database(db_name):
    config = {"user": databse_user, "password": databse_password, "host": "localhost"}
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"DROP DATABASE IF EXISTS {db_name}"
    cursor.execute(SQL_QUERY)
    SQL_QUERY = f"CREATE DATABASE {db_name}"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("DATABASE CREATED SUCCESSFULLY")

def create_table_user():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = """CREATE TABLE USER(
        `ID`                                        VARCHAR(15) NOT NULL,
        `NAME`                                      VARCHAR(50) NOT NULL,
        `PERSONAL_IDENTIFICATION_LINK`              VARCHAR(20) NOT NULL,
        `AGE`                                       VARCHAR(2) NOT NULL,
        `GENDER`                                    ENUM("Male", "Female"),
        `PROFILE_PIC`                               VARCHAR(150) NOT NULL,
        `PROVINCE`                                  VARCHAR(20) NOT NULL,
        `LATITUDE`                                  FLOAT,
        `LONGITUDE`                                 FLOAT,
        `NUMBER_OF_COINS`                           SMALLINT UNSIGNED NOT NULL DEFAULT 5,
        `INVITATION_LINK`                           VARCHAR(120) NOT NULL,
        `UNKNOWN_LINK`                              VARCHAR(130) NOT NULL,
        PRIMARY KEY(`ID`)
    );"""
    cursor.execute(SQL_QUERY)
    cursor.execute("CREATE INDEX idx_user_id ON USER(ID);")
    cursor.execute("CREATE INDEX idx_user_name ON USER(NAME);")
    cursor.execute("CREATE INDEX idx_user_personal_link ON USER(PERSONAL_IDENTIFICATION_LINK);")
    conn.commit()
    cursor.close()
    conn.close()
    print("TABLE USER CREATED SUCCESSFULLY")

def create_table_contacts():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = """CREATE TABLE CONTACTS(
        `ROW_ID`                        INT AUTO_INCREMENT PRIMARY KEY,
        `CONTACT_ID`                    VARCHAR(15) NOT NULL,
        `CONTACT_NAME`                  VARCHAR(50) NOT NULL,
        `CONTACT_PERSONAL_LINK`         VARCHAR(20) NOT NULL,
        FOREIGN KEY(`CONTACT_ID`) REFERENCES USER(`ID`),
        FOREIGN KEY(`CONTACT_NAME`) REFERENCES USER(`NAME`),
        FOREIGN KEY(`CONTACT_PERSONAL_LINK`) REFERENCES USER(`PERSONAL_IDENTIFICATION_LINK`),


        UNIQUE(`CONTACT_ID`)            
    );"""
    cursor.execute(SQL_QUERY)
    conn.commit()
    
    cursor.execute("CREATE INDEX idx_contact_id ON CONTACTS(`CONTACT_ID`);")
    cursor.execute("CREATE INDEX idx_contact_name ON CONTACTS(`CONTACT_NAME`);")
    cursor.execute("CREATE INDEX idx_contact_personal_link ON CONTACTS(`CONTACT_PERSONAL_LINK`);")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("TABLE CONTACTS CREATED SUCCESSFULLY")

def create_table_blocked_users():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = """CREATE TABLE BLOCKED_USERS(
        `ROW_ID`                INT AUTO_INCREMENT PRIMARY KEY,
        `USER_ID`               VARCHAR(12) NOT NULL,
        `USER_NAME`             VARCHAR(50) NOT NULL,
        `USER_PERSONAL_ID`      VARCHAR(20) NOT NULL,
        UNIQUE(`USER_ID`)       
    );"""
    cursor.execute(SQL_QUERY)
    conn.commit()
    
    cursor.execute("CREATE INDEX idx_blocked_user_id ON BLOCKED_USERS(`USER_ID`);")
    cursor.execute("CREATE INDEX idx_blocked_user_name ON BLOCKED_USERS(`USER_NAME`);")
    cursor.execute("CREATE INDEX idx_blocked_user_personal_id ON BLOCKED_USERS(`USER_PERSONAL_ID`);")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("TABLE BLOCKED USERS CREATED SUCCESSFULLY")

def create_contacts_users_row():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = """CREATE TABLE CONTACTS_USERS_ROW(
        `ROW_ID`                        INT AUTO_INCREMENT PRIMARY KEY,
        `ID`                            VARCHAR(12) NOT NULL,
        `CONTACT_ID`                    VARCHAR(15) NOT NULL,
        `CONTACT_NAME`                  VARCHAR(50) NOT NULL,
        `CONTACT_PERSONAL_LINK`         VARCHAR(20) NOT NULL,
        FOREIGN KEY(`ID`) REFERENCES USER(`ID`),
        FOREIGN KEY(`CONTACT_ID`) REFERENCES CONTACTS(`CONTACT_ID`),
        FOREIGN KEY(`CONTACT_NAME`) REFERENCES CONTACTS(`CONTACT_NAME`),
        FOREIGN KEY(`CONTACT_PERSONAL_LINK`) REFERENCES CONTACTS(`CONTACT_PERSONAL_LINK`)
    );"""
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("TABLE CONTACTS USERS ROW CREATED SUCCESSFULLY")

def create_blocked_users_row():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = """CREATE TABLE BLOCKED_USERS_ROW(
        `ROW_ID`                INT AUTO_INCREMENT PRIMARY KEY,
        `ID`                    VARCHAR(12) NOT NULL,
        `USER_ID`               VARCHAR(12) NOT NULL,
        `USER_NAME`             VARCHAR(50) NOT NULL,
        `USER_PERSONAL_ID`      VARCHAR(20) NOT NULL,
        FOREIGN KEY(`ID`) REFERENCES USER(`ID`),
        FOREIGN KEY(`USER_ID`) REFERENCES BLOCKED_USERS(`USER_ID`),
        FOREIGN KEY(`USER_NAME`) REFERENCES BLOCKED_USERS(`USER_NAME`),
        FOREIGN KEY(`USER_PERSONAL_ID`) REFERENCES BLOCKED_USERS(`USER_PERSONAL_ID`)
    );"""
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("TABLE BLOCKED USERS ROW CREATED SUCCESSFULLY")

def create_table_coins():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = """CREATE TABLE COINS(
        `PRODUCT_ID`                SMALLINT NOT NULL AUTO_INCREMENT,
        `CREDIT`                    SMALLINT NOT NULL,
        `PRICE`                     MEDIUMINT UNSIGNED NOT NULL,
        PRIMARY KEY(`PRODUCT_ID`),
        UNIQUE(`CREDIT`), 
        UNIQUE(`PRICE`)
    );"""
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("TABLE COINS CREATED SUCCESSFULLY")

def create_table_sales():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = """CREATE TABLE SALES(
        `SALE_ID`               SMALLINT NOT NULL AUTO_INCREMENT,
        `DATE`                  DATETIME NOT NULL,
        PRIMARY KEY(`SALE_ID`),
        UNIQUE(`DATE`)
    );"""
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("TABLE SALES CREATED SUCCESSFULLY")

def create_table_sales_row():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = """CREATE TABLE SALES_ROW(
        `ROW_ID`                SMALLINT NOT NULL AUTO_INCREMENT,
        `ID`                    VARCHAR(15) NOT NULL,
        `PRODUCT_ID`            SMALLINT NOT NULL,
        `CREDIT`                SMALLINT NOT NULL,
        `PRICE`                 MEDIUMINT UNSIGNED NOT NULL,
        `DATE`                  DATETIME NOT NULL,
        PRIMARY KEY(`ROW_ID`),
        FOREIGN KEY(`ID`) REFERENCES USER(`ID`),
        FOREIGN KEY(`PRODUCT_ID`) REFERENCES COINS(`PRODUCT_ID`),
        FOREIGN KEY(`CREDIT`) REFERENCES COINS(`CREDIT`),
        FOREIGN KEY(`PRICE`) REFERENCES COINS(`PRICE`),
        FOREIGN KEY(`DATE`) REFERENCES SALES(`DATE`)           

    );"""
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("TABLE SALES_ROW CREATED SUCCESSFULLY")

def insert1(credit, price):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"INSERT INTO COINS (CREDIT, PRICE) VALUES({credit}, {price});"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("FIRST_PRODUCT_ADDED")

def insert2(credit, price):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"INSERT INTO COINS (CREDIT, PRICE) VALUES({credit}, {price});"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("SECOND_PRODUCT_ADDED")

def insert3(credit, price):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"INSERT INTO COINS (CREDIT, PRICE) VALUES({credit}, {price});"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("THIRD_PRODUCT_ADDED")   

def insert4(credit, price):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"INSERT INTO COINS (CREDIT, PRICE) VALUES({credit}, {price});"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()
    print("FOURTH_PRODUCT_ADDED")

if __name__ == "__main__":
    create_database(database_name)
    create_table_user()
    create_table_contacts()
    create_table_blocked_users()
    create_contacts_users_row()
    create_blocked_users_row()
    create_table_coins()
    create_table_sales()
    create_table_sales_row()
    insert1(280, 100000)  
    insert2(490, 185000)
    insert3(1400, 285000)
    insert4(2700, 400000)