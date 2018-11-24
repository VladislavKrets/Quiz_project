from flask import Flask, render_template, redirect, url_for, session, escape, request

from src.model.DAO import DAO
import os

app = Flask(__name__, template_folder='../view/admin', static_folder='../view/admin')
dao = DAO()
app.secret_key = os.urandom(16)


@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('users'))
    if request.method == 'POST':
        user = dao.isUserInDb(request.form['username'], request.form['password'])
        if len(user) != 0:
            session['username'] = request.form['username']
        return redirect(url_for('users'))
    return render_template('Login.html')


@app.route('/admin/statistics', methods=['GET'])
def statistics():
    if 'username' in session:
        return render_template('Statistics.html')
    else:
        return redirect(url_for('login'))


@app.route('/admin/users', methods=['GET'])
def users():
    if 'username' in session:
        users = dao.getUsers()
        return render_template('Users.html', users=users)
    else:
        return redirect(url_for('login'))


@app.route('/admin/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


app.run()