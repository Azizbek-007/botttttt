from aiogram.dispatcher.filters.state import State, StatesGroup

class SateSetQuantity(StatesGroup):
    promis = State()

class SateSetLink(StatesGroup):
    road = State()
    promis = State()
    interval = State()

class SateSetInterview(StatesGroup):
    road = State()
    promis = State()
    interval = State()
class SateSetRandomPost(StatesGroup):
    road = State()
    promis = State()
    interval = State()

class StateSendForward(StatesGroup):
    getMsg = State()

class SateSetOprogram(StatesGroup):
    road = State()
    promis = State()
    interval = State()

class permeationSetGroup(StatesGroup):
    perm = State()

class permeationSendMsg(StatesGroup):
    perm = State()
