# -*- coding: utf-8 -*-
import dao


def get_user_info(user_name, passwd):
    """
    Get detailed information of one user.
    :param user_name: user name
    :param passwd: hashed user password
    :return: a user object or None if the user does not exist
    """
    user = dao.query_db('SELECT * FROM users WHERE user_name = ? AND hashed_name_passwd = ?',
                        [user_name, passwd], True)
    return user


def get_user_info(uid):
    """
    Get detailed information of one user.
    :param id: user id
    :return: a user object or None if the user does not exist
    """
    user = dao.query_db('SELECT * FROM users WHERE id = ?', [uid], True)
    return user


def has_user(user_name, passwd):
    """
    Used for login to check whether the given information could retrieve an user.
    :param user_name: user name
    :param passwd: hashed user password
    :return: whether the user exist
    """
    user = dao.query_db('SELECT id FROM users WHERE user_name = ? AND hashed_name_passwd = ?',
                        [user_name, passwd])
    if 0 == len(user):
        return -1
    else:
        return user[0]['id']


def update_balance(user_id, new_balance):
    dao.query_add('UPDATE users SET balance = ? WHERE id = ?', args=[new_balance, user_id])
