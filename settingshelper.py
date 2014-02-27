def get_server_url(http_method, server_root, username, password):
    if username and password:
        return '%(http_method)s://%(user)s:%(pass)s@%(server)s' % {
            'http_method': http_method,
            'user': username,
            'pass': password,
            'server': server_root,
        }
    else:
        return '%(http_method)s://%(server)s' % {
            'http_method': http_method,
            'server': server_root,
        }


def get_dynamic_db_settings(server_root, username, password, dbname,
                            use_https=False):
    """
    Get dynamic database settings.
    Other apps can use this if they want to change settings

    """

    http_method = 'https' if use_https else 'http'
    server_url = get_server_url(http_method, server_root, username, password)
    database = '%(server)s/%(database)s' % {
        'server': server_url,
        'database': dbname,
    }
    return {
        'COUCH_SERVER':  server_url,
        'COUCH_DATABASE': database,
    }


def make_couchdb_tuple(app_label, couch_database_url):
    """
    Helper function to generate couchdb tuples
    for mapping app name to couch database URL.

    Will also magically alter the URL for special core libraries;
    namely, auditcare, and couchlog
    """

    if app_label == 'auditcare' or app_label == 'couchlog':
        return app_label, '%s__%s' % (couch_database_url, app_label)
    else:
        return app_label, couch_database_url
