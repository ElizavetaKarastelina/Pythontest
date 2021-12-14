from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn_go = InlineKeyboardButton('Начнем!', callback_data='go')
start_menu = InlineKeyboardMarkup().row(btn_go)

btn1_v1 = InlineKeyboardButton('[1, 2, 3]', callback_data='1')
btn2_v1 = InlineKeyboardButton('[1, 2, 2]', callback_data='1well')
btn3_v1 = InlineKeyboardButton('[1, 2, 2, 3]', callback_data='1')
btn4_v1 = InlineKeyboardButton('Ошибка', callback_data='1')
first_menu = InlineKeyboardMarkup().row(btn1_v1, btn2_v1).row(btn3_v1).row(btn4_v1)

btn1_v2 = InlineKeyboardButton('1', callback_data='2')
btn2_v2 = InlineKeyboardButton('0', callback_data='2')
btn3_v2 = InlineKeyboardButton('Ошибка', callback_data='2well')
second_menu = InlineKeyboardMarkup().row(btn1_v2, btn2_v2).row(btn3_v2)

btn1_v3 = InlineKeyboardButton('for', callback_data='3')
btn2_v3 = InlineKeyboardButton('func', callback_data='3')
btn3_v3 = InlineKeyboardButton('def', callback_data='3well')
btn4_v3 = InlineKeyboardButton('while', callback_data='3')
third_menu = InlineKeyboardMarkup().row(btn1_v3, btn2_v3).row(btn3_v3, btn4_v3)

btn1_v4 = InlineKeyboardButton('6', callback_data='4well')
btn2_v4 = InlineKeyboardButton('2', callback_data='4')
btn3_v4 = InlineKeyboardButton('5', callback_data='4')
btn4_v4 = InlineKeyboardButton('1', callback_data='4')
fourth_menu = InlineKeyboardMarkup().row(btn1_v4, btn2_v4).row(btn3_v4, btn4_v4)

btn1_v5 = InlineKeyboardButton('5,5', callback_data='5')
btn2_v5 = InlineKeyboardButton('1', callback_data='5well')
btn3_v5 = InlineKeyboardButton('2', callback_data='5')
btn4_v5 = InlineKeyboardButton('Ошибка', callback_data='5')
fifth_menu = InlineKeyboardMarkup().row(btn1_v5, btn2_v5).row(btn3_v5, btn4_v5)

btn1_v6 = InlineKeyboardButton('6', callback_data='6')
btn2_v6 = InlineKeyboardButton('7', callback_data='6')
btn3_v6 = InlineKeyboardButton('8', callback_data='6well')
btn4_v6 = InlineKeyboardButton('Ошибка', callback_data='6')
sixth_menu = InlineKeyboardMarkup().row(btn1_v6, btn2_v6).row(btn3_v6, btn4_v6)

btn1_v7 = InlineKeyboardButton('6', callback_data='7well')
btn2_v7 = InlineKeyboardButton('2a', callback_data='7')
btn3_v7 = InlineKeyboardButton('24', callback_data='7')
btn4_v7 = InlineKeyboardButton('Ошибка', callback_data='7')
seventh_menu = InlineKeyboardMarkup().row(btn1_v7, btn2_v7).row(btn3_v7, btn4_v7)

btn1_v8 = InlineKeyboardButton('Hello', callback_data='8')
btn2_v8 = InlineKeyboardButton('o', callback_data='8')
btn3_v8 = InlineKeyboardButton('olleH', callback_data='8well')
btn4_v8 = InlineKeyboardButton('Ошибка', callback_data='8')
eighth_menu = InlineKeyboardMarkup().row(btn1_v8, btn2_v8).row(btn3_v8, btn4_v8)

btn1_v9 = InlineKeyboardButton('10', callback_data='9')
btn2_v9 = InlineKeyboardButton('22222', callback_data='9well')
btn3_v9 = InlineKeyboardButton('25', callback_data='9')
btn4_v9 = InlineKeyboardButton('Ошибка', callback_data='9')
ninth_menu = InlineKeyboardMarkup().row(btn1_v9, btn2_v9).row(btn3_v9, btn4_v9)

btn1_v10 = InlineKeyboardButton('0', callback_data='-')
btn2_v10 = InlineKeyboardButton('1', callback_data='-')
btn3_v10 = InlineKeyboardButton('2', callback_data='-')
btn4_v10 = InlineKeyboardButton('3', callback_data='-well')
tenth_menu = InlineKeyboardMarkup().row(btn1_v10, btn2_v10).row(btn3_v10, btn4_v10)


admin_btn = InlineKeyboardButton('Перейти в чат', url= 'https://t.me/llizzzaa327')
admin_menu = InlineKeyboardMarkup().row(admin_btn)