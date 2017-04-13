# -*- coding: utf-8 -*-
import user_model
import dao


def get_live_sessions():
    """
    Get all live sessions.
    :param db: database instance
    :return: a list of all live sessions
    """
    res = []
    lives = dao.query_db('SELECT * FROM live_general')
    for live in lives:
        # live is a data tuple from live_general
        host = user_model.get_user_info(live['host_id'])
        live['host_name'] = host['nick_name']
        res.append(live)
    return res


def get_live_session(lid):
    """
    Get details of a live session
    :param lid: live session id
    :return: 
    """
    return dao.query_db('SELECT * FROM live_general WHERE id = ?', [lid], one=True)


def create_live_session(host_id, title, price):
    """
    Add a new live session into database.
    :param host_id: user id of the host
    :param title: the title of live session
    :param price: the price of this session
    """
    dao.query_add('INSERT INTO live_general (title, host_id, price) VALUES (?, ?, ?)',
                  args=[title, host_id, price])


def end_live_session(live_id):
    """
    End current live session.
    :param live_id: live session id
    """
    dao.query_add('UPDATE live_general SET has_end = 1 WHERE id = ?', [live_id])


def get_live_session_id():
    """
    :return: Return the live session id.
    """
    return dao.query_db('SELECT COUNT(id) FROM live_general', one=True)['COUNT(id)']


def has_paid(uid, lid):
    """
    Check whether one has paid price for live session.
    :param uid: user id
    :param lid: live id
    :return: whether one has paid
    """
    count = dao.query_db('SELECT COUNT(id) FROM live_participants WHERE participant_id = ? AND live_id = ?',
                         [uid, lid], one=True)['COUNT(id)']
    if 0 == count:
        return False
    else:
        return True


def add_participant(live_id, participant_id):
    """
    Add a new participant into a live session. Also, if there is a price, the balance will be changed.
    :param live_id: live id
    :param participant_id: user id
    """
    print(live_id)
    print(participant_id)
    live = get_live_session(live_id)
    print(live)
    if '0' != live['price']:
        # host
        host_id = get_live_session(live_id)['host_id']
        host_balance = user_model.get_user_info(host_id)['balance']
        host_balance = host_balance + live['price']
        user_model.update_balance(host_id, host_balance)
        # participant
        participant_balance = user_model.get_user_info(participant_id)['balance']
        participant_balance = participant_balance - live['price']
        user_model.update_balance(participant_id, participant_balance)
    dao.query_add('INSERT INTO live_participants (live_id, participant_id) VALUES (?, ?)',
                  args=[live_id, participant_id])
