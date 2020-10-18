import pymysql

MYSQL_CONFIG = {
    'host': 'mysql',  # mysql or '127.0.0.1'
    'port': 3306,
    'user': 'root',
    'password': 'mysql520',
    'charset': 'utf8',
    'use_unicode': True,
    'cursorclass': pymysql.cursors.DictCursor,
    'connect_timeout': 60,
    'maxconnections': 50
}
