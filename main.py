import telebot
import datetime as dt
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os



TOKEN = "7785542509:AAH7DXqt7ow6O0qaiUMn3xCWEbZHAfdV4_0"

bot = telebot.TeleBot(TOKEN)

bot = telebot.TeleBot(TOKEN)
user_states = {}

# تعریف یک دستور: /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # ایجاد موضوع کیبورد اینلاین
    markup = InlineKeyboardMarkup()
    
    # افزودن دکمه‌ها
    markup.row_width = 2  # تعداد دکمه در هر ردیف
    markup.add(
        InlineKeyboardButton("les", callback_data="option1"),
        InlineKeyboardButton("femboy", callback_data="option2")
    )
    markup.add(InlineKeyboardButton("وب‌سایت ما", url="https://pornhub.com"))
    bot.send_message(message.chat.id, "سلام! یکی از گزینه‌های زیر رو انتخاب کن:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "option1":
        bot.send_message(call.message.chat.id, "✅ سایت مخصوص گزینه 1:\nhttps://https://www.erome.com/search?q=lesbian+.com")
        
    elif call.data == "option2":
        bot.send_message(call.message.chat.id, "✅ سایت مخصوص گزینه 2:\nhttps://www.erome.com/search?q=cute+femboy.com")



# تعریف یک دستور: /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, """سلام دابش میتونی از من برای اوقات فراغت(جق) استفاده کنی
                 البته یه سری کار دیگم میکنم مثل:
                 /echo : پیام هر چی بدی به خودت برمیگردونم
                 /time :ساعت بهت میگم
                 /help : همین کصشرارو بهت میگم باز
                 /location : لوکیشن یه چیزی که دوس داری بکنی تو کونت رو بهت میدم
                 /photo : یه عکس قشنگ برات میفرستم
                 /voice : برات ویس قشنگ میفرسم گل 
                 """ )
    
@bot.message_handler(commands=['time'])
def return_time(message):
    now = dt.datetime.now()
    bot.reply_to(message, f"الان ساعته: {now.strftime('%H:%M:%S')}")

@bot.message_handler(commands=['echo'])
def echo_command(message):
    user_states[message.chat.id] = "awaiting_echo"  # تنظیم وضعیت کاربر
    bot.reply_to(message, "پیامت رو بفرست تا برات تکرار کنم!")

@bot.message_handler(commands=['location'])
def send_location(message):
    lat = 35.7448
    lon = 51.3753
    bot.send_location(message.chat.id, lat, lon)

@bot.message_handler(commands=['photo'])
def send_photo(message):
    current_dir = os.path.dirname(os.path.abspath(__file__))  # مسیر فایل فعلی
    photo_path = os.path.join(current_dir, 'images.jpg')  # مسیر عکس کنار main.py
    try:
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="بیا بخورش بیا")
    except FileNotFoundError:
        bot.reply_to(message,"عکس یافت نشد")

# @bot.message_handler(commands=['voice'])
# def send_voice(message):
#     markup = InlineKeyboardMarkup()
    
#     # افزودن دکمه‌ها
#     markup.row_width = 2  # تعداد دکمه در هر ردیف
#     markup.add(
#         InlineKeyboardButton("دلنواز", callback_data="option1"),
#         InlineKeyboardButton("گوشنواز", callback_data="option2"),
#         InlineKeyboardButton("گوشنواز", callback_data="option3")
#     )

#     bot.send_message(message.chat.id, "سلام حمال عزیز یکی از گزینه‌های زیر رو انتخاب کن:", reply_markup=markup)
# @bot.callback_query_handler(func=lambda call: True)
# def callback_handler(call):
#       file_1 = 
@bot.message_handler(content_types=['voice'])
def get_voice_file_id(message):
    file_id = message.voice.file_id
    print("Voice file_id:", file_id)  # اینجا تو کنسول چاپ میشه
    bot.reply_to(message, "ویس دریافت شد و file_id آن ذخیره شد.")
   
    
    
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if user_states.get(message.chat.id) == "awaiting_echo":
        bot.reply_to(message, message.text)
        user_states.pop(message.chat.id)  # بعد از دریافت پیام، وضعیت رو پاک کن
    else:
        bot.reply_to(message, f"شما گفتید: {message.text}")

# شروع به کار بات
print("بات در حال اجراست...")
bot.polling(none_stop=True)
