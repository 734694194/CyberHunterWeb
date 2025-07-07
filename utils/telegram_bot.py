import requests

BOT_TOKEN = "7729969699:AAFTGWKMXmegkiLT2qYvkkwQy102jiowM78"
CHAT_IDS = [
    "734694194",       # @ABU_JAMAL777
    "@Abu_Jamal771"    # حساب ثاني
]

def send_telegram_alert(phone, message):
    alert_text = f"🚨 *بلاغ ابتزاز إلكتروني* 🚨\n\n📞 الرقم: `{phone}`\n💬 الرسالة:\n{message}"
    for chat_id in CHAT_IDS:
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": alert_text,
                    "parse_mode": "Markdown"
                }
            )
        except Exception as e:
            print(f"[TELEGRAM ERROR] Failed to send to {chat_id}: {e}")
