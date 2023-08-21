from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp, bot
from data import BOT_ID
from keyboards.inline import admin_btn, GroupList_btn
from states import permeationSetGroup, permeationSendMsg, StateSendForward
from utils.db_api import DBS
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
import asyncio

@dp.message_handler(text=["/admin", "⬅️Назад"], state="*", user_id=ADMINS)
async def bot_admin(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Добро пожаловать в панель администратора!🤗\n\n👇 Выбирайте меню", reply_markup=admin_btn())


@dp.callback_query_handler(text="addGroup")
async def addgroup_bot(call: types.CallbackQuery):
    await permeationSetGroup.next()
    await call.message.answer("Отправьте мне *id группы")

@dp.callback_query_handler(text="SendMessageForward")
async def SendMessageForward(call: types.CallbackQuery):
    await StateSendForward.getMsg.set()
    await call.message.delete()
    await call.message.answer("Напиши мне сообщение, я отправлю его всей группе.")

@dp.message_handler(content_types=types.ContentTypes.ANY, state=StateSendForward.getMsg)
async def SendForward_bot(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.reply("Отправка...")
    data = DBS.getGroups(DBS)
    if data == False: 
        await msg.answer("Группа не существует")
        return
    for x in data:
        try:
            await asyncio.sleep(.07)
            await msg.forward(x[1])
        except:
            continue
    await msg.answer("Сообщение было отправлено")

@dp.message_handler(content_types=['text'], state=permeationSetGroup.perm)
async def setGroup (message: types.Message, state: FSMContext):
    if message.text.lstrip('-').isdigit():
        try:
            data = await dp.bot.get_chat_member(message.text, BOT_ID)
            if data.is_chat_admin():
                await message.reply("Бот успешно добавлен✅")
                DBS.chat_register(DBS, message.text)
                await state.finish()
            else: await message.reply("Бот не является админом в группе\nПопробуйте еще раз")
        except:
            await message.reply("Бот не является админом в группе\nПопробуйте еще раз")
    else: await message.reply("*ID не являются числом\nПопробуйте еще раз")


@dp.callback_query_handler(text='delGroup')
async def delGroup_bot (call: types.CallbackQuery):
    data = DBS.getGroups(DBS)
    if data == False: 
        await call.message.answer("Группа не существует")
    else:
        btn = InlineKeyboardMarkup(row_width=2)
        a = []
        i = 1
        for x in data:
            try:
                chat = await dp.bot.export_chat_invite_link(x[1])
                a.append(InlineKeyboardButton(f'{i}-Group', url=chat))
                a.append(InlineKeyboardButton("❌delete", callback_data=f'chat_id={x[1]}'))
                i +=1
            except:
                continue
        await call.message.answer("👇 Выбирайте меню", reply_markup=btn.add(*a))
    
@dp.callback_query_handler(lambda call: call.data.split('=')[0] == 'chat_id')
async def delChat(call: types.CallbackQuery):
    chat_id = call.data.split('=')[1]
    DBS.delGroup(DBS, chat_id)
    data = DBS.getGroups(DBS)
    if data == False: 
        await call.message.delete()
        await call.message.answer("Группа не существует")
    else:
        btn = InlineKeyboardMarkup(row_width=2)
        a = []
        i = 1
        for x in data:
            print(x)
            try:
                chat = await dp.bot.export_chat_invite_link(x[1])
                print(chat)
                a.append(InlineKeyboardButton(f'{i}-Group', url=chat))
                a.append(InlineKeyboardButton("❌delete", callback_data=f'chat_id={x[1]}'))
                i +=1
            except:
                continue
        if len(a) == 0:
            await call.message.delete()
            await call.message.answer("Группа не существует")
            return
        await call.message.edit_reply_markup(reply_markup=btn.add(*a))



@dp.callback_query_handler(text="SendMessage")
async def SendAllMessage(call: types.CallbackQuery):
    await permeationSendMsg.next()
    await call.message.delete()
    await call.message.answer("Напиши мне сообщение, я отправлю его всей группе.")

@dp.message_handler(content_types=types.ContentTypes.ANY, state=permeationSendMsg.perm)
async def Sending_bot(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.reply("Отправка...")
    data = DBS.getGroups(DBS)
    if data == False: 
        await msg.answer("Группа не существует")
        return
    for x in data:
        try:
            await asyncio.sleep(.07)
            await msg.send_copy(x[1])
        except:
            continue
    await msg.answer("Сообщение было отправлено")