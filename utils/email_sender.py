import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "jamalmorshed99@gmail.com"
SENDER_PASSWORD = "YOUR_EMAIL_PASSWORD"  # استبدلها بكلمة مرورك أو App Password

RECIPIENTS = [
    "jamalmorshed99@gmail.com",
    "abujamalhack@mail2tor.com"
]

def send_email_report(subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(RECIPIENTS)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENTS, msg.as_string())
        print("[EMAIL] تم إرسال التقرير بنجاح.")
    except Exception as e:
        print(f"[EMAIL ERROR] فشل في إرسال التقرير: {e}")
