from flask import Flask, render_template, request
import requests # Telegram'га POST суроо жөнөтүү үчүн

# КОНФИГУРАЦИЯ (ӨЗГӨРТҮҮ КЕРЕК!)
TELEGRAM_BOT_TOKEN = "8388878151:AAHB7kN8S50Whu_UmoAv3lrV54B1LLOzVLs"  # Мисалы: 123456:ABC-DEF123456
TELEGRAM_CHAT_ID = "5086705602"

# Flask'тын инстанциясын түзүү
app = Flask(__name__)

# -----------------
# TELEGRAM БИЛДИРҮҮСҮН ЖӨНӨТҮҮ ФУНКЦИЯСЫ
# -----------------
def send_telegram_message(text):
    """Берилген текстти Telegram'га жөнөтүү."""
    
    # Telegram API'нин URL'и
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    # Суроо үчүн параметрлер
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML" # HTML форматтоосун колдонуу
    }
    
    try:
        # POST суроо жөнөтүү
        response = requests.post(url, data=payload)
        response.raise_for_status() # Статус коду 4xx же 5xx болсо катаны көтөрүү
        print("Telegram'га билдирүү ийгиликтүү жөнөтүлдү.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Telegram'га билдирүү жөнөтүүдө ката кетти: {e}")
        return False

# -----------------
# МАРШРУТТАР (ROUTES)
# -----------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # POST методу - форма жөнөтүлгөндө
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_body = request.form.get('message_body')
        
        # HTML форматындагы билдирүү түзүү
        telegram_message = (
            "<b>🔥 ПОРТФОЛИО: ЖАҢЫ БИЛДИРҮҮ 🔥</b>\n\n"
            f"<b>Аты:</b> {name}\n"
            f"<b>Email:</b> <code>{email}</code>\n\n"
            "<b>Билдирүү:</b>\n"
            f"{message_body}"
        )

        # Telegram'га жөнөтүү
        if send_telegram_message(telegram_message):
            success_message = "Рахмат! Билдирүүңүз Telegram аркылуу кабыл алынды."
        else:
            success_message = "Кечиресиз, билдирүү жөнөтүүдө ката кетти. Сураныч, түздөн-түз email аркылуу байланышыңыз."
            
        # Форманы кайра render кылуу, бирок ийгиликтүү билдирүү менен
        return render_template('contact.html', message=success_message)
    
    # GET методу - бетти жөн эле ачуу
    return render_template('contact.html')


# -----------------
# КОЛДОНМОНУ ИШКЕ КИРГИЗҮҮ
# -----------------
if __name__ == '__main__':
    # Жайгаштыруу үчүн debug=False болушу керек
    app.run(debug=True)