class User:
    """
    This is the user model for database management / website render in the flask.
    """

    def __init__(self):
        pass

    def __init__(self, id, uname, passwd, balance, nname):
        self.balance = balance
        self.id = id
        self.hashed_user_passwd = passwd
        self.nick_name = nname
        self.user_name = uname

    id = -1
    user_name = ''
    hashed_user_passwd = ''
    balance = ''
    nick_name = ''


def get_user_info(db, user_name, passwd):
    """
    Get detailed information of one user.
    :param db: database instance
    :param user_name: user name
    :param passwd: hashed user password
    :return: a user object or None if the user does not exist
    """
    cur = db.execute('SELECT * FROM users WHERE user_name = ? AND hashed_name_passwd = ?',
                     [user_name, passwd])
    user = cur.fetchall()
    if 0 == len(user):
        return None
    return User(user[0]['id'], user[0]['user_name'], user[0]['hashed_user_passwd'], user[0]['balance'],
                user[0]['nick_name'])


def get_user_info(db, uid):
    """
    Get detailed information of one user.
    :param db: database instance
    :param id: user id
    :return: a user object or None if the user does not exist
    """
    cur = db.execute('SELECT * FROM users WHERE id = ?', [uid])
    user = cur.fetchall()
    if 0 == len(user):
        return None
    return User(user[0]['id'], user[0]['user_name'], user[0]['hashed_user_passwd'], user[0]['balance'],
                user[0]['nick_name'])


def has_user(db, user_name, passwd):
    """
    Used for login to check whether the given information could retrieve an user.
    :param db: database instance
    :param user_name: user name
    :param passwd: hashed user password
    :return: whether the user exist
    """
    cur = db.execute('SELECT id FROM users WHERE user_name = ? AND hashed_name_passwd = ?',
                     [user_name, passwd])
    user = cur.fetchall()
    if 0 == len(user):
        return -1
    else:
        return user[0]['id']
