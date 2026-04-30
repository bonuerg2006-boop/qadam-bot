#!/usr/bin/env python3
"""
Qadam.uz Telegram Bot
Ishlatish: pip install pyTelegramBotAPI
Keyin: python bot.py
"""

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# ⚠️ TOKENNI BU YERGA QO'YING (yangi token)
TOKEN = "8718438349:AAH9KzDHj7Kvq6skblT3EzkLM_c0IvmfbVc

bot = telebot.TeleBot(TOKEN)

# ============================================================
# MA'LUMOTLAR (keyinchalik database ga o'tkaziladi)
# ============================================================

USTALAR = [
    {
        "id": 1,
        "ism": "Sardor Xasanov",
        "kasb": "Elektrchi",
        "emoji": "⚡",
        "narx": "50 000 so'm/soat",
        "reyting": "⭐ 4.9 (47 ta sharh)",
        "telefon": "+998 90 123 45 67",
        "telegram": "@sardor_usta",
        "manzil": "Olot tumani",
        "xizmatlar": "Sim tortish, Shield ta'mir, Rozetka o'rnatish",
        "band": False
    },
    {
        "id": 2,
        "ism": "Jasur Toshmatov",
        "kasb": "Slessar",
        "emoji": "🔧",
        "narx": "40 000 so'm/soat",
        "reyting": "⭐ 4.7 (32 ta sharh)",
        "telefon": "+998 91 234 56 78",
        "telegram": "@jasur_usta",
        "manzil": "Olot tumani",
        "xizmatlar": "Qulf ta'mir, Metal ishlov, Eshik o'rnatish",
        "band": False
    },
    {
        "id": 3,
        "ism": "Bobur Rahimov",
        "kasb": "Santexnik",
        "emoji": "🚿",
        "narx": "45 000 so'm/soat",
        "reyting": "⭐ 4.8 (28 ta sharh)",
        "telefon": "+998 93 345 67 89",
        "telegram": "@bobur_usta",
        "manzil": "Olot tumani",
        "xizmatlar": "Quvur ta'mir, Vannaxona, Nasos o'rnatish",
        "band": False
    },
    {
        "id": 4,
        "ism": "Dilshod Karimov",
        "kasb": "Bo'yoqchi",
        "emoji": "🎨",
        "narx": "35 000 so'm/soat",
        "reyting": "⭐ 4.6 (19 ta sharh)",
        "telefon": "+998 94 456 78 90",
        "telegram": "@dilshod_usta",
        "manzil": "Olot tumani",
        "xizmatlar": "Devor bo'yash, Gipsokardton, Dekorativ bo'yoq",
        "band": False
    },
]

RESTORANLAR = [
    {
        "id": 1,
        "nomi": "Bahor Oshxonasi",
        "turi": "Milliy taom",
        "emoji": "🍖",
        "reyting": "⭐ 4.8",
        "manzil": "Olot markazi",
        "ish_vaqti": "08:00 — 22:00",
        "telefon": "+998 90 111 22 33",
        "telegram": "@bahor_osh",
        "ochiq": True,
        "menu": "Osh, Shashlik, Lag'mon, Manti, So'rpa"
    },
    {
        "id": 2,
        "nomi": "City Cafe",
        "turi": "Kafe",
        "emoji": "☕",
        "reyting": "⭐ 4.6",
        "manzil": "Olot tumani",
        "ish_vaqti": "09:00 — 23:00",
        "telefon": "+998 91 222 33 44",
        "telegram": "@citycafe_olot",
        "ochiq": True,
        "menu": "Qahva, Choy, Sandwich, Tort, Kokteyl"
    },
    {
        "id": 3,
        "nomi": "Pizza House",
        "turi": "Fast food",
        "emoji": "🍕",
        "reyting": "⭐ 4.4",
        "manzil": "Olot tumani",
        "ish_vaqti": "10:00 — 21:00",
        "telefon": "+998 93 333 44 55",
        "telegram": "@pizzahouse_olot",
        "ochiq": False,
        "menu": "Pizza, Burger, Lavash, Kartoshka fri, Ichimliklar"
    },
]

# Admin ID (o'zingizning Telegram ID ingizni qo'ying)
ADMIN_ID =1400512698   # @userinfobot dan oling

# ============================================================
# ASOSIY MENYU
# ============================================================

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("🔧 Ustalar"),
        KeyboardButton("🍽️ Restoranlar"),
        KeyboardButton("🛒 Bozor"),
        KeyboardButton("📢 E'lon berish"),
        KeyboardButton("➕ Usta bo'lish"),
        KeyboardButton("📞 Aloqa")
    )
    return markup

def usta_kategoriyalar():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("⚡ Elektrchi", callback_data="kat_Elektrchi"),
        InlineKeyboardButton("🔧 Slessar", callback_data="kat_Slessar"),
        InlineKeyboardButton("🚿 Santexnik", callback_data="kat_Santexnik"),
        InlineKeyboardButton("🎨 Bo'yoqchi", callback_data="kat_Bo'yoqchi"),
        InlineKeyboardButton("🏗️ Qurilish", callback_data="kat_Qurilish"),
        InlineKeyboardButton("🚗 Avto ta'mir", callback_data="kat_Avto"),
        InlineKeyboardButton("📋 Barchasi", callback_data="kat_barchasi"),
    )
    return markup

# ============================================================
# /start
# ============================================================

@bot.message_handler(commands=['start'])
def start(message):
    ism = message.from_user.first_name or "Foydalanuvchi"
    matn = (
        f"👋 Assalomu alaykum, *{ism}*!\n\n"
        f"🏙️ *Qadam.uz* ga xush kelibsiz!\n"
        f"Olot tumani uchun №1 platforma\n\n"
        f"Nima qilmoqchisiz?"
    )
    bot.send_message(
        message.chat.id,
        matn,
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

# ============================================================
# USTALAR
# ============================================================

@bot.message_handler(func=lambda m: m.text == "🔧 Ustalar")
def ustalar_menu(message):
    bot.send_message(
        message.chat.id,
        "🔧 *Qaysi soha ustasini qidiryapsiz?*",
        parse_mode="Markdown",
        reply_markup=usta_kategoriyalar()
    )

@bot.callback_query_handler(func=lambda c: c.data.startswith("kat_"))
def usta_kategoriya(call):
    kat = call.data.replace("kat_", "")

    if kat == "barchasi":
        filtered = USTALAR
    else:
        filtered = [u for u in USTALAR if u["kasb"] == kat]

    if not filtered:
        bot.answer_callback_query(call.id, "Bu kategoriyada hozircha usta yo'q")
        return

    bot.answer_callback_query(call.id)

    for usta in filtered:
        holat = "🔴 Band" if usta["band"] else "🟢 Bo'sh"
        matn = (
            f"{usta['emoji']} *{usta['ism']}*\n"
            f"💼 {usta['kasb']} | {holat}\n"
            f"📍 {usta['manzil']}\n"
            f"⭐ {usta['reyting']}\n"
            f"💰 {usta['narx']}\n"
            f"🛠 {usta['xizmatlar']}\n\n"
            f"📞 {usta['telefon']}\n"
            f"✈️ {usta['telegram']}"
        )
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton(
                "✈️ Telegram orqali yozish",
                url=f"https://t.me/{usta['telegram'].replace('@','')}"
            )
        )
        bot.send_message(
            call.message.chat.id,
            matn,
            parse_mode="Markdown",
            reply_markup=markup
        )

# ============================================================
# RESTORANLAR
# ============================================================

@bot.message_handler(func=lambda m: m.text == "🍽️ Restoranlar")
def restoranlar(message):
    bot.send_message(message.chat.id, "🍽️ *Olot tumani restoranlari:*", parse_mode="Markdown")

    for r in RESTORANLAR:
        holat = "🟢 Ochiq" if r["ochiq"] else "🔴 Yopiq"
        matn = (
            f"{r['emoji']} *{r['nomi']}*\n"
            f"🍴 {r['turi']} | {holat}\n"
            f"📍 {r['manzil']}\n"
            f"⭐ {r['reyting']}\n"
            f"🕐 {r['ish_vaqti']}\n"
            f"📋 *Menu:* {r['menu']}\n\n"
            f"📞 {r['telefon']}"
        )
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton(
                "✈️ Telegram menyu",
                url=f"https://t.me/{r['telegram'].replace('@','')}"
            )
        )
        bot.send_message(
            message.chat.id,
            matn,
            parse_mode="Markdown",
            reply_markup=markup
        )

# ============================================================
# E'LON BERISH
# ============================================================

user_states = {}

@bot.message_handler(func=lambda m: m.text == "📢 E'lon berish")
def elon_berish(message):
    user_states[message.chat.id] = {"step": "elon_sarlavha"}
    bot.send_message(
        message.chat.id,
        "📢 *E'lon berish*\n\nE'lon sarlavhasini yozing:\n_(Misol: Yangi telefon sotiladi)_",
        parse_mode="Markdown"
    )

# ============================================================
# USTA BO'LISH
# ============================================================

@bot.message_handler(func=lambda m: m.text == "➕ Usta bo'lish")
def usta_bolish(message):
    user_states[message.chat.id] = {"step": "usta_ism"}
    bot.send_message(
        message.chat.id,
        "➕ *Usta sifatida ro'yxatdan o'tish*\n\n"
        "Ismingizni yozing:",
        parse_mode="Markdown"
    )

# ============================================================
# ALOQA
# ============================================================

@bot.message_handler(func=lambda m: m.text == "📞 Aloqa")
def aloqa(message):
    matn = (
        "📞 *Qadam.uz bilan bog'laning*\n\n"
        "✈️ Telegram: @QadamUz\n"
        "📱 Tel: +998 XX XXX XX XX\n"
        "📍 Olot tumani, Buxoro viloyati\n\n"
        "🕐 Ish vaqti: 09:00 — 21:00"
    )
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✈️ @QadamUz", url="https://t.me/QadamUz"))
    bot.send_message(message.chat.id, matn, parse_mode="Markdown", reply_markup=markup)

# ============================================================
# XABAR QABUL QILISH (state machine)
# ============================================================

@bot.message_handler(func=lambda m: m.chat.id in user_states)
def handle_states(message):
    chat_id = message.chat.id
    state = user_states.get(chat_id, {})
    step = state.get("step")

    # --- E'LON BERISH ---
    if step == "elon_sarlavha":
        user_states[chat_id]["sarlavha"] = message.text
        user_states[chat_id]["step"] = "elon_narx"
        bot.send_message(chat_id, "💰 Narxni yozing:\n_(Misol: 500 000 so'm)_")

    elif step == "elon_narx":
        user_states[chat_id]["narx"] = message.text
        user_states[chat_id]["step"] = "elon_telefon"
        bot.send_message(chat_id, "📞 Telefon raqamingizni yozing:")

    elif step == "elon_telefon":
        user_states[chat_id]["telefon"] = message.text
        data = user_states[chat_id]
        # Adminga yuborish
        admin_matn = (
            f"📢 *Yangi e'lon!*\n\n"
            f"📌 {data['sarlavha']}\n"
            f"💰 {data['narx']}\n"
            f"📞 {data['telefon']}\n"
            f"👤 @{message.from_user.username or 'username yoq'}"
        )
        try:
            bot.send_message(ADMIN_ID, admin_matn, parse_mode="Markdown")
        except:
            pass
        bot.send_message(
            chat_id,
            "✅ *E'loningiz qabul qilindi!*\n\n"
            "Admin ko'rib chiqib, tez orada chiqaradi.",
            parse_mode="Markdown",
            reply_markup=main_menu()
        )
        del user_states[chat_id]

    # --- USTA BO'LISH ---
    elif step == "usta_ism":
        user_states[chat_id]["ism"] = message.text
        user_states[chat_id]["step"] = "usta_kasb"
        bot.send_message(chat_id, "💼 Kasbingizni yozing:\n_(Misol: Elektrchi, Slessar)_")

    elif step == "usta_kasb":
        user_states[chat_id]["kasb"] = message.text
        user_states[chat_id]["step"] = "usta_tel"
        bot.send_message(chat_id, "📞 Telefon raqamingiz:")

    elif step == "usta_tel":
        user_states[chat_id]["tel"] = message.text
        data = user_states[chat_id]
        admin_matn = (
            f"➕ *Yangi usta so'rovi!*\n\n"
            f"👤 {data['ism']}\n"
            f"💼 {data['kasb']}\n"
            f"📞 {data['tel']}\n"
            f"✈️ @{message.from_user.username or 'username yoq'}"
        )
        try:
            bot.send_message(ADMIN_ID, admin_matn, parse_mode="Markdown")
        except:
            pass
        bot.send_message(
            chat_id,
            "✅ *Arizangiz yuborildi!*\n\n"
            "Admin 24 soat ichida siz bilan bog'lanadi. 🙏",
            parse_mode="Markdown",
            reply_markup=main_menu()
        )
        del user_states[chat_id]

# ============================================================
# ISHGA TUSHIRISH
# ============================================================

print("✅ Qadam.uz bot ishga tushdi!")
print("🤖 @NewQadamUzBot")
bot.infinity_polling()
