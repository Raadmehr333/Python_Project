import mysql.connector
from config import *

config = {"user": databse_user, "password": databse_password, "host": "localhost", "database": database_name}


# insert user info into database.
# اطلاعات کاربر رو وارد پایگاه داده میکند.
def insert_info(ID, name, personal_id, age, gender, profile_pic, province, latitude, longitude, coins, invite_link, privet_link):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = "INSERT INTO USER(ID, NAME, PERSONAL_IDENTIFICATION_LINK, AGE, GENDER, PROFILE_PIC, PROVINCE, LATITUDE, LONGITUDE, NUMBER_OF_COINS, INVITATION_LINK, UNKNOWN_LINK) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(SQL_QUERY, (ID, name, personal_id, age, gender, profile_pic, province, latitude, longitude, coins, invite_link, privet_link))
    conn.commit()
    cursor.close()
    conn.close()

def edit_name(cid, new_name):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    UPDATE_QUERY = "UPDATE USER SET NAME = %s WHERE ID= %s"
    cursor.execute(UPDATE_QUERY, (new_name, cid))
    conn.commit()
    cursor.close()
    conn.close()

def edit_gender(cid, new_gender):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    UPDATE_QUERY = "UPDATE USER SET GENDER = %s WHERE ID = %s"
    cursor.execute(UPDATE_QUERY, (new_gender, cid))
    conn.commit()
    cursor.close()
    conn.close()

def edit_age(cid, new_age):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    UPDATE_QUERY = "UPDATE USER SET AGE = %s WHERE ID = %s"
    cursor.execute(UPDATE_QUERY, (new_age, cid))
    conn.commit()
    cursor.close()
    conn.close()

def edit_province(cid, new_province):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    UPDATE_QUERY = "UPDATE USER SET PROVINCE = %s WHERE ID = %s"
    cursor.execute(UPDATE_QUERY, (new_province, cid))
    conn.commit()
    cursor.close()
    conn.close()

def edit_profile_pic(cid, new_file_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    UPDATE_QUERY = "UPDATE USER SET PROFILE_PIC = %s WHERE ID = %s"
    cursor.execute(UPDATE_QUERY, (new_file_id, cid))
    conn.commit()
    cursor.close()
    conn.close()

def edit_latitude(cid, new_latitude):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    UPDATE_QUERY = "UPDATE USER SET LATITUDE = %s WHERE ID = %s"
    cursor.execute(UPDATE_QUERY, (new_latitude, cid))
    conn.commit()
    cursor.close()
    conn.close()

def edit_longitude(cid, new_longitude):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    UPDATE_QUERY = "UPDATE USER SET LONGITUDE = %s WHERE ID = %s"
    cursor.execute(UPDATE_QUERY, (new_longitude, cid))
    conn.commit()
    cursor.close()
    conn.close()

def add_coin_to_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"UPDATE USER SET NUMBER_OF_COINS = NUMBER_OF_COINS + 4 WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()

def add_purchased_coin(cid, credit):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"UPDATE USER SET NUMBER_OF_COINS = NUMBER_OF_COINS + {credit} WHERE ID = {cid}"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()

def insert_into_contacts(cid, name, personal_link):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = "INSERT INTO CONTACTS(CONTACT_ID, CONTACT_NAME, CONTACT_PERSONAL_LINK) VALUES(%s, %s, %s);"
    cursor.execute(SQL_QUERY, (cid, name, personal_link))
    conn.commit()
    cursor.close()
    conn.close()

def insert_cid_to_contacts(cid, contact_id, contact_name, contact_personal_link):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = "INSERT INTO CONTACTS_USERS_ROW(ID, CONTACT_ID, CONTACT_NAME, CONTACT_PERSONAL_LINK) VALUES(%s, %s, %s, %s)"
    cursor.execute(SQL_QUERY, (cid, contact_id, contact_name, contact_personal_link))
    conn.commit()
    cursor.close()
    conn.close()

def insert_into_blocked_users(cid, name, personal_link):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = "INSERT INTO BLOCKED_USERS(USER_ID, USER_NAME, USER_PERSONAL_ID) VALUES(%s, %s, %s);"
    cursor.execute(SQL_QUERY, (cid, name, personal_link))
    conn.commit()
    cursor.close()
    conn.close()

def insert_cid_to_blocked_users(cid, blocked_id, blocked_name, blocked_personal_link):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = "INSERT INTO BLOCKED_USERS_ROW(ID, USER_ID, USER_NAME, USER_PERSONAL_ID) VALUES(%s, %s, %s, %s)"
    cursor.execute(SQL_QUERY, (cid, blocked_id, blocked_name, blocked_personal_link))
    conn.commit()
    cursor.close()
    conn.close()

def unblock_user_by_cid(user_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    user = int(user_id)
    SQL_QUERY = f"DELETE FROM BLOCKED_USERS WHERE USER_ID = {user};"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()

def unblock_user_by_cid1(user_id):
    print(type(user_id))
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    user = int(user_id)
    SQL_QUERY = f"DELETE FROM BLOCKED_USERS_ROW WHERE USER_ID = {user};"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()

def delete_contact_by_cid(user_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    user = int(user_id)
    SQL_QUERY = f"DELETE FROM CONTACTS WHERE CONTACT_ID = {user}"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()

def delete_contact_by_cid1(user_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    user = int(user_id)
    SQL_QUERY = f"DELETE FROM CONTACTS_USERS_ROW WHERE CONTACT_ID = {user}"
    cursor.execute(SQL_QUERY)
    conn.commit()
    cursor.close()
    conn.close()

def insert_purchase_invoice(cid, product_id, credit, price):
    pass

if __name__ == "__main__":
    insert_info()
    edit_name()
    edit_gender()
    edit_age()
    edit_province()
    edit_profile_pic()
    edit_latitude()
    edit_longitude()