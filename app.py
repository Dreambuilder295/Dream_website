from flask import Flask, render_template, request
import os
import config  # This should be at the top with other imports

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', site_title=config.SITE_TITLE)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # You can use these values to send emails or store in a DB later
        return render_template('thankyou.html', name=name)
    return render_template('contact.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
