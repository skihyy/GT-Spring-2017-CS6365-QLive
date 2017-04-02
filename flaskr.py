import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='jz67NUU5$ych89S7D&yGkm&qNHZfzJj7q*Zs3&h!JyzvG'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


def connect_db():
    """
    Connect database.
    :return: database instance
    """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """
    When initialization, it will generate a sqlit3 database.
    Using python shell for creating the database: 
    >> from flaskr import init_db
    >> init_db()
    """
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    """
    Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('main.html', first=True)


@app.route('/login', methods=['POST'])
def log_in():
    error = 'Connection failed, please try again.'
    if 'POST' == request.method:
        # get instance of database
        db = get_db()
        cur = db.execute('SELECT id FROM users WHERE user_name = ? AND hashed_name_passwd = ?',
                         [request.form['name'], request.form['pass']])
        user = cur.fetchall()
        if 0 == len(user):
            error = 'Incorrect password / username, please try again.'
            return render_template('main.html', error=error)
        else:
            session['logged_in'] = True
            return go_to_home()
    return render_template('main.html', error=error)


@app.route('/home')
def go_to_home():
    if not session['logged_in']:
        return render_template('main.html')
    else:
        return render_template('home.html')


@app.route('/logout')
def log_out():
    session.pop('logged_in', None)
    return render_template('main.html')


@app.route('/live', methods=['GET', 'POST'])
def live():
    if not session['logged_in']:
        return render_template('main.html')
    else:
        print(request.form['type'])
        # TODO: if is host or participant
        is_host = request.form['type']
        # TODO: get app key from DB
        appkey = '8a746066-d341-459d-8fd7-06a78ef7a233'
        return render_template('live.html', is_host=is_host, appkey=appkey)


if '__main__' == __name__:
    app.run()
