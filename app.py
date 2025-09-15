import os
from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # get port from env variable or use 5000
    app.run(host='0.0.0.0', port=port, debug=True)  # bind to all interfaces and the port
