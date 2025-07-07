
# 💻 CyberHunter Web

نظام ويب متكامل لتتبع المبتزين الإلكترونيين، توليد تقارير، وإرسال تنبيهات تلقائية لحماية الضحايا.

**بالإنجليزية:**  
A comprehensive web system to track cyber blackmailers, generate reports, and send automatic alerts to protect victims.

---

## 🚀 مميزات النظام

- واجهة مستخدم عربية/إنجليزية باستخدام Flask.
- توليد تقارير PDF منظمة لكل بلاغ.
- إرسال تنبيهات تلقائية عبر Telegram والبريد الإلكتروني.
- تخزين بيانات البلاغات في SQLite بشكل آمن.
- واجهة تسجيل دخول محمية بكلمة سر.
- متوافق مع Termux وKali Linux والأنظمة الخفيفة.

---

## ⚙️ المتطلبات

- Python 3.8+
- pip

---

## 📦 التثبيت والتشغيل

```bash
git clone https://github.com/734694194/CyberHunterWeb.git
cd CyberHunterWeb
pip install -r requirements.txt
python app.py

🔐 كلمة المرور للدخول:

abujamal


---

📁 هيكل المشروع

CyberHunterWeb/
├── app.py                # سكربت التشغيل الرئيسي
├── hunter.db             # قاعدة البيانات (تُنشأ تلقائيًا)
├── templates/            # ملفات HTML (واجهة المستخدم)
│   ├── login.html
│   └── dashboard.html
├── static/
│   └── style.css         # تنسيقات CSS
├── utils/                # الأدوات المساعدة
│   ├── email_sender.py
│   ├── telegram_bot.py
│   └── pdf_report.py
├── reports/              # التقارير المُولدة (PDF)
├── requirements.txt
├── README.md
└── .gitignore


---

🧠 ملاحظات إضافية

🗃️ ملاحظة: لا حاجة لرفع أو تحميل قاعدة البيانات hunter.db. سيتم إنشاؤها تلقائيًا في أول تشغيل للبرنامج.


---

💬 تواصل معي

Telegram: @ABU_JAMAL777 | @Abu_Jamal771

Email: jamalmorshed99@gmail.com | abujamalhack@mail2tor.com


---

هل تود أن أرسل لك كل ملف بنسخته أيضًا داخل ملف `.zip`؟ أم أنك سترفعهم يدويًا بنفسك الآن من هاتفك على GitHub؟

