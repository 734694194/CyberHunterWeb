import smtplib
from email.message import EmailMessage

# إعدادات البريد الإلكتروني
EMAIL_ADDRESS = "jamalmorshed99@gmail.com"
EMAIL_PASSWORD = "abujamal"  # ⚠️ استخدم كلمة مرور خاصة بالتطبيق (App Password) إن كنت تستخدم Gmail
RECIPIENTS = [
    "jamalmorshed99@gmail.com",
    "abujamalhack@mail2tor.com"
]

def send_email_report(subject, body, attachment_path=None):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_path:
        try:
            with open(attachment_path, "rb") as f:
                file_data = f.read()
                file_name = f.name
                msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
        except Exception as e:
            print(f"[EMAIL ERROR] فشل في إرفاق التقرير: {e}")
            return

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("[EMAIL] تم إرسال التقرير بنجاح.")
    except Exception as e:
        print(f"[EMAIL ERROR] فشل إرسال البريد الإلكتروني: {
