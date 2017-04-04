import user_model


def get_live_sessions(db):
    """
    Get all live sessions.
    :param db: database instance
    :return: a list of all live sessions
    """
    res = []
    cur = db.execute('SELECT * FROM live_general')
    lives = cur.fetchall()
    for live in lives:
        host = user_model.get_user_info(db, lives['host_id'])
        live['host_name'] = host['nick_name']
        res.append(live)
    return res
