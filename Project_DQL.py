import mysql.connector
from Project_texts import text as keyboardbutton
from config import *

config = {"user": databse_user, "password": databse_password, "host": "localhost", "database": database_name}

def get_cid():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = "SELECT ID FROM USER;"
    cursor.execute(SQL_QUERY)
    cid = cursor.fetchall()
    str_cid = cid
    result = list()
    for i in str_cid:
        result.append(i[0])
    conn.commit()
    cursor.close()
    conn.close()
    if not result:
        return ""
    else:
        return result

def get_user_info_by_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT * FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    user_info = cursor.fetchall()
    str_user_info = user_info[0]
    conn.commit()
    cursor.close()
    conn.close()
    return str_user_info

def send_location(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT LATITUDE, LONGITUDE FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    latitude, longitude = cursor.fetchall()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return latitude, longitude

def get_cid_by_private_link(p_link):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT ID FROM USER WHERE UNKNOWN_LINK = {p_link};"
    cursor.execute(SQL_QUERY)
    target_cid = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return target_cid

def invite_link_gen(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT INVITATION_LINK FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    invite_link_hash_value = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    text = f"{keyboardbutton["b38"]}\n{keyboardbutton["b36"]}\nhttps://t.me/Pyhton_testvb_bot?start={invite_link_hash_value}"
    return text
    

def private_link_gen(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT UNKNOWN_LINK FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    private_link_hash_value = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    text = f"{keyboardbutton["b37"]}\nhttps://t.me/Pyhton_testvb_bot?start={private_link_hash_value}"
    return text

def get_name_by_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT NAME FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    name = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return name

def get_personal_id_by_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT PERSONAL_IDENTIFICATION_LINK FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    personal_id = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    return personal_id


def get_invite_links():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QEURY = "SELECT INVITATION_LINK FROM USER;"
    cursor.execute(SQL_QEURY)
    invite_links_numeric_part = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return invite_links_numeric_part

def get_private_links():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QEURY = "SELECT UNKNOWN_LINK FROM USER;"
    cursor.execute(SQL_QEURY)
    private_links_numeric_part = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return private_links_numeric_part

def get_cid_by_invite_link(invite_link):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT ID FROM USER WHERE INVITATION_LINK = {invite_link};"
    cursor.execute(SQL_QUERY)
    target_cid = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    return target_cid

def get_coin_numbers_by_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT NUMBER_OF_COINS FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    coins = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    return coins

def get_coins_credit_by_id(ID):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT CREDIT FROM COINS WHERE PRODUCT_ID = {ID};"
    cursor.execute(SQL_QUERY)
    credit = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    return credit

def get_coins_price_by_id(ID):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT PRICE FROM COINS WHERE PRODUCT_ID = {ID};"
    cursor.execute(SQL_QUERY)
    price = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    return price

def search_user(selected_provinces, age_range):
    min_age = min(age_range)
    max_age = max(age_range)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    selected_provinces = "('" + "','".join(selected_provinces) + "')"
    SQL_QUERY = f"SELECT ID FROM USER WHERE PROVINCE IN {selected_provinces} AND AGE BETWEEN {min_age} AND {max_age} ORDER BY RAND() LIMIT 10;"
    cursor.execute(SQL_QUERY)
    users = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    print(users)
    if not users:
         return "nothing"
    else:
        return users[0]

def organize_the_text(users):
    text = ""
    counter = 1
    if users == "nothing" or text == "":
        return keyboardbutton["b63"]
    else:
        for i in users:
            name = get_name_by_cid(i)[0][0]
            personal_id = get_personal_id_by_cid(i)
            text += f"{counter}_{name}\n{personal_id}\n\n-----------------------\n"
            counter += 1
        return text
    
def organize_the_text_for_contacts_section(users):
    text = ""
    counter = 1
    if users == "nothing":
        return keyboardbutton["b63"]
    else:
        for i in users:
            name = get_name_by_cid(i)[0][0]
            link = get_personal_id_by_cid(i)
            text += f"{counter}_{name}\n{link}\n\n-----------------------\n"
            counter += 1
        return text

def get_cid_by_personal_id(personal_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT ID FROM USER WHERE PERSONAL_IDENTIFICATION_LINK = '{personal_id}';"
    cursor.execute(SQL_QUERY)
    cid = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if not cid:
        return "this link does not belong to any user of this bot."
    else:
        return cid[0][0]
    
def get_private_link_by_personal_id(personal_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT UNKNOWN_LINK FROM USER WHERE PERSONAL_IDENTIFICATION_LINK = {personal_id};"
    cursor.execute(SQL_QUERY)
    private_link_numeric_part = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    return private_link_numeric_part

def get_name_by_personal_id(personal_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT NAME FROM USER WHERE PERSONAL_IDENTIFICATION_LINK = '{personal_id}';"
    cursor.execute(SQL_QUERY)
    user_name = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    return user_name

def get_contacts_by_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT CONTACT_ID FROM CONTACTS_USERS_ROW WHERE ID = {cid}"
    cursor.execute(SQL_QUERY)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if not result:
        return "nothing"
    else:
        return result[0]
    
def get_blocked_users_by_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT USER_ID FROM BLOCKED_USERS_ROW WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    users = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if not users:
        return "nothing"
    else:
        return users[0]

def get_province_by_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT PROVINCE FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    result = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    return result

def get_age_by_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT AGE FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    result = cursor.fetchall()[0][0]
    conn.commit()
    cursor.close()
    conn.close()
    return result

def get_same_age_only_male_users_by_age(age, preferred_gender):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT ID FROM USER WHERE AGE = {age} AND GENDER = '{preferred_gender}';"
    cursor.execute(SQL_QUERY)
    users = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if not users:
        return "nothing"
    else:
        return users[0]

def get_same_age_only_female_users_by_age(age, preferred_gender):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT ID FROM USER WHERE AGE = {age} AND GENDER = '{preferred_gender}';"
    cursor.execute(SQL_QUERY)
    users = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if not users:
        return "nothing"
    else:
        return users[0]
    
def get_same_age_users_by_age(age):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT ID FROM USER WHERE AGE = {age} ORDER BY RAND();"
    cursor.execute(SQL_QUERY)
    users = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if not users:
        return "nothing"
    else:
        return users[0]
    
def get_same_province_only_females_or_males_users_by_province(province, preferred_gender):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT ID FROM USER WHERE PROVINCE = '{province}' AND GENDER = '{preferred_gender}';"
    cursor.execute(SQL_QUERY)
    users = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if not users:
        return "nothing"
    else:
        return users[0]

def get_same_province_by_province(province):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT ID FROM USER WHERE PROVINCE = '{province}' ORDER BY RAND();"
    cursor.execute(SQL_QUERY)
    users = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if not users:
        return "nothing"
    else:
        return users[0]

def get_random_user_cid():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = "SELECT ID FROM USER ORDER BY RAND() LIMIT 1;"
    cursor.execute(SQL_QUERY)
    user = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return user[0][0]

def get_latitude_longitude_by_cid(cid):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = f"SELECT LATITUDE, LONGITUDE FROM USER WHERE ID = {cid};"
    cursor.execute(SQL_QUERY)
    user_geographic_cordinates = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return user_geographic_cordinates[0]

def get_latitude_longitude_of_every_user():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    SQL_QUERY = "SELECT ID, LATITUDE, LONGITUDE FROM USER;"
    cursor.execute(SQL_QUERY)
    every_user_geographic_cordinates = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if not every_user_geographic_cordinates:
        return "nothing"
    else:
        return every_user_geographic_cordinates


if __name__ == "__main__":
    get_cid()
    get_user_info_by_cid()
    send_location()
    get_cid_by_private_link()
    invite_link_gen()
    private_link_gen()
    get_name_by_cid()
    get_invite_links()
    get_private_links()
    get_cid_by_invite_link()
    get_coin_numbers_by_cid()
    get_coins_credit_by_id()
    get_coins_price_by_id()
    search_user()
    organize_the_text()
    organize_the_text_for_contacts_section()
    get_cid_by_personal_id()
    get_private_link_by_personal_id()
    get_name_by_personal_id()
    get_contacts_by_cid()
    get_blocked_users_by_cid()
    get_province_by_cid()
    get_age_by_cid()
    get_same_age_only_male_users_by_age()
    get_same_age_only_female_users_by_age()
    get_same_age_users_by_age()
    get_same_province_only_females_or_males_users_by_province()
    get_same_province_by_province()
    get_random_user_cid()
    get_latitude_longitude_by_cid()
    get_latitude_longitude_of_every_user()