import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_SENDER = "jamalmorshed99@gmail.com"
EMAIL_PASSWORD = "abujamal"  # ⚠️ إذا كنت تستخدم Gmail فعّل "كلمة مرور التطبيقات"

RECIPIENTS = [
    "jamalmorshed99@gmail.com",
    "abujamalhack@mail2tor.com"
]

def send_email_report(phone, message):
    subject = "🚨 بلاغ ابتزاز جديد"
    body = f"رقم المبتز: {phone}\n\nالرسالة:\n{message}"

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = ", ".join(RECIPIENTS)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, RECIPIENTS, msg.as_string())
        server.quit()
        print("📧 تم إرسال البلاغ عبر البريد الإلكتروني")
    except Exception as e:
        print("Email Error:", e)
