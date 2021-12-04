from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # ,ReplyKeyboardRemove

b1=KeyboardButton("Youtube")
b2=KeyboardButton("Instagram")
b3=KeyboardButton("TikTok")
b4=KeyboardButton("Twitter")
b5=KeyboardButton("Поделиться номером",request_contact=True)
b6=KeyboardButton("Отправить где я",request_location=True)

kb_client=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_client.add(b1).insert(b2)
kb_client.add(b3).insert(b4)

#kb_client.row(b1)