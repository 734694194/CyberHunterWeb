from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3
from datetime import datetime
from utils.pdf_report import generate_report
from utils.telegram_bot import send_telegram_alert
from utils.email_sender import send_email_report

app = Flask(__name__)
app.secret_key = 'abujamal'  # كلمة مرور الجلسة

DATABASE = 'hunter.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute('''
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'abujamal':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="كلمة المرور غير صحيحة")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    db = get_db()
    reports = db.execute('SELECT * FROM reports ORDER BY id DESC').fetchall()
    return render_template('dashboard.html', reports=reports)

@app.route('/report', methods=['POST'])
def report():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    phone = request.form.get('phone')
    message = request.form.get('message')

    if not phone or not message:
        return "يرجى إدخال جميع الحقول", 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_db() as db:
        db.execute("INSERT INTO reports (phone, message, timestamp) VALUES (?, ?, ?)", (phone, message, timestamp))
    
    # توليد تقرير PDF
    report_path = generate_report(phone, message)

    # إرسال تنبيهات
    send_telegram_alert(phone, message)
    send_email_report(phone, message, report_path)

    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
