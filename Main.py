import telebot
import datetime
import os
import string
import random
import math
from Project_DML import *
from Project_DQL import *
from config import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, Location
from Project_texts import text as keyboardbutton

API_TOKEN = bot_token

bot = telebot.TeleBot(API_TOKEN)
admin_cid = admin_cid
user_step = dict()
user_data = dict()
selected_provinces = dict()
advance_search_age_range = dict()
intended_cid = list()
intended_name = list()
target_cid = list()
sendable_message = list()
counter = dict()
cart = dict()
active_chats = dict()
waiting_users = list()
personal_id_container = list()
blocked_users_to_unblock = dict()
delete_contact = list()
hide_markup = ReplyKeyboardRemove()
channel_id = channel_id
message_ids = {
    "start"                                             :   2,
    "connect_to_stranger"                               :   3,
    "nearby_users"                                      :   4,
    "search_users"                                      :   5,
    "guide"                                             :   6,
    "profile"                                           :   7,
    "coin"                                              :   8,
    "invite_link"                                       :   9,
    "unknown_link"                                      :   10,
    "guide_text"                                        :   11,
    "home_commands"                                     :   12,
    "enter_name"                                        :   13,
    "select_gender"                                     :   14,
    "enter_age"                                         :   15,
    "send_photo"                                        :   16,
    "select_province"                                   :   17,
    "send_location"                                     :   18,
    "successful_sign_up"                                :   19,
    "name"                                              :   20,
    "gender"                                            :   21,
    "province"                                          :   22,
    "age"                                               :   23,
    "blocked_users"                                     :   25,
    "contacts"                                          :   26,
    "edit_profile"                                      :   27,
    "send_new_name"                                     :   28,
    "false_new_name"                                    :   29,
    "your_name_changed"                                 :   30,
    "your_gender_changed"                               :   31,
    "your_age_changed"                                  :   32,
    "your_province_changed"                             :   33,
    "your_profile_pic_changed"                          :   34,
    "your_location_changed"                             :   35,
    "send_new_profile_pic"                              :   36,
    "false_new_gender"                                  :   37,
    "false_new_age"                                     :   38,
    "false_new_province"                                :   39,
    "false_new_img"                                     :   40,
    "false_new_location"                                :   41,
    "false_numeric_name"                                :   42,
    "correct_sign"                                      :   43,
    "false_name"                                        :   44,
    "invalid_long_name"                                 :   45,
    "false_gender"                                      :   46,
    "false_age"                                         :   47,
    "str_age"                                           :   48,
    "false_img"                                         :   49,
    "false_province"                                    :   50,
    "false_location"                                    :   51,
    "search_text"                                       :   52,
    "same_age_show_who"                                 :   53,
    "same_province_show_who"                            :   54,
    "advance_search_select_province"                    :   55,
    "advance_search_select_age"                         :   56,
    "message_successfully_sent"                         :   61,
    "unread_message"                                    :   62,
    "successful_add_coin"                               :   63,
    "send_screen_shot"                                  :   66,
    "false_payment"                                     :   67,
    "cancel_purchase"                                   :   68,
    "successful_cancellation"                           :   69,
    "sent_payment_photo_successfuly"                    :   70,
    "successful_purchase"                               :   71,
    "purchase_failed"                                   :   72,
    "unassigned_link"                                   :   73,
    "successful_add_contact"                            :   74,
    "successful_add_blocked"                            :   75,
    "cant_send_message_user_blocked"                    :   76,
    "user_unblocked"                                    :   77,
    "delete_contact"                                    :   78,
    "connected_users"                                   :   79,
    "disconnect"                                        :   80,
    "other_disconnect"                                  :   81,
    "successful_purchase_for_another_user"              :   82,
    "nearby_users_search"                               :   83,
    "sign_up_first"                                     :   84,
    "not_enough_coins"                                  :   85,



    }
connect_command = ["/connect_to_a_stranger", "به یک ناشناس وصلم کن!"]
search_command = ["/search_users", "❕جستجوی کاربران❕"]
nearby_command = ["/nearby_users", "📍افراد نزدیک"]
coins_command = ["/coins", "💰سکه"]
profile_command = ["/profile", "👤پروفایل"]
help_command = ["/help", "🤔راهنما"]
invite_command = ["/invite_link", "🚸معرفی به دوستان(سکه رایگان)"]
unknownchat_command = ["/private_chat_link", "📱لینگ ناشناس من"]
photo_and_text_only = ["photo", "text"]
location_and_text_only = ["location", "text"]


commands = {
    "Start"                         :   keyboardbutton["b28"],
    "profile"                       :   keyboardbutton["b29"],
    "connect_to_a_stranger"         :   keyboardbutton["b30"],
    "search_users"                  :   keyboardbutton["b31"],
    "nearby_users"                  :   keyboardbutton["b32"],
    "coins"                         :   keyboardbutton["b33"],
    "invite_link"                   :   keyboardbutton["b34"],
    "private_chat_link"             :   keyboardbutton["b35"],
}

provinces = {
    "b1": "البرز",
    "b2": "آذربایجان شرقی",
    "b3": "آذربایجان غربی",
    "b4": "بوشهر",
    "b5": "چهارمحال و بختیاری",
    "b6": "فارس",
    "b7": "گیلان",
    "b8": "گلستان",
    "b9": "همدان",
    "b10": "هرمزگان",
    "b11": "ایلام",
    "b12": "اصفهان",
    "b13": "کرمان",
    "b14": "کرمانشاه",
    "b15": "خراسان رضوی",
    "b16": "خراسان جنوبی",
    "b17": "خراسان شمالی",
    "b18": "خوزستان",
    "b19": "کهگیلویه و بویراحمد",
    "b20": "کردستان",
    "b21": "لرستان",
    "b22": "مرکزی",
    "b23": "مازندران",
    "b24": "قزوین",
    "b25": "قم",
    "b26": "سمنان",
    "b27": "سیستان و بلوچستان",
    "b28": "تهران",
    "b29": "یزد",
    "b30": "زنجان",
}

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot = telebot.TeleBot(API_TOKEN)
bot.set_update_listener(listener)

def advanced_search_inlinekeyboard_gen(cid, mid, intrested_city):
    province_data = list()
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(InlineKeyboardButton(keyboardbutton["b26"], callback_data="everyone"))
    for i in provinces:
        text = provinces[i]
        if provinces[i] in intrested_city[cid]:
            text += "✔"
        province_data.append(InlineKeyboardButton(text, callback_data=provinces[i]))
    markup.add(*province_data)
    markup.add(InlineKeyboardButton(keyboardbutton["b27"], callback_data="next"))
    bot.edit_message_reply_markup(cid, mid, reply_markup=markup)

def delete_markup(cid, mid, items):
    data = list()
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(InlineKeyboardButton(keyboardbutton["b26"], callback_data="everyone"))
    for i in provinces:
            if provinces[i] in items[cid]:
                data.append(InlineKeyboardButton(provinces[i], callback_data=provinces[i]))
                selected_provinces[cid].remove(provinces[i])
            else:
                data.append(InlineKeyboardButton(provinces[i], callback_data=provinces[i]))
    markup.add(*data)
    markup.add(InlineKeyboardButton(keyboardbutton["b27"], callback_data="next"))
    bot.edit_message_reply_markup(cid, mid, reply_markup=markup)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c 

def age_range(cid, mid, age_range):
    data = list()
    markup = InlineKeyboardMarkup(row_width=5)
    for i in range(10, 101, 10):
        text = str(i)
        if str(i) in age_range[cid]:
            text += "✔"
        data.append(InlineKeyboardButton(text, callback_data=str(i)))
    markup.add(*data)
    markup.add(InlineKeyboardButton(keyboardbutton["b27"], callback_data="finish_search"))
    bot.edit_message_reply_markup(cid, mid, reply_markup=markup)
    


# start command
# دستور شروع ربات
@bot.message_handler(commands=['start'])
def command_start_handler(message):
    cid = message.chat.id
    invite_links = get_invite_links()
    private_links = get_private_links()
    IL_result = list()
    PL_result = list()
    for i in invite_links:
        IL_result.append(i[0])
    for j in private_links:
        PL_result.append(j[0])
    if message.text.split()[-1] in PL_result:
        private_link_hash_value = message.text.split()[-1]
        receiver_cid = get_cid_by_private_link(private_link_hash_value)[0][0]
        receiver_name = get_name_by_cid(receiver_cid)[0][0]
        text = f"{keyboardbutton["b39"]} {receiver_name} {keyboardbutton["b40"]}\n{keyboardbutton["b41"]}"
        markup1 = ReplyKeyboardMarkup(resize_keyboard=True)
        markup1.add(keyboardbutton["b42"])
        bot.send_message(cid, text, reply_markup=markup1)
        intended_cid.append(receiver_cid)
        intended_name.append(receiver_name)
        user_step[cid] = "send_message_to_receiver_cid"
    elif message.text.split()[-1] in IL_result and str(cid):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(keyboardbutton["b1"]))
        markup.add(KeyboardButton(keyboardbutton["b2"]), KeyboardButton(keyboardbutton["b3"]))
        markup.add(KeyboardButton(keyboardbutton["b4"]), KeyboardButton(keyboardbutton["b5"]), KeyboardButton(keyboardbutton["b6"]))
        markup.add(KeyboardButton(keyboardbutton["b7"]))
        markup.add(KeyboardButton(keyboardbutton["b8"]))
        cid_link_to_add_coin = message.text.split()[-1]
        cid_to_add_coin = get_cid_by_invite_link(cid_link_to_add_coin)
        add_coin_to_cid(cid_to_add_coin)
        bot.copy_message(cid, channel_id, message_ids["start"])
        bot.copy_message(cid, channel_id, message_ids["home_commands"], reply_markup=markup)
        bot.copy_message(cid_to_add_coin, channel_id, message_ids["successful_add_coin"])
    elif message.text == "/start":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(keyboardbutton["b1"]))
        markup.add(KeyboardButton(keyboardbutton["b2"]), KeyboardButton(keyboardbutton["b3"]))
        markup.add(KeyboardButton(keyboardbutton["b4"]), KeyboardButton(keyboardbutton["b5"]), KeyboardButton(keyboardbutton["b6"]))
        markup.add(KeyboardButton(keyboardbutton["b7"]))
        markup.add(KeyboardButton(keyboardbutton["b8"]))
        bot.copy_message(cid, channel_id, message_ids["start"])
        bot.copy_message(cid, channel_id, message_ids["home_commands"], reply_markup=markup)

@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "send_message_to_receiver_cid")
def step_smrc_handler(message):
    cid = message.chat.id
    receiver_cid = intended_cid[-1]
    if message.text == keyboardbutton["b42"]:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(keyboardbutton["b1"]))
        markup.add(KeyboardButton(keyboardbutton["b2"]), KeyboardButton(keyboardbutton["b3"]))
        markup.add(KeyboardButton(keyboardbutton["b4"]), KeyboardButton(keyboardbutton["b5"]), KeyboardButton(keyboardbutton["b6"]))
        markup.add(KeyboardButton(keyboardbutton["b7"]))
        markup.add(KeyboardButton(keyboardbutton["b8"]))
        bot.copy_message(cid, channel_id, message_ids["home_commands"], reply_markup=markup)
        user_step[cid] = 0
        receiver_cid = ""
    else:
        sendable_message.append(message.text)
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(keyboardbutton["b1"]))
        markup.add(KeyboardButton(keyboardbutton["b2"]), KeyboardButton(keyboardbutton["b3"]))
        markup.add(KeyboardButton(keyboardbutton["b4"]), KeyboardButton(keyboardbutton["b5"]), KeyboardButton(keyboardbutton["b6"]))
        markup.add(KeyboardButton(keyboardbutton["b7"]))
        markup.add(KeyboardButton(keyboardbutton["b8"]))
        markup1 = InlineKeyboardMarkup()
        markup1.add(InlineKeyboardButton(keyboardbutton["b43"], callback_data="open"))
        bot.copy_message(cid, channel_id, message_ids["message_successfully_sent"])
        bot.copy_message(cid, channel_id, message_ids["home_commands"], reply_markup=markup)
        bot.copy_message(receiver_cid, channel_id, message_ids["unread_message"], reply_markup=markup1)
        user_step[cid] = 0
        receiver_cid = ""


# home command
# دستور خانه
@bot.message_handler(commands=["home"])
def command_home_handler(message):
    cid = message.chat.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(keyboardbutton["b1"]))
    markup.add(KeyboardButton(keyboardbutton["b2"]), KeyboardButton(keyboardbutton["b3"]))
    markup.add(KeyboardButton(keyboardbutton["b4"]), KeyboardButton(keyboardbutton["b5"]), KeyboardButton(keyboardbutton["b6"]))
    markup.add(KeyboardButton(keyboardbutton["b7"]))
    markup.add(KeyboardButton(keyboardbutton["b8"]))
    bot.copy_message(cid, channel_id, message_ids["home_commands"], reply_markup=markup)

# help command
# دستور کمک
@bot.message_handler(func= lambda message: message.text in help_command)
def command_help_handler(message):
    text = ""
    cid = message.chat.id
    for command, desc in commands.items():
        text += f"/{command}: {desc}\n"
    bot.copy_message(cid, channel_id, message_ids["guide_text"])
    bot.send_message(cid, text)
    bot.copy_message(cid, channel_id, text)

# show profile/sign up command
# دستور ساخت اکانت کاربری یا نمایش اطلاعات کاربر
@bot.message_handler(func= lambda message: message.text in profile_command)
def command_profile_hanfler(message):
    cid = message.chat.id
    signed_up_cids = get_cid()
    if str(cid) in str(signed_up_cids):
        user_info = get_user_info_by_cid(cid)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b9"], callback_data="send_location"))
        markup.add(InlineKeyboardButton(keyboardbutton["b11"], callback_data="show_contacts"), InlineKeyboardButton(keyboardbutton["b10"], callback_data="show_blocked"))
        markup.add(InlineKeyboardButton(keyboardbutton["b12"], callback_data="show_edit_menu"))
        if user_info[4] == "Male":
            text = f"نام: {user_info[1]}\nجنسیت: مرد\nاستان: {user_info[6]}\nسن: {user_info[3]}\nلینک حساب کاربری شما:{user_info[2]}"
            file_id = user_info[5]
            bot.send_photo(cid, file_id, caption=text, reply_markup=markup)
        if user_info[4] == "Female":
            text = f"نام: {user_info[1]}\nجنسیت: زن\nاستان: {user_info[6]}\nسن: {user_info[3]}\nلینک حساب کاربری شما:{user_info[2]}"
            file_id = user_info[5]
            bot.send_photo(cid, file_id, caption=text, reply_markup=markup)
    else:
        # get username
        # نام کاربری را میگیرد
        bot.copy_message(cid, channel_id, message_ids["enter_name"])
        user_step[cid] = "username_checker"

# check if the name is valid or not and in the else get gender.
# چک میکند نام وارد شده صحیح است یا خیر و در اخر جنسیت کاربر را میگیرد.
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "username_checker")
def username_checker_handler(message):
    cid = message.chat.id
    username = message.text
    if username[0].isdigit():
        bot.copy_message(cid, channel_id, message_ids["false_numeric_name"])
    elif len(username) > 21:
        bot.copy_message(cid, channel_id, message_ids["invalid_long_name"])
    else:
        bot.copy_message(cid, channel_id, message_ids["correct_sign"])
        user_data.setdefault(cid, {})
        user_data[cid].setdefault("cid", cid)
        user_data[cid].setdefault("username", username)
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(keyboardbutton["b13"]),
                    KeyboardButton(keyboardbutton["b14"]))
        bot.copy_message(cid, channel_id, message_ids["select_gender"], reply_markup=markup)
        user_step[cid] = "gender_checker"

# check if the gender is valid or not and in the end else get age.
# چک میکند ایا جنسیت وارد شده صحیح است یا خیر و در اخر سن کاربر را میگیرد.
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "gender_checker")
def step_A_handler(message):
    cid = message.chat.id
    gender = message.text
    print(type(gender))
    print(keyboardbutton["b14"], type(keyboardbutton["b14"]))
    if gender == keyboardbutton["b13"] or gender == keyboardbutton["b14"]:
        bot.copy_message(cid, channel_id, message_ids["correct_sign"])
        if gender == "پسر👨":
            user_data[cid].setdefault("gender", "Male")
        elif gender == "دختر👩":
            user_data[cid].setdefault("gender", "Female")
    else:
        bot.copy_message(cid, channel_id, message_ids["false_gender"])
    bot.copy_message(cid, channel_id, message_ids["enter_age"], reply_markup=hide_markup)
    user_step[cid] = "age_checker"

# check if the age is valid or not and in the else get progile picture.
# چک میکند ایا سن وارد شده صحیح است یا خیر و  در اخر تصویر نمایه کاربر را میگیرد.
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "age_checker")
def step_C_handler(message):
    cid = message.chat.id
    age = message.text
    if 10 > int(age) or int(age) > 100:
        bot.copy_message(cid, channel_id, message_ids["false_age"])
    elif not age.isdigit():
        bot.copy_message(cid, channel_id, message_ids["str_age"])
    else:
        bot.copy_message(cid, channel_id, message_ids["correct_sign"])
        user_data[cid].setdefault("age", age)
        bot.copy_message(cid, channel_id, message_ids["send_photo"])
        user_step[cid] = "profile_checker"

# check if the profile pic is valid or not and in the else get province.
# چک میکند ایا تصویر نمایه صحیح است یا خیر و در اخر استان کاربر را میگیرد.
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "profile_checker", content_types=photo_and_text_only)
def step_D_handler(message):
    cid = message.chat.id
    if message.content_type == "photo":
        buttons = list()
        bot.copy_message(cid, channel_id, message_ids["correct_sign"])
        file_id = message.photo[-1].file_id
        user_data[cid].setdefault("file_id", file_id)
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        os.makedirs(os.path.join("photos", str(cid)), exist_ok=True)
        image_name = datetime.datetime.now().strftime("%y-%m-%d %H-%M-%S_%f")
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        content = bot.download_file(file_info.file_path)
        with open(os.path.join("photos", str(cid), image_name), "wb") as f:
            f.write(content)
        for i in provinces.values():
            buttons.append(i)
        markup.add(*buttons)
        bot.copy_message(cid, channel_id, message_ids["select_province"], reply_markup=markup)
        user_step[cid] = "province_checker"
    else:
        bot.copy_message(cid, channel_id, message_ids["false_img"])



# check if the province is valid or not and in the else get location.
# چک میکند ایا استان وارد شده صحیح است یا خیر و در اخر موقعیت مکانی کاربر را میگیرد.
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "province_checker",)
def step_E_handler(message):
    cid = message.chat.id
    province = message.text
    if province not in provinces.values():
        bot.copy_message(cid, channel_id, message_ids["false_province"])
    else:
        bot.copy_message(cid, channel_id, message_ids["correct_sign"], reply_markup=hide_markup)
        user_data[cid].setdefault("province", province)
        markup = ReplyKeyboardMarkup(resize_keyboard=True)  
        location_button = KeyboardButton(keyboardbutton["b9"], request_location=True)
        markup.add(location_button)
        bot.copy_message(cid, channel_id, message_ids["send_location"], reply_markup=markup)
        user_step[cid] = "location_checker"
        
# check if the location is valid or not and in the else send the successfull sign up message.
# چک میکند ایا موقعیت مکانی صحیح است یا خیر و در اخر پیام ثبت نام موفقیت امیز را میفرستد.
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "location_checker", content_types=location_and_text_only)
def step_F_handler(message):
    cid = message.chat.id
    if not message.content_type == "location":
        bot.copy_message(cid, channel_id, message_ids["false_location"])
    else:
        bot.copy_message(cid, channel_id, message_ids["successful_sign_up"], reply_markup=hide_markup)
        latitude = message.location.latitude
        longitude = message.location.longitude
        user_data[cid].setdefault("location", {})
        user_data[cid]["location"].setdefault("latitude", latitude)
        user_data[cid]["location"].setdefault("longitude", longitude)
        hash_value = hash(cid)
        invite_link_hash_value = hash_value*350+2583
        unknown_chat_link_hash_value = hash_value*550+2383
        chars_and_numbers = string.ascii_letters + "12345678910"
        result = "/user_" + ''.join(random.choice(chars_and_numbers) for _ in range(8))
        print(result)
        user_data[cid].setdefault("invite_&_unknown_chat_link", {})
        user_data[cid]["invite_&_unknown_chat_link"].setdefault("invite_link", invite_link_hash_value)
        user_data[cid]["invite_&_unknown_chat_link"].setdefault("unknown_chat_link", unknown_chat_link_hash_value)
        user_data[cid].setdefault("personal_link", result)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b9"], callback_data="send_location"))
        markup.add(InlineKeyboardButton(keyboardbutton["b11"], callback_data="show_contacts"), InlineKeyboardButton(keyboardbutton["b10"], callback_data="show_blocked"))
        markup.add(InlineKeyboardButton(keyboardbutton["b12"], callback_data="show_edit_menu"))
        text = f"نام:{user_data[cid]["username"]}\nجنسیت:{user_data[cid]["gender"]}\nاستان:{user_data[cid]["province"]}\nسن:{user_data[cid]["age"]}\nلینک کاربری شما:{user_data[cid]["personal_link"]}"
        file_id = user_data[cid]["file_id"]
        print(user_data)
        insert_info(user_data[cid]["cid"], user_data[cid]["username"], user_data[cid]["personal_link"], user_data[cid]["age"], user_data[cid]["gender"], user_data[cid]["file_id"], user_data[cid]["province"], user_data[cid]["location"]["latitude"], user_data[cid]["location"]["longitude"], 5, user_data[cid]["invite_&_unknown_chat_link"]["invite_link"], user_data[cid]["invite_&_unknown_chat_link"]["unknown_chat_link"])
        bot.send_photo(cid, file_id, caption=text, reply_markup=markup)
        user_step[cid] = 0

@bot.message_handler(func= lambda message: message.text in search_command)
def search_users_handler(message):
    cid = message.chat.id
    signed_up_cids = get_cid()
    if not str(cid) in str(signed_up_cids):
        bot.copy_message(cid, channel_id, message_ids["sign_up_first"])
    else:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b21"], callback_data="same_age"), InlineKeyboardButton(keyboardbutton["b22"], callback_data="same_province"))
        markup.add(InlineKeyboardButton(keyboardbutton["b23"], callback_data="advance_search"))
        bot.copy_message(cid, channel_id, message_ids["search_text"], reply_markup=markup)

@bot.message_handler(func= lambda message: message.text in nearby_command)
def nearby_user_finder_handler(message):
    cid = message.chat.id
    signed_up_cids = get_cid()
    if not str(cid) in str(signed_up_cids):
        bot.copy_message(cid, channel_id, message_ids["sign_up_first"])
    else:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b79"], callback_data=keyboardbutton["b79"]), InlineKeyboardButton(keyboardbutton["b80"], callback_data=keyboardbutton["b80"]))
        markup.add(InlineKeyboardButton(keyboardbutton["b81"], callback_data=keyboardbutton["b81"]), InlineKeyboardButton(keyboardbutton["b82"], callback_data=keyboardbutton["b82"]))
        bot.copy_message(cid, channel_id, message_ids["nearby_users_search"], reply_markup=markup)
 
# invite link command.
# دستور لینک دعوت.
@bot.message_handler(func= lambda message: message.text in invite_command)
def invite_command_handler(message):
    cid = message.chat.id
    signed_up_cids = get_cid()
    if not str(cid) in str(signed_up_cids):
        bot.copy_message(cid, channel_id, message_ids["sign_up_first"])
    else:
        bot.send_message(cid, invite_link_gen(cid))

# unknown link command.
# دستور لینک چت ناشناس.
@bot.message_handler(func= lambda message: message.text in unknownchat_command)
def unknownchat_link_handler(message):
    cid = message.chat.id
    signed_up_cids = get_cid()
    if not str(cid) in str(signed_up_cids):
        bot.copy_message(cid, channel_id, message_ids["sign_up_first"])
    else:
        bot.send_message(cid, private_link_gen(cid))

# coins store command.
# دستور بخش خرید سکه.
@bot.message_handler(func= lambda message: message.text in coins_command)
def coins_command_handler(message):
    cid = message.chat.id
    signed_up_cids = get_cid()
    if not str(cid) in str(signed_up_cids):
        bot.copy_message(cid, channel_id, message_ids["sign_up_first"])
    else:
        number_of_coins = get_coin_numbers_by_cid(cid)
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton(keyboardbutton["b47"], callback_data="first_item"))
        markup.add(InlineKeyboardButton(keyboardbutton["b48"], callback_data="second_item"))
        markup.add(InlineKeyboardButton(keyboardbutton["b49"], callback_data="third_item"))
        markup.add(InlineKeyboardButton(keyboardbutton["b50"], callback_data="fourth_item"))
        markup.add(InlineKeyboardButton(keyboardbutton["b58"], callback_data="cancel_purchase"))
        text = f"{keyboardbutton["b45"]} {str(number_of_coins)}\n{keyboardbutton["b46"]}"
        bot.send_message(cid, text, reply_markup=markup)
        cart.setdefault(cid, list())
        target_cid.append(cid)

@bot.message_handler(func= lambda message: message.text in connect_command)
def connect_to_random_handler(message):
    cid = message.chat.id
    signed_up_cids = get_cid()
    if not str(cid) in str(signed_up_cids):
        bot.copy_message(cid, channel_id, message_ids["sign_up_first"])
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(keyboardbutton["b73"]))
        waiting_users.append(cid)
        print(waiting_users)
        while True:
            partner_cid = int(get_random_user_cid())
            if partner_cid not in active_chats and partner_cid in waiting_users and partner_cid != cid:
                break
        active_chats[cid] = partner_cid
        active_chats[partner_cid] = cid
        bot.copy_message(cid, channel_id, message_ids["connected_users"], reply_markup=markup)
        bot.copy_message(partner_cid, channel_id, message_ids["connected_users"], reply_markup=markup)
        

@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "payment_confirmation", content_types=photo_and_text_only)
def payment_confrimation_handler(message):
    cid = message.chat.id
    if message.content_type == "photo":
        cid_personal_id = get_cid_by_personal_id(cid)
        file_id = message.photo[-1].file_id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b56"], callback_data="purchase_confirmed"), InlineKeyboardButton(keyboardbutton["b57"], callback_data="purchase_rejected"))
        bot.send_photo(admin_cid, file_id, caption=f"{keyboardbutton["b59"]}{cart[cid][0]}\n{keyboardbutton["b60"]}{cart[cid][1]}\n{keyboardbutton["b61"]}{cart[cid][2]}", reply_markup=markup)
        bot.copy_message(cid, channel_id, message_ids["sent_payment_photo_successfuly"])
        user_step[cid] = 0
    elif message.content_type == "text":
        bot.copy_message(cid, channel_id, message_ids["false_payment"])
        bot.copy_message(cid, channel_id, message_ids["cancel_purchase"])

@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "payment_confirmation_for_another_user", content_types=photo_and_text_only)
def payment_confrimation_for_another_user_handler(message):
    cid = message.chat.id
    if message.content_type == "photo":
        cid_personal_id = get_personal_id_by_cid(cid)
        target_personal_cid = cart[cid][3]
        file_id = message.photo[-1].file_id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b56"], callback_data="purchase_confirmed_for_another_user"), InlineKeyboardButton(keyboardbutton["b57"], callback_data="purchase_rejected_for_another_user"))
        bot.send_photo(admin_cid, file_id, caption=f"{keyboardbutton["b59"]}{cart[cid][0]}\n{keyboardbutton["b60"]}{cart[cid][1]}\n{keyboardbutton["b61"]}{cart[cid][2]}\n\nbuyer: {cid_personal_id}\nreciver: {target_personal_cid}", reply_markup=markup)
        bot.copy_message(cid, channel_id, message_ids["sent_payment_photo_successfuly"])
        user_step[cid] = 0
        del cart[cid]
    elif message.content_type == "text":
        bot.copy_message(cid, channel_id, message_ids["false_payment"])
        bot.copy_message(cid, channel_id, message_ids["cancel_purchase"])

# edit username
# ویرایش نام کاربری
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "edit_name")
def new_name_handler(message):
    cid = message.chat.id
    new_name = message.text
    if not new_name.isdigit(): 
        edit_name(cid, new_name)
        bot.copy_message(cid, channel_id, message_ids["your_name_changed"])
        user_step[cid] = 0
    elif new_name[0].isdigit():
        bot.copy_message(cid, channel_id, message_ids["false_new_name"])
    elif len(new_name) > 21:
        bot.copy_message(cid, channel_id, message_ids["invalid_long_name"])

# edit users gender
# ویرایش جنسیت
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "edit_gender")
def new_gender_handler(message):
    cid = message.chat.id
    new_gender = message.text
    if new_gender == keyboardbutton["b13"]:
        edit_gender(cid, "MALE")
    elif new_gender == keyboardbutton["b14"]:
            edit_gender(cid, "FEMALE")
    elif not new_gender == keyboardbutton["b13"] or not new_gender == keyboardbutton["b14"]:
          bot.copy_message(cid, channel_id, message_ids["false_new_gender"])
    bot.copy_message(cid, channel_id, message_ids["your_gender_changed"], reply_markup=hide_markup)
    user_step[cid] = 0

# edit users age
# ویرایش سن
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "edit_age")
def new_age_handler(message):
    cid = message.chat.id
    new_age = message.text
    if not new_age.isdigit():
          bot.copy_message(cid, channel_id, message_ids["false_new_age"])
    elif 10 > int(new_age) > 100:
        bot.copy_message(cid, channel_id, message_ids["false_new_age"])
    else:
        edit_age(cid, new_age)
        bot.copy_message(cid, channel_id, message_ids["your_age_changed"])
        user_step[cid] = 0

# edit users province
# ویرایش استان
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "edit_province")
def new_province_handler(message):
    cid = message.chat.id
    new_province = message.text
    print(new_province)
    if  new_province not in provinces.values():
        bot.copy_message(cid, channel_id, message_ids["false_new_province"])
    else:
        edit_province(cid, new_province)
        bot.copy_message(cid, channel_id, message_ids["your_province_changed"], reply_markup=hide_markup)
        user_step[cid] = 0

# edit users profile pic
# ویرایش تصویر نمایه
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "edit_picture", content_types=["photo"])
def new_picture_handler(message):
    cid = message.chat.id
    if message.content_type != "photo":
          bot.copy_message(cid, channel_id, message_ids["false_new_img"])
    elif message.content_type == "photo":
        new_file_id = message.photo[-1].file_id
        edit_profile_pic(cid, new_file_id)
        os.makedirs(os.path.join("photos", str(cid)), exist_ok=True)
        image_name = datetime.datetime.now().strftime("%y-%m-%d %H-%M-%S_%f")
        file_info = bot.get_file(new_file_id)
        content = bot.download_file(file_info.file_path)
        with open(os.path.join("photos", str(cid), image_name), "wb") as f:
            f.write(content)
        bot.copy_message(cid, channel_id, message_ids["your_profile_pic_changed"])
        user_step[cid] = 0

# edit location
# ویرایش موقعیت مکانی
@bot.message_handler(func= lambda message: user_step.get(message.chat.id) == "edit_location", content_types=["location"])
def new_location_handler(message):
    cid = message.chat.id
    if message.content_type != "location":
        bot.copy_message(cid, channel_id, message_ids["false_new_location"])
    elif message.content_type == "location":
        new_latitude = message.location.latitude
        new_longitude = message.location.longitude
        edit_latitude(cid, new_latitude)
        edit_longitude(cid, new_longitude)
        bot.copy_message(cid, channel_id, message_ids["your_location_changed"], reply_markup=hide_markup)
        user_step[cid] = 0

# shows profile of the user when his/her personal id was sent. 
# اطلاعات حساب کاربری کاربری که ایدی شخصیش ارسال شده بود رو نمایش میده.
@bot.message_handler(func= lambda message: message.text.startswith("/user_"))
def personal_id_handler(message):
    cid = message.chat.id
    user_personal_id = message.text
    user_cid = get_cid_by_personal_id(user_personal_id)
    blocked_users_by_cid = get_blocked_users_by_cid(cid)
    contacts = get_contacts_by_cid(cid)
    personal_id_container.append(user_personal_id)
    if user_cid == "this link does not belong to any user of this bot.":
        bot.copy_message(cid, channel_id, message_ids["unassigned_link"])
    elif int(user_cid) == cid:
        user_info = get_user_info_by_cid(cid)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b9"], callback_data="send_location"))
        markup.add(InlineKeyboardButton(keyboardbutton["b11"], callback_data="show_contacts"), InlineKeyboardButton(keyboardbutton["b10"], callback_data="show_blocked"))
        markup.add(InlineKeyboardButton(keyboardbutton["b12"], callback_data="show_edit_menu"))
        if user_info[4] == "Male":
            text = f"نام: {user_info[1]}\nجنسیت: مرد\nاستان: {user_info[6]}\nسن: {user_info[3]}\nلینک حساب کاربری شما:{user_info[2]}"
            file_id = user_info[5]
            bot.send_photo(cid, file_id, caption=text, reply_markup=markup)
        if user_info[4] == "Female":
            text = f"نام: {user_info[1]}\nجنسیت: زن\nاستان: {user_info[6]}\nسن: {user_info[3]}\nلینک حساب کاربری شما:{user_info[2]}"
            file_id = user_info[5]
            bot.send_photo(cid, file_id, caption=text, reply_markup=markup)
    else:
        existing_cid = get_user_info_by_cid(user_cid)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b64"], callback_data=keyboardbutton["b64"]))
        markup.add(InlineKeyboardButton(keyboardbutton["b66"], callback_data=keyboardbutton["b66"]), InlineKeyboardButton(keyboardbutton["b65"], callback_data=keyboardbutton["b65"]))
        if user_cid in blocked_users_by_cid and user_cid in contacts:
            markup.add(InlineKeyboardButton(keyboardbutton["b69"], callback_data=keyboardbutton["b69"]), InlineKeyboardButton(keyboardbutton["b70"], callback_data=keyboardbutton["b70"]))
        else:
            if user_cid in blocked_users_by_cid:
                markup.add(InlineKeyboardButton(keyboardbutton["b69"], callback_data=keyboardbutton["b69"]), InlineKeyboardButton(keyboardbutton["b67"], callback_data=keyboardbutton["b67"]))
            elif user_cid in contacts:
                markup.add(InlineKeyboardButton(keyboardbutton["b68"], callback_data=keyboardbutton["b68"]), InlineKeyboardButton(keyboardbutton["b70"], callback_data=keyboardbutton["b70"]))
            else:
                markup.add(InlineKeyboardButton(keyboardbutton["b67"], callback_data=keyboardbutton["b67"]), InlineKeyboardButton(keyboardbutton["b68"], callback_data=keyboardbutton["b68"]))
        if existing_cid[4] == "Male":
            text = f"نام: {existing_cid[1]}\nجنسیت: مرد\nاستان: {existing_cid[6]}\nسن: {existing_cid[3]}\nلینک حساب کاربری :{existing_cid[2]}"
            file_id = existing_cid[5]
            bot.send_photo(cid, file_id, caption=text, reply_markup=markup)
        if existing_cid[4] == "Female":
            text = f"نام: {existing_cid[1]}\nجنسیت: زن\nاستان: {existing_cid[6]}\nسن: {existing_cid[3]}\nلینک حساب کاربری :{existing_cid[2]}"
            file_id = existing_cid[5]
            bot.send_photo(cid, file_id, caption=text, reply_markup=markup)
        
@bot.message_handler(func= lambda message: message.chat.id in active_chats)
def connect_and_send_messages(message):
    cid = message.chat.id
    partner_cid = active_chats[cid]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(keyboardbutton["b73"]))
    if message.text == keyboardbutton["b73"]:
        if message.chat.id == cid:
            bot.copy_message(cid, channel_id, message_ids["disconnect"], reply_markup=hide_markup)
            bot.copy_message(partner_cid, channel_id, message_ids["other_disconnect"], reply_markup=hide_markup)
            del active_chats[cid]
            del active_chats[partner_cid]
            if cid in waiting_users or partner_cid in waiting_users:
                waiting_users.remove(cid)
                waiting_users.remove(partner_cid)
        elif message.chat.id == partner_cid:
            bot.copy_message(partner_cid, channel_id, message_ids["disconnect"])
            bot.copy_message(cid, channel_id, message_ids["other_disconnect"])
    elif message.chat.id == cid:
        bot.send_message(partner_cid, message.text, reply_markup=markup)
    elif message.chat.id == partner_cid:
        bot.send_message(cid, message.text, reply_markup=markup)


@bot.callback_query_handler(func= lambda call: True)
def callback_query_handler(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data
    call_id = call.id
    if data == "send_location":
        latitude, longitude = send_location(cid)
        bot.send_location(cid, latitude=latitude, longitude=longitude)
    elif data == "show_contacts":
        contacts = get_contacts_by_cid(cid)
        result = organize_the_text_for_contacts_section(contacts)
        bot.send_message(cid, result)
    elif data == "show_blocked":
        blocked_users = get_blocked_users_by_cid(cid)
        if blocked_users == "nothing":
            bot.send_message(cid, keyboardbutton["b63"])
        else:
            result = organize_the_text_for_contacts_section(blocked_users)
            bot.send_message(cid, result)
    elif data == "show_edit_menu":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b15"], callback_data="edit_name"), InlineKeyboardButton(keyboardbutton["b16"], callback_data="edit_gender"))
        markup.add(InlineKeyboardButton(keyboardbutton["b17"], callback_data="edit_age"), InlineKeyboardButton(keyboardbutton["b18"], callback_data="edit_province"))
        markup.add(InlineKeyboardButton(keyboardbutton["b19"], callback_data="edit_profile_pic"), InlineKeyboardButton(keyboardbutton["b20"], callback_data="edit_location"))
        bot.edit_message_reply_markup(cid, mid, reply_markup=markup)
    # edit information inline keyboard buttons
    # دکمه های شیشه ای ویرایش اطلاعات
    elif data == "edit_name":
        bot.copy_message(cid, channel_id, message_ids["send_new_name"])
        user_step[cid] = "edit_name"
    elif data == "edit_gender":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(keyboardbutton["b13"]), KeyboardButton(keyboardbutton["b14"]))
        bot.copy_message(cid, channel_id, message_ids["select_gender"], reply_markup=markup)
        user_step[cid] = "edit_gender"
    elif data == "edit_age":
        bot.copy_message(cid, channel_id, message_ids["enter_age"])
        user_step[cid] = "edit_age"
    elif data == "edit_province":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        data = list()
        for province in provinces.values(): 
            data.append(KeyboardButton(province))
        markup.add(*data)
        bot.copy_message(cid, channel_id, message_ids["select_province"], reply_markup=markup)
        user_step[cid] = "edit_province"
    elif data == "edit_profile_pic":
        bot.copy_message(cid, channel_id, message_ids["send_new_profile_pic"])
        user_step[cid] = "edit_picture"
    elif data == "edit_location":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)  
        markup.add(KeyboardButton(keyboardbutton["b9"], request_location=True))
        bot.copy_message(cid, channel_id, message_ids["send_location"], reply_markup=markup)
        user_step[cid] = "edit_location"
    elif data == "same_age":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b24"], callback_data="same_age_&_only_males"), InlineKeyboardButton(keyboardbutton["b25"], callback_data="same_age_&_only_females"))
        markup.add(InlineKeyboardButton(keyboardbutton["b26"], callback_data="same_age_&_everyone"))
        bot.copy_message(cid, channel_id, message_ids["same_age_show_who"], reply_markup=markup)
    elif data == "same_province":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b24"], callback_data="same_province_&_only_males"), InlineKeyboardButton(keyboardbutton["b25"], callback_data="same_province_&_only_females"))
        markup.add(InlineKeyboardButton(keyboardbutton["b26"], callback_data="same_province_&_everyone"))
        bot.copy_message(cid, channel_id, message_ids["same_province_show_who"], reply_markup=markup)
    elif data == "open":
        bot.send_message(intended_cid[0], sendable_message)
    elif data == "advance_search":
        if selected_provinces:
            selected_provinces[cid] = list()
        if counter:
            counter[cid] = list()   
        province_data = list()
        markup = InlineKeyboardMarkup(row_width=3)
        markup.add(InlineKeyboardButton(keyboardbutton["b26"], callback_data="everyone"))
        for i in provinces:
            province_data.append(InlineKeyboardButton(provinces[i], callback_data=provinces[i]))
        markup.add(*province_data)
        markup.add(InlineKeyboardButton(keyboardbutton["b27"], callback_data="next"))
        bot.copy_message(cid, channel_id, message_ids["advance_search_select_province"], reply_markup=markup)
        selected_provinces.setdefault(cid, list()) 
    elif data == provinces["b1"]:
        if provinces["b1"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b1"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b2"]:
        if provinces["b2"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b2"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b3"]:
        if provinces["b3"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b3"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b4"]:
        if provinces["b4"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b4"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b5"]:
        if provinces["b5"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b5"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b6"]:
        if provinces["b6"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b6"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b7"]:
        if provinces["b7"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b7"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b8"]:
        if provinces["b8"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b8"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b9"]:
        if provinces["b9"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b9"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b10"]:
        if provinces["b10"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b10"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b11"]:
        if provinces["b11"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b11"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b12"]:
        if provinces["b12"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b12"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b13"]:
        if provinces["b13"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b13"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b14"]:
        if provinces["b14"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b14"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b15"]:
        if provinces["b15"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b15"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b16"]:
        if provinces["b16"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b16"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b17"]:
        if provinces["b17"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b17"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b18"]:
        if provinces["b18"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b18"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b19"]:
        if provinces["b19"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b19"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b20"]:
        if provinces["b20"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b20"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b21"]:
        if provinces["b21"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b21"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b22"]:
        if provinces["b22"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b22"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b23"]:
        if provinces["b23"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b23"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b24"]:
        if provinces["b24"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b24"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b25"]:
        if provinces["b25"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b25"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b26"]:
        if provinces["b26"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b26"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b27"]:
        if provinces["b27"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b27"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b28"]:
        if provinces["b28"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b28"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b29"]:
        if provinces["b29"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b29"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == provinces["b30"]:
        if provinces["b30"] not in selected_provinces[cid]:
            selected_provinces[cid].append(provinces["b30"])
            advanced_search_inlinekeyboard_gen(cid, mid, selected_provinces)
        else:
            delete_markup(cid, mid, selected_provinces)
    elif data == "everyone":
        for i in provinces:
            selected_provinces[cid].append(provinces[i])
        markup = InlineKeyboardMarkup(row_width=5)
        advance_search_age_range.setdefault(cid, list())
        buttons = []
        for i in range(10, 101, 10):
            buttons.append(InlineKeyboardButton(str(i), callback_data=str(i)))
        markup.add(*buttons)
        markup.add(InlineKeyboardButton(keyboardbutton["b27"], callback_data="finish_search"))
        bot.copy_message(cid, channel_id, message_ids["advance_search_select_age"], reply_markup=markup)
        counter.setdefault(cid, list())
    elif data == "next":
        if not selected_provinces[cid]:
            bot.answer_callback_query(call_id, keyboardbutton["b44"])
        else:
            markup = InlineKeyboardMarkup(row_width=5)
            advance_search_age_range.setdefault(cid, list())
            buttons = []
            for i in range(10, 101, 10):
                buttons.append(InlineKeyboardButton(str(i), callback_data=str(i)))
            markup.add(*buttons)
            markup.add(InlineKeyboardButton(keyboardbutton["b27"], callback_data="finish_search"))
            bot.copy_message(cid, channel_id, message_ids["advance_search_select_age"], reply_markup=markup)
            counter.setdefault(cid, list())
    elif data == "10":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("10")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(10)
        elif len(counter) >= 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "20":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("20")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(20)
        elif len(counter) == 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "30":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("30")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(30)
        elif len(counter[cid]) == 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "40":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("40")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(40)
        elif len(counter[cid]) == 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "50":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("50")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(50)
        elif len(counter[cid]) == 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "60":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("60")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(60)
        elif len(counter[cid]) == 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "70":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("70")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(70)
        elif len(counter[cid]) == 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "80":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("80")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(80)
        elif len(counter[cid]) == 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "90":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("90")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(90)
        elif len(counter[cid]) == 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "100":
        if len(counter[cid]) != 2:
            advance_search_age_range[cid].append("100")
            age_range(cid, mid, advance_search_age_range)
            counter[cid].append(100)
        elif len(counter[cid]) == 2:
            bot.answer_callback_query(call_id, keyboardbutton["b62"])
    elif data == "finish_search":
        text = search_user(selected_provinces[cid], counter[cid])
        users = organize_the_text(text)
        selected_provinces[cid].clear()
        counter[cid].clear()
        print(selected_provinces)
        print(counter[cid])
        bot.send_message(cid, users, reply_markup=hide_markup)
    elif data == "first_item":
        credit = get_coins_credit_by_id(1)
        price = get_coins_price_by_id(1)
        text = f"{keyboardbutton["b51"]}{credit}{keyboardbutton["b52"]}{price}{keyboardbutton["b53"]}\n{keyboardbutton["b54"]}"
        bot.send_message(cid, text)
        bot.copy_message(cid, channel_id, message_ids["send_screen_shot"])
        cart[cid].append(1)
        cart[cid].append(credit)
        cart[cid].append(price)
    elif data == "purchase_for_some-one_else_first_item":
        cart.setdefault(cid, list())
        for i in call.message.caption.split():
            if i.startswith("/user"):
                target_personal_id = i
        credit = get_coins_credit_by_id(1)
        price = get_coins_price_by_id(1)
        text = f"{keyboardbutton["b51"]}{credit}{keyboardbutton["b52"]}{price}{keyboardbutton["b53"]}\n{keyboardbutton["b54"]}"
        bot.send_message(cid, text)
        bot.copy_message(cid, channel_id, message_ids["send_screen_shot"])
        cart[cid].append(1)
        cart[cid].append(credit)
        cart[cid].append(price)
        cart[cid].append(target_personal_id)
        user_step[cid] = "payment_confirmation_for_another_user"
    elif data == "purchase_for_some-one_else_second_item":
        cart.setdefault(cid, list())
        for i in call.message.caption.split():
            if i.startswith("/user"):
                target_personal_id = i
        credit = get_coins_credit_by_id(2)
        price = get_coins_price_by_id(2)
        text = f"{keyboardbutton["b51"]}{credit}{keyboardbutton["b52"]}{price}{keyboardbutton["b53"]}\n{keyboardbutton["b54"]}"
        bot.send_message(cid, text)
        bot.copy_message(cid, channel_id, message_ids["send_screen_shot"])
        cart[cid].append(2)
        cart[cid].append(credit)
        cart[cid].append(price)
        cart[cid].append(target_personal_id)
        user_step[cid] = "payment_confirmation_for_another_user"
    elif data == "purchase_for_some-one_else_third_item":
        cart.setdefault(cid, list())
        for i in call.message.caption.split():
            if i.startswith("/user"):
                target_personal_id = i
        credit = get_coins_credit_by_id(3)
        price = get_coins_price_by_id(3)
        text = f"{keyboardbutton["b51"]}{credit}{keyboardbutton["b52"]}{price}{keyboardbutton["b53"]}\n{keyboardbutton["b54"]}"
        bot.send_message(cid, text)
        bot.copy_message(cid, channel_id, message_ids["send_screen_shot"])
        cart[cid].append(3)
        cart[cid].append(credit)
        cart[cid].append(price)
        cart[cid].append(target_personal_id)
        user_step[cid] = "payment_confirmation_for_another_user"
    elif data == "purchase_for_some-one_else_fourth_item":
        cart.setdefault(cid, list())
        for i in call.message.caption.split():
            if i.startswith("/user"):
                target_personal_id = i
        credit = get_coins_credit_by_id(4)
        price = get_coins_price_by_id(4)
        text = f"{keyboardbutton["b51"]}{credit}{keyboardbutton["b52"]}{price}{keyboardbutton["b53"]}\n{keyboardbutton["b54"]}"
        bot.send_message(cid, text)
        bot.copy_message(cid, channel_id, message_ids["send_screen_shot"])
        cart[cid].append(4)
        cart[cid].append(credit)
        cart[cid].append(price)
        cart[cid].append(target_personal_id)
        user_step[cid] = "payment_confirmation_for_another_user"
    elif data == "second_item":
        credit = get_coins_credit_by_id(2)
        price = get_coins_price_by_id(2)
        text = f"{keyboardbutton["b51"]}{credit}{keyboardbutton["b52"]}{price}{keyboardbutton["b53"]}\n{keyboardbutton["b54"]}"
        bot.send_message(cid, text)
        bot.copy_message(cid, channel_id, message_ids["send_screen_shot"])
        cart[cid].append(2)
        cart[cid].append(credit)
        cart[cid].append(price)
        user_step[cid] = "payment_confirmation"
    elif data == "third_item":
        credit = get_coins_credit_by_id(3)
        price = get_coins_price_by_id(3)
        text = f"{keyboardbutton["b51"]}{credit}{keyboardbutton["b52"]}{price}{keyboardbutton["b53"]}\n{keyboardbutton["b54"]}"
        bot.send_message(cid, text)
        bot.copy_message(cid, channel_id, message_ids["send_screen_shot"])
        cart[cid].append(3)
        cart[cid].append(credit)
        cart[cid].append(price)
        user_step[cid] = "payment_confirmation"
    elif data == "fourth_item":
        credit = get_coins_credit_by_id(4)
        price = get_coins_price_by_id(4)
        text = f"{keyboardbutton["b51"]}{credit}{keyboardbutton["b52"]}{price}{keyboardbutton["b53"]}\n{keyboardbutton["b54"]}"
        bot.send_message(cid, text)
        bot.copy_message(cid, channel_id, message_ids["send_screen_shot"])
        cart[cid].append(4)
        cart[cid].append(credit)
        cart[cid].append(price)
        user_step[cid] = "payment_confirmation"
    elif data == "purchase_confirmed":
        credit = cart[target_cid][1]
        add_purchased_coin(target_cid, credit)
        cart[target_cid].pop(0, 1, 2)
        bot.copy_message(target_cid, channel_id, message_ids["successful_purchase"])
    elif data == "purchase_rejected":
        cart[cid].pop(0, 1, 2)
        bot.copy_message(cid, channel_id, message_ids["purchase_failed"])
    elif data == "cancel_purchase":
        bot.copy_message(cid, channel_id, message_ids["successful_cancellation"])
        user_step[cid] = 0
        cart[cid].pop(0, 1, 2)
    elif data == keyboardbutton["b64"]:
        for i in call.message.caption.split():
            if i.startswith(":/user"):
                target_personal_id = i[1:]
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(keyboardbutton["b47"], callback_data="purchase_for_some-one_else_first_item"))
        markup.add(InlineKeyboardButton(keyboardbutton["b48"], callback_data="purchase_for_some-one_else_second_item"))
        markup.add(InlineKeyboardButton(keyboardbutton["b49"], callback_data="purchase_for_some-one_else_third_item"))
        markup.add(InlineKeyboardButton(keyboardbutton["b50"], callback_data="purchase_for_some-one_else_fourth_item"))
        text = f"{keyboardbutton["b74"]}{target_personal_id}{keyboardbutton["b75"]}"
        bot.edit_message_caption(text, cid, mid, reply_markup=markup)
    elif data == keyboardbutton["b65"]:
        number_of_coins = get_coin_numbers_by_cid(cid)
        if number_of_coins < 2:
            bot.copy_message(cid, channel_id, message_ids["not_enough_coins"])
        else:
            for i in call.message.caption.split():
                if i.startswith(":/user"):
                    target_personal_id = i[1:]
            user_id = get_cid_by_personal_id(target_personal_id)
            print(user_id)
            blocked_users_by_cid = get_blocked_users_by_cid(user_id)
            cid_personal_link = get_personal_id_by_cid(cid)
            text = f"{keyboardbutton["b71"]}{cid_personal_link}{keyboardbutton["b72"]}"
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(keyboardbutton["b56"], callback_data="chat_confrimed"), InlineKeyboardButton(keyboardbutton["b57"], callback_data="chat_rejected"))
            if str(cid) in blocked_users_by_cid:
                bot.copy_message(cid, channel_id, message_ids["cant_send_message_user_blocked"])
            else:
                bot.send_message(user_id, text, reply_markup=markup)
    elif data == keyboardbutton["b66"]:
        user_personal_id = personal_id_container[-1]
        user_id = get_cid_by_personal_id(user_personal_id)
        blocked_users_by_cid = get_blocked_users_by_cid(user_id)
        if str(cid) in blocked_users_by_cid:
            bot.copy_message(cid, channel_id, message_ids["cant_send_message_user_blocked"])
        else:
            intended_cid.append(user_id)
            user_name = get_name_by_personal_id(user_personal_id)
            text = f"{keyboardbutton["b39"]} {user_name} {keyboardbutton["b40"]}\n{keyboardbutton["b41"]}"
            bot.send_message(cid, text)
            user_step[cid] = "send_message_to_receiver_cid"
    elif data == keyboardbutton["b67"]:
        user_personal_id = personal_id_container[-1]
        user_name = get_name_by_personal_id(user_personal_id)
        user_id = get_cid_by_personal_id(user_personal_id)
        insert_into_contacts(user_id, user_name, user_personal_id)
        insert_cid_to_contacts(cid, user_id, user_name, user_personal_id)
        bot.copy_message(cid, channel_id, message_ids["successful_add_contact"])
    elif data == keyboardbutton["b68"]:
        user_personal_id = personal_id_container[-1]
        user_name = get_name_by_personal_id(user_personal_id)
        user_id = get_cid_by_personal_id(user_personal_id)
        insert_into_blocked_users(user_id, user_name, user_personal_id)
        insert_cid_to_blocked_users(cid, user_id, user_name, user_personal_id)
        bot.copy_message(cid, channel_id, message_ids["successful_add_blocked"])
        personal_id_container.pop(-1)
    elif data == keyboardbutton["b69"]:
        for i in call.message.caption.split():
            if i.startswith(":/user"):
                target_personal_id = i[1:]
        user_id = get_cid_by_personal_id(target_personal_id)
        unblock_user_by_cid1(user_id)
        unblock_user_by_cid(user_id)
        bot.copy_message(cid, channel_id, message_ids["user_unblocked"])
        blocked_users_to_unblock.clear()
    elif data == keyboardbutton["b70"]:
        for i in call.message.caption.split():
            if i.startswith(":/user"):
                target_personal_id = i[1:]
        user_id = get_cid_by_personal_id(target_personal_id)
        delete_contact_by_cid1(user_id)
        delete_contact_by_cid(user_id)
        bot.copy_message(cid, channel_id, message_ids["delete_contact"])
    elif data == "same_age_&_only_males":
        age = get_age_by_cid(cid)
        result = get_same_age_only_male_users_by_age(age, "Male")
        text = organize_the_text(result)
        bot.send_message(cid, text)
    elif data == "same_age_&_only_females":
        age = get_age_by_cid(cid)
        result = get_same_age_only_female_users_by_age(age, "Female")
        text = organize_the_text(result)
        bot.send_message(cid, text)
    elif data == "same_age_&_everyone":
        age = get_age_by_cid(cid)
        result = get_same_age_users_by_age(age)
        text = organize_the_text(result)
        bot.send_message(cid, text)
    elif data == "same_province_&_only_males":
        province = get_province_by_cid(cid)
        result = get_same_province_only_females_or_males_users_by_province(province, "Male")
        text = organize_the_text(result)
        bot.send_message(cid, text)
    elif data == "same_province_&_only_females":
        province = get_province_by_cid(cid)
        result = get_same_province_only_females_or_males_users_by_province(province, "Female")
        text = organize_the_text(result)
        bot.send_message(cid, text)
    elif data == "same_province_&_everyone":
        province = get_province_by_cid(cid)
        result = get_same_province_by_province(province)
        text = organize_the_text(result)
        bot.send_message(cid, text)
    elif data == "chat_confrimed":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(keyboardbutton["b73"]))
        for i in call.message.text.split():
            if i.startswith("/user"):
                target_personal_id = i
        user_id = get_cid_by_personal_id(target_personal_id)
        active_chats[cid] = int(user_id)
        active_chats[int(user_id)] = cid
        bot.delete_message(cid, mid, 2)
        bot.copy_message(cid, channel_id, message_ids["connected_users"], reply_markup=markup)
        bot.copy_message(user_id, channel_id, message_ids["connected_users"], reply_markup=markup)
        decrease_coins_for_chat(user_id)
    elif data == "chat_rejected":
        pass
    elif data == "purchase_confirmed_for_another_user":
        result = list()
        for i in call.message.caption.split():
            if i.startswith("/user"):
                result.append(i)
            elif i.isdigit() and len(i) == 1:
                product_id = i
        buyer, reciver = result
        credit = get_coins_credit_by_id(product_id)
        reciver_cid = get_cid_by_personal_id(reciver)
        buyer_cid = get_cid_by_personal_id(buyer)
        add_purchased_coin(reciver_cid, credit)
        text_for_reciver_cid = f"{keyboardbutton["b76"]}{buyer}{keyboardbutton["b77"]}{keyboardbutton["b78"]}"
        bot.send_message(reciver_cid, text_for_reciver_cid)
        bot.copy_message(buyer_cid, channel_id, message_ids["successful_purchase_for_another_user"]) 
    elif data == "purchase_rejected_for_another_user":
        result = list()
        for i in call.message.caption.split():
            if i.startswith("/user"):
                result.append(i)
            elif i.isdigit() and len(i) == 1:
                product_id = i
        buyer, reciver = result
        buyer_cid = get_cid_by_personal_id(buyer)
        bot.copy_message(buyer_cid, channel_id, message_ids["purchase_failed"])
    
    elif data == keyboardbutton["b79"]:
        nearby_users = dict()
        nearby_users.setdefault(cid, list())
        user_location = get_latitude_longitude_by_cid(cid)
        users_location = get_latitude_longitude_of_every_user()
        for other_user_id, other_lat, other_lon in users_location:
            distance = haversine(user_location[0], user_location[1], other_lat, other_lon)
            if distance <= 25:
                nearby_users[cid].append(other_user_id)
        text = organize_the_text(nearby_users[cid])
        bot.send_message(cid, text)
        del nearby_users[cid]
    elif data == keyboardbutton["b80"]:
        nearby_users = dict()
        nearby_users.setdefault(cid, list())
        user_location = get_latitude_longitude_by_cid(cid)
        users_location = get_latitude_longitude_of_every_user()
        for other_user_id, other_lat, other_lon in users_location:
            distance = haversine(user_location[0], user_location[1], other_lat, other_lon)
            if distance <= 50:
                nearby_users[cid].append(other_user_id)
        text = organize_the_text(nearby_users[cid])
        bot.send_message(cid, text)
        del nearby_users[cid]
    elif data == keyboardbutton["b81"]:
        nearby_users = dict()
        nearby_users.setdefault(cid, list())
        user_location = get_latitude_longitude_by_cid(cid)
        users_location = get_latitude_longitude_of_every_user()
        for other_user_id, other_lat, other_lon in users_location:
            distance = haversine(user_location[0], user_location[1], other_lat, other_lon)
            if distance <= 100:
                nearby_users[cid].append(other_user_id)
        text = organize_the_text(nearby_users[cid])
        bot.send_message(cid, text)
        del nearby_users[cid]
    elif data == keyboardbutton["b82"]:
        nearby_users = dict()
        nearby_users.setdefault(cid, list())
        user_location = get_latitude_longitude_by_cid(cid)
        users_location = get_latitude_longitude_of_every_user()
        for other_user_id, other_lat, other_lon in users_location:
            distance = haversine(user_location[0], user_location[1], other_lat, other_lon)
            if distance <= 150:
                nearby_users[cid].append(other_user_id)
        text = organize_the_text(nearby_users[cid])
        bot.send_message(cid, text)
        del nearby_users[cid]


bot.infinity_polling()