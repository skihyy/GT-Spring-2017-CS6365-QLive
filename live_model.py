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
        print(host)
        live['host_name'] = host['nick_name']
        res.append(live)
    return res
