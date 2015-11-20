# blog.py - controller

#imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = "\x08\xd6\xd3\x89'\x8a\xf7_\xd7\x81\x06rs\xec\x08\xe6\x84\xef\xe0UkU\xfd\\"

app =Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
         request.form['password'] !=app.config['PASSWORD']:
            error = "Invalid Credentials. Please try again."
        else:
            session['logged in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)
