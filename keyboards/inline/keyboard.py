from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_btn(): 
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="Отправить сообщение", callback_data="SendMessage")
    ).add(
        InlineKeyboardButton(text="Отправить сообщение(Forward)", callback_data="SendMessageForward")
    ).add(
        InlineKeyboardButton(text="Добавить группу", callback_data="addGroup"),
        InlineKeyboardButton(text="Удалить группу", callback_data="delGroup")
    )

def GroupList_btn(arr):
    btn = InlineKeyboardMarkup(row_width=2)
    a = []
    i = 1
    for x in arr:
        a.append(InlineKeyboardButton(i+"- Group", callback_data='chat_id='+ x[1]))
        i +=1
    return btn.add(*a)
 