import sqlite3
from flask import g


def connect_db(app):
    """
    Connect database.
    :return: database instance
    """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db(app):
    """
    When initialization, it will generate a sqlit3 database.
    Using python shell for creating the database: 
    >> from flaskr import init_db
    >> init_db()
    """
    with app.app_context():
        db = get_db(app)
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db(app):
    """
    Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db(app)
    return g.sqlite_db


def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv
