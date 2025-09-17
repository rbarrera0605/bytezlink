import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key for flash messages

DATABASE = 'your_database.db'  # Change this to your SQLite DB path


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/feedback', methods=['GET'])
def feedback():
    conn = get_db_connection()
    feedbacks = conn.execute('SELECT name, message, created_at FROM feedback ORDER BY created_at DESC').fetchall()
    conn.close()

    formatted_feedbacks = []
    for fb in feedbacks:
        formatted_feedbacks.append((
            fb['name'],
            fb['message'],
            datetime.strptime(fb['created_at'], '%Y-%m-%d %H:%M:%S').strftime('%b %d, %Y %I:%M %p')
        ))

    return render_template('feedback.html', feedbacks=formatted_feedbacks)


@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    message = request.form.get('feedback')

    if not name or not message:
        flash('Please fill out both your name and feedback.', 'error')
        return redirect(url_for('feedback'))

    conn = get_db_connection()
    conn.execute('INSERT INTO feedback (name, message) VALUES (?, ?)', (name, message))
    conn.commit()
    conn.close()

    flash('Thank you for your feedback!', 'success')
    return redirect(url_for('feedback'))


if __name__ == '__main__':
    init_db()  # Initialize DB and create table if not exists
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
