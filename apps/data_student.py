from apps.mysql_pool_connection import MYSQL_pool_connection


def list_students():
    sql = """
    SELECT * FROM `demo`.`student`
    """
    result = MYSQL_pool_connection.execute(sql)
    return result


def save_student(data):
    if 'id' not in data:
        insert_student(data)
    else:
        update_student(data)
    return data


def insert_student(data):
    sql = "INSERT INTO `demo`.`student`(`age`, `birth`, `gender`, `name`, `parent`) VALUES (%s, STR_TO_DATE(%s, '%%Y-%%m-%%d'), %s, %s, %s)"
    val = (data['age'], data['birth'], data['gender'], data['name'], data['parent'])
    return MYSQL_pool_connection.execute_commit(sql, val)


def update_student(data):
    sql = "UPDATE `demo`.`student` SET `age` = %s, `birth` = STR_TO_DATE(%s, '%%Y-%%m-%%d'), `gender` = %s, `name` = %s, `parent` = %s WHERE `id` = %s"
    val = (data['age'], data['birth'], data['gender'], data['name'], data['parent'], data['id'])
    return MYSQL_pool_connection.execute_commit(sql, val)


def get_student(id):
    sql = """
    SELECT * FROM demo.student WHERE id = %s
    """ % id
    result = MYSQL_pool_connection.execute(sql)
    return result


def delete_student(id):
    sql = """
    DELETE from demo.student WHERE id = %s
    """ % id
    MYSQL_pool_connection.execute_commit(sql)
