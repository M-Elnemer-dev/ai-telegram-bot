import os
import time
import logging
from collections import defaultdict
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from google import genai

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ADMIN_ID = os.getenv("ADMIN_CHAT_ID")

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

user_languages = {}
user_states = {}

user_message_times = defaultdict(list)
RATE_LIMIT_COUNT = 5
RATE_LIMIT_WINDOW = 10 

def is_rate_limited(user_id: int) -> bool:
    current_time = time.time()
    user_message_times[user_id] = [
        t for t in user_message_times[user_id] if current_time - t < RATE_LIMIT_WINDOW
    ]
    if len(user_message_times[user_id]) >= RATE_LIMIT_COUNT:
        return True
    user_message_times[user_id].append(current_time)
    return False

def get_main_keyboard(lang="en"):
    if lang == "ar":
        keyboard = [
            [InlineKeyboardButton("📊 الأسعار / الخطط", callback_data="pricing"), InlineKeyboardButton("💼 خدماتنا", callback_data="services")],
            [InlineKeyboardButton("📩 تواصل مع المطور", callback_data="contact")],
            [InlineKeyboardButton("🔄 إعادة ضبط المحادثة", callback_data="reset"), InlineKeyboardButton("ℹ️ عن النظام", callback_data="about")],
            [InlineKeyboardButton("🌐 تغيير اللغة (Change Language)", callback_data="language")]
        ]
    elif lang == "es":
        keyboard = [
            [InlineKeyboardButton("📊 Planes / Precios", callback_data="pricing"), InlineKeyboardButton("💼 Servicios", callback_data="services")],
            [InlineKeyboardButton("📩 Contactar Desarrollador", callback_data="contact")],
            [InlineKeyboardButton("🔄 Reiniciar Chat", callback_data="reset"), InlineKeyboardButton("ℹ️ Sobre el Sistema", callback_data="about")],
            [InlineKeyboardButton("🌐 Cambiar Idioma", callback_data="language")]
        ]
    else:
        keyboard = [
            [InlineKeyboardButton("📊 Pricing / Plans", callback_data="pricing"), InlineKeyboardButton("💼 Our Services", callback_data="services")],
            [InlineKeyboardButton("📩 Contact Developer", callback_data="contact")],
            [InlineKeyboardButton("🔄 Reset Chat", callback_data="reset"), InlineKeyboardButton("ℹ️ About System", callback_data="about")],
            [InlineKeyboardButton("🌐 Change Language", callback_data="language")]
        ]
    return InlineKeyboardMarkup(keyboard)

def get_language_keyboard():
    keyboard = [
        [InlineKeyboardButton("🇸🇦 العربية", callback_data="set_lang_ar"), InlineKeyboardButton("🇺🇸 English", callback_data="set_lang_en")],
        [InlineKeyboardButton("🇫🇷 Français", callback_data="set_lang_fr"), InlineKeyboardButton("🇪🇸 Español", callback_data="set_lang_es")],
        [InlineKeyboardButton("🇩🇪 Deutsch", callback_data="set_lang_de"), InlineKeyboardButton("🇨🇳 中文", callback_data="set_lang_zh")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_states[user_id] = None
    lang = user_languages.get(user_id, "en")
    
    welcome_messages = {
        "ar": "🤖 **أهلاً بك في خدمة Elnemer AI Assistant!** 🌟\n\nكيف يمكنني مساعدتك اليوم؟ اختر خياراً من القائمة أدناه أو اطرح سؤالك مباشرة!",
        "es": "🤖 **¡Bienvenido al Servicio Elnemer AI Assistant!** 🌟\n\n¿Cómo puedo ayudarte hoy? Selecciona una opción del menú o haz tu pregunta directamente.",
        "en": "🤖 **Welcome to Elnemer AI Assistant Service!** 🌟\n\nHow can I assist you today? Select an option from the menu below or directly ask any question!"
    }
    
    text = welcome_messages.get(lang, welcome_messages["en"])
    await update.message.reply_text(text, reply_markup=get_main_keyboard(lang), parse_mode="Markdown")

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data.startswith("set_lang_"):
        selected_lang = query.data.split("_")[2]
        user_languages[user_id] = selected_lang
        msg = f"✅ Language updated to: **{selected_lang.upper()}**"
        await query.message.reply_text(msg, reply_markup=get_main_keyboard(selected_lang), parse_mode="Markdown")
        return

    lang = user_languages.get(user_id, "en")
    
    if query.data == "pricing":
        msg = "📊 **الخطط والأسعار:**\n- الباقة المجانية: استعلامات محدودة.\n- الباقة الاحترافية: محادثات مفتوحة." if lang == "ar" else "📊 **Plans & Pricing:**\n- Free Tier: Basic Queries\n- Pro Tier: Unlimited Chat."
    elif query.data == "services":
        msg = "💼 **خدماتنا:**\n1. مساعد ذكاء اصطناعي\n2. تلخيص وتحليل\n3. دعم برمجيات." if lang == "ar" else "💼 **Services:** Smart AI, Summarization, Coding."
    elif query.data == "contact":
        user_states[user_id] = "awaiting_contact"
        msg = "📩 **أرسل رسالتك الآن وسأقوم بتحويلها مباشرة إلى المطور!**" if lang == "ar" else "📩 **Send your message now, and I will forward it directly to the developer!**"
        await query.message.reply_text(msg)
        return
    elif query.data == "reset":
        user_states[user_id] = None
        msg = "🔄 **تم إعادة ضبط سياق المحادثة!**" if lang == "ar" else "🔄 **Chat context reset!**"
    elif query.data == "about":
        msg = "ℹ️ **Elnemer AI Bot v2.0**"
    elif query.data == "language":
        await query.message.reply_text("🌐 **Select Language:**", reply_markup=get_language_keyboard())
        return

    await query.message.reply_text(msg, parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = user_languages.get(user_id, "en")
    
    if is_rate_limited(user_id):
        await update.message.reply_text("⚠️ Rate limit reached.")
        return

    user_text = update.message.text

    if user_states.get(user_id) == "awaiting_contact":
        user_states[user_id] = None
        if ADMIN_ID:
            try:
                await context.bot.forward_message(chat_id=int(ADMIN_ID), from_chat_id=update.effective_chat.id, message_id=update.message.message_id)
                msg = "✅ **تم إرسال رسالتك بنجاح إلى المطور!**" if lang == "ar" else "✅ **Your message has been sent to the developer!**"
            except Exception as e:
                logger.error(f"Forwarding error: {e}")
                msg = "⚠️ حدث خطأ أثناء تحويل الرسالة للمطور."
        else:
            msg = "⚠️ ADMIN_CHAT_ID is missing in Railway variables."
        await update.message.reply_text(msg, parse_mode="Markdown")
        return

    if not client:
        await update.message.reply_text("⚠️ GEMINI_API_KEY is missing in Railway variables.")
        return

    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=f"Respond in '{lang}' language to: {user_text}"
        )
        if response and response.text:
            await update.message.reply_text(response.text)
        else:
            await update.message.reply_text("⚠️ Empty response received from Gemini.")
    except Exception as e:
        logger.error(f"Gemini Error: {e}")
        await update.message.reply_text(f"⚠️ Gemini Error: {str(e)}")

def main():
    if not TELEGRAM_TOKEN:
        logger.critical("TELEGRAM_BOT_TOKEN environment variable is missing or empty!")
        return

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()
