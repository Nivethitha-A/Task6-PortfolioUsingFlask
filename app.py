from flask import Flask, render_template, request, redirect, url_for, flash
import datetime

app = Flask(__name__)
app.secret_key = 'replace-with-a-secure-random-key'


# Home
@app.route('/')
def index():
    return render_template('index.html')


# About
@app.route('/about')
def about():
    return render_template('about.html')


# Contact (GET shows form, POST handles submission)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        timestamp = datetime.datetime.now().isoformat()

        # Save messages to messages.txt
        with open('messages.txt', 'a', encoding='utf-8') as f:
            f.write(f"{timestamp}\t{name}\t{email}\t{message}\n")

        flash('Thanks! Your message has been received.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
