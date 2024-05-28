from flask import Flask, render_template
import psycopg2
app = Flask(__name__)

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=""
)

# Функция для выполнения запросов к базе данных
def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Массивы с карточками
flashcards_book=execute_query("SELECT engilish, russian FROM words;")
flashcards = []
for i in flashcards_book:
    my_dict = {f'english': i[0], f'russian': i[1]}
    flashcards.append(my_dict)

current_card_index = 0

@app.route('/')
def index():
    return render_template('index.html', flashcards=flashcards, current_card_index=current_card_index)

@app.route('/next', methods=['POST'])
def next_card():
    global current_card_index

    # Переходим к следующей карточке
    current_card_index = (current_card_index + 1) % len(flashcards)

    return render_template('index.html', flashcards=flashcards, current_card_index=current_card_index)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
