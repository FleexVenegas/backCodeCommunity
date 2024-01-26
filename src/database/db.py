import pymysql
from decouple import config


def get_connection_MySQL():
    try:
        return pymysql.connect(
            host=config('MYSQL_HOST'),
            user=config('MYSQL_USER'),
            password=config('MYSQL_PASSWORD'),
            db=config('MYSQL_DATABASE')
        )
    except Exception as ex:
        return {"message": f"Error al conectarse a la base de datos {str(ex)}", "status": 500}