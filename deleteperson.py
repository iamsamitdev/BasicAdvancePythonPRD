import pymysql
from dbpackage import ConnectMySQL as con


def edit_person():
    connection = con.connectdb()
    cursor = connection.cursor()
    sql = """
         DELETE FROM person WHERE id='2'
        """
    try:
        cursor.execute(sql)
        connection.commit()
        print('Delete person success.')
    except pymysql.err:
        print(pymysql.err)


edit_person()
