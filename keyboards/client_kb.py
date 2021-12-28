from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # ,ReplyKeyboardRemove

b1 = KeyboardButton("Youtube")
b2 = KeyboardButton("Instagram")
b3 = KeyboardButton("TikTok")
b4 = KeyboardButton("Twitter")
b8=KeyboardButton("Spotify")
b5 = KeyboardButton("Поделиться номером", request_contact=True)
b6 = KeyboardButton("Отправить где я", request_location=True)
b7=KeyboardButton("Отмена")
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b1).insert(b2)
kb_client.add(b3).insert(b4)
kb_client.add(b8)

kb_youtube=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
q01=KeyboardButton("Видео")
q02=KeyboardButton("Аудио")
q03=KeyboardButton("Плэй-лист")
kb_youtube.add(q01)
kb_youtube.add(q02)

kb_cancer=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_cancer.row('Отмена')

kb_main_menu=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_main_menu.row('Вернуться на главное меню')
# kb_client.row(b1)
