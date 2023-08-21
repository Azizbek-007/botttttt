from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
BOT_ID = str(BOT_TOKEN).split(':')[0]
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
print(ADMINS)
IP = env.str("ip")  # Xosting ip manzili
CHAT_ID = env.str("CHAT_ID")
