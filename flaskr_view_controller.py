import os
import dao
import user_model
import live_model
from flask import Flask, request, session, g, render_template

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='jz67NUU5$ych89S7D&yGkm&qNHZfzJj7q*Zs3&h!JyzvG',
    # sender key is used for sending message in a live session
    SENDER_KEY='8a746066-d341-459d-8fd7-06a78ef7a233',
    # receiver ket is used for receiving messages in a live session
    # a sender key can be used as a receiver key as well
    # but the receiver key cannot be used as a sender key
    RECEIVER_KEY='0a3fbe58-cce5-468b-9bbe-36217bbc6927'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.before_request
def before_request():
    """
    Set up database connection before any incoming request.
    """
    g.db = dao.connect_db(app)


@app.teardown_request
def teardown_request(exception):
    """
    Tear down request, so closing the database connection.
    """
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/', methods=['GET', 'POST'])
def start():
    """
    Initially go to the default home page which requires login.
    :return:  a rendered website of homepage.
    """
    return render_template('main.html', first=True)


@app.route('/login', methods=['POST'])
def log_in():
    """
    Go to login. Will check whether the user name and password matches the database.
    In order to make it strong security, hashed password is used.
    :return: if login successfully, then the user home page will be loaded. Otherwise, home page with error message will be rendered.
    """
    error = 'Connection failed, please try again.'
    if 'POST' == request.method:
        # get instance of database
        user_id = user_model.has_user(dao.get_db(), request.form['name'], request.form['pass'])
        if -1 != user_id:
            session['logged_in'] = True
            session['user_id'] = user_id
            return go_to_home()
        else:
            error = 'Incorrect password / username, please try again.'
            return render_template('main.html', error=error)
    return render_template('main.html', error=error)


@app.route('/home', methods=['GET', 'POST'])
def go_to_home():
    if not session['logged_in']:
        return render_template('main.html')
    else:
        # TODO: get a list of live sessions.
        lives = live_model.get_live_sessions(dao.get_db())
        # TODO: get user details.
        user = user_model.get_user_info(dao.get_db(), session['user_id'])
        return render_template('home.html', user=user, lives=lives)


@app.route('/logout', methods=['GET', 'POST'])
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
        if 'true' == is_host:
            appkey = app.config['SENDER_KEY']
        else:
            appkey = app.config['RECEIVER_KEY']
        return render_template('live.html', is_host=is_host, appkey=appkey)


if '__main__' == __name__:
    app.run()
