import os
import time
import logging
from collections import defaultdict
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from g4f.client import Client

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("TELEGRAM_TOKEN")
ADMIN_ID = os.getenv("ADMIN_CHAT_ID")

g4f_client = Client()

user_languages = {}
user_states = {}
# ذاكرة المحادثة لكل مستخدم (تخزن أخر 10 رسائل لعدم استهلاك الذاكرة)
user_histories = defaultdict(list)

user_message_times = defaultdict(list)
RATE_LIMIT_COUNT = 5
RATE_LIMIT_WINDOW = 10

# قاموس الترجمات الشامل لكل اللغات المدعومة
TRANSLATIONS = {
    "ar": {
        "welcome": "🤖 **أهلاً بك في خدمة Elnemer AI Assistant!** 🌟\n\nكيف يمكنني مساعدتك اليوم؟ اختر خياراً من القائمة أدناه أو اطرح سؤالك مباشرة!",
        "pricing": "📊 الأسعار / الخطط",
        "pricing_text": "📊 **الخطط والأسعار:**\n- الباقة المجانية: استعلامات محدودة.\n- الباقة الاحترافية: محادثات مفتوحة.",
        "services": "💼 خدماتنا",
        "services_text": "💼 **خدماتنا:**\n1. مساعد ذكاء اصطناعي\n2. تلخيص وتحليل\n3. دعم برمجيات.",
        "contact": "📩 تواصل مع المطور",
        "contact_text": "📩 **أرسل رسالتك الآن وسأقوم بتحويلها مباشرة إلى المطور!**",
        "contact_success": "✅ **تم إرسال رسالتك بنجاح إلى المطور!**",
        "reset": "🔄 إعادة ضبط المحادثة",
        "reset_text": "🔄 **تم مسح ذاكرة المحادثة وإعادة الضبط بنجاح!**",
        "about": "ℹ️ عن النظام",
        "about_text": "ℹ️ **Elnemer AI Bot v2.0**",
        "language": "🌐 تغيير اللغة",
        "select_lang": "🌐 **اختر اللغة / Select Language:**"
    },
    "en": {
        "welcome": "🤖 **Welcome to Elnemer AI Assistant Service!** 🌟\n\nHow can I assist you today? Select an option from the menu below or directly ask any question!",
        "pricing": "📊 Pricing / Plans",
        "pricing_text": "📊 **Plans & Pricing:**\n- Free Tier: Basic Queries\n- Pro Tier: Unlimited Chat.",
        "services": "💼 Our Services",
        "services_text": "💼 **Services:** Smart AI, Summarization, Coding.",
        "contact": "📩 Contact Developer",
        "contact_text": "📩 **Send your message now, and I will forward it directly to the developer!**",
        "contact_success": "✅ **Your message has been sent to the developer!**",
        "reset": "🔄 Reset Chat",
        "reset_text": "🔄 **Chat memory cleared and reset successfully!**",
        "about": "ℹ️ About System",
        "about_text": "ℹ️ **Elnemer AI Bot v2.0**",
        "language": "🌐 Change Language",
        "select_lang": "🌐 **Select Language:**"
    },
    "es": {
        "welcome": "🤖 **¡Bienvenido al Servicio Elnemer AI Assistant!** 🌟\n\n¿Cómo puedo ayudarte hoy? Selecciona una opción del menú o haz tu pregunta directamente.",
        "pricing": "📊 Planes / Precios",
        "pricing_text": "📊 **Planes y Precios:**\n- Plan Gratuito: Consultas Básicas\n- Plan Pro: Chat Ilimitado.",
        "services": "💼 Servicios",
        "services_text": "💼 **Servicios:** IA Inteligente, Resúmenes, Programación.",
        "contact": "📩 Contactar Desarrollador",
        "contact_text": "📩 **¡Envía tu mensaje ahora y se lo forwardearé directamente al desarrollador!**",
        "contact_success": "✅ **¡Tu mensaje ha sido enviado al desarrollador!**",
        "reset": "🔄 Reiniciar Chat",
        "reset_text": "🔄 **¡Memoria del chat borrada y reiniciada con éxito!**",
        "about": "ℹ️ Sobre el Sistema",
        "about_text": "ℹ️ **Elnemer AI Bot v2.0**",
        "language": "🌐 Cambiar Idioma",
        "select_lang": "🌐 **Selecciona el Idioma:**"
    },
    "fr": {
        "welcome": "🤖 **Bienvenue sur le service Elnemer AI Assistant !** 🌟\n\nComment puis-je vous aider aujourd'hui ? Sélectionnez une option dans le menu ci-dessous ou posez votre question directement !",
        "pricing": "📊 Forfaits / Tarifs",
        "pricing_text": "📊 **Tarifs :**\n- Version Gratuite : Requêtes de base\n- Version Pro : Chat illimité.",
        "services": "💼 Services",
        "services_text": "💼 **Services :** IA intelligente, Résumé, Programmation.",
        "contact": "📩 Contacter le développeur",
        "contact_text": "📩 **Envoyez votre message maintenant, je le transmettrai au développeur !**",
        "contact_success": "✅ **Votre message a été envoyé au développeur !**",
        "reset": "🔄 Réinitialiser le chat",
        "reset_text": "🔄 **Mémoire du chat effacée et réinitialisée avec succès !**",
        "about": "ℹ️ À propos du système",
        "about_text": "ℹ️ **Elnemer AI Bot v2.0**",
        "language": "🌐 Changer de langue",
        "select_lang": "🌐 **Sélectionnez la langue :**"
    },
    "de": {
        "welcome": "🤖 **Willkommen beim Elnemer AI Assistant Dienst!** 🌟\n\nWie kann ich dir heute helfen? Wähle eine Option aus dem Menü unten oder stelle deine Frage direkt!",
        "pricing": "📊 Pläne / Preise",
        "pricing_text": "📊 **Pläne & Preise:**\n- Kostenlose Stufe: Grundlegende Abfragen\n- Pro-Stufe: Unbegrenzter Chat.",
        "services": "💼 Dienste",
        "services_text": "💼 **Dienste:** Intelligente KI, Zusammenfassung, Programmierung.",
        "contact": "📩 Entwickler kontaktieren",
        "contact_text": "📩 **Sende jetzt deine Nachricht, ich leite sie direkt an den Entwickler weiter!**",
        "contact_success": "✅ **Deine Nachricht wurde an den Entwickler gesendet!**",
        "reset": "🔄 Chat zurücksetzen",
        "reset_text": "🔄 **Chat-Speicher erfolgreich gelöscht und zurückgesetzt!**",
        "about": "ℹ️ Über das System",
        "about_text": "ℹ️ **Elnemer AI Bot v2.0**",
        "language": "🌐 Sprache ändern",
        "select_lang": "🌐 **Sprache auswählen:**"
    },
    "zh": {
        "welcome": "🤖 **欢迎使用 Elnemer AI 助手服务！** 🌟\n\n今天我能为您做些什么？请从下方菜单中选择一个选项或直接提问！",
        "pricing": "📊 套餐 / 价格",
        "pricing_text": "📊 **套餐与定价：**\n- 免费层：基础查询\n- 专业层：无限聊天。",
        "services": "💼 服务",
        "services_text": "💼 **服务：** 智能AI、摘要生成、编程。",
        "contact": "📩 联系开发者",
        "contact_text": "📩 **立即发送您的消息，我将直接转发给开发者！**",
        "contact_success": "✅ **您的消息已成功发送给开发者！**",
        "reset": "🔄 重置聊天",
        "reset_text": "🔄 **聊天记忆已成功清除并重置！**",
        "about": "ℹ️ 关于系统",
        "about_text": "ℹ️ **Elnemer AI Bot v2.0**",
        "language": "🌐 更改语言",
        "select_lang": "🌐 **选择语言：**"
    }
}

def get_t(user_id: int, key: str) -> str:
    lang = user_languages.get(user_id, "en")
    if lang not in TRANSLATIONS:
        lang = "en"
    return TRANSLATIONS[lang].get(key, TRANSLATIONS["en"].get(key, key))

def is_rate_limited(user_id: int) -> bool:
    current_time = time.time()
    user_message_times[user_id] = [
        t for t in user_message_times[user_id] if current_time - t < RATE_LIMIT_WINDOW
    ]
    if len(user_message_times[user_id]) >= RATE_LIMIT_COUNT:
        return True
    user_message_times[user_id].append(current_time)
    return False

def get_main_keyboard(user_id: int):
    keyboard = [
        [InlineKeyboardButton(get_t(user_id, "pricing"), callback_data="pricing"), InlineKeyboardButton(get_t(user_id, "services"), callback_data="services")],
        [InlineKeyboardButton(get_t(user_id, "contact"), callback_data="contact")],
        [InlineKeyboardButton(get_t(user_id, "reset"), callback_data="reset"), InlineKeyboardButton(get_t(user_id, "about"), callback_data="about")],
        [InlineKeyboardButton(get_t(user_id, "language"), callback_data="language")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_language_keyboard():
    keyboard = [
        [InlineKeyboardButton("🇸🇦 العربية", callback_data="set_lang_ar"), InlineKeyboardButton("🇺🇸 English", callback_data="set_lang_en")],
        [InlineKeyboardButton("🇫🇷 Français", callback_data="set_lang_fr"), InlineKeyboardButton("🇪🇸 Español", callback_data="set_lang_es")],
        [InlineKeyboardButton("🇩🇪 Deutsch", callback_data="set_lang_de"), InlineKeyboardButton("🇨🇳 中 文", callback_data="set_lang_zh")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_states[user_id] = None
    user_histories[user_id] = []
    
    text = get_t(user_id, "welcome")
    await update.message.reply_text(text, reply_markup=get_main_keyboard(user_id), parse_mode="Markdown")

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data.startswith("set_lang_"):
        selected_lang = query.data.split("_")[2]
        user_languages[user_id] = selected_lang
        msg = f"✅ Language updated to: **{selected_lang.upper()}**"
        await query.message.reply_text(msg, reply_markup=get_main_keyboard(user_id), parse_mode="Markdown")
        return

    if query.data == "pricing":
        msg = get_t(user_id, "pricing_text")
    elif query.data == "services":
        msg = get_t(user_id, "services_text")
    elif query.data == "contact":
        user_states[user_id] = "awaiting_contact"
        msg = get_t(user_id, "contact_text")
        await query.message.reply_text(msg)
        return
    elif query.data == "reset":
        user_states[user_id] = None
        user_histories[user_id] = []
        msg = get_t(user_id, "reset_text")
    elif query.data == "about":
        msg = get_t(user_id, "about_text")
    elif query.data == "language":
        await query.message.reply_text(get_t(user_id, "select_lang"), reply_markup=get_language_keyboard(), parse_mode="Markdown")
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
                msg = get_t(user_id, "contact_success")
            except Exception as e:
                logger.error(f"Forwarding error: {e}")
                msg = "⚠️ حدث خطأ أثناء تحويل الرسالة للمطور."
        else:
            msg = "⚠️ ADMIN_CHAT_ID is missing in Railway variables."
        await update.message.reply_text(msg, parse_mode="Markdown")
        return

    user_histories[user_id].append({"role": "user", "content": user_text})

    if len(user_histories[user_id]) > 10:
        user_histories[user_id] = user_histories[user_id][-10:]

    messages = [
        {"role": "system", "content": f"You are a helpful AI assistant. Always respond in '{lang}' language."}
    ] + user_histories[user_id]

    try:
        response = g4f_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        reply = response.choices[0].message.content
        if reply:
            user_histories[user_id].append({"role": "assistant", "content": reply})
            await update.message.reply_text(reply)
        else:
            await update.message.reply_text("⚠️ No response generated.")
    except Exception as e:
        logger.error(f"AI Error: {e}")
        await update.message.reply_text("⚠️ Service temporarily busy, please try again.")

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
