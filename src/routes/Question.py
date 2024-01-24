from flask import Blueprint, jsonify
from database.db import get_connection_MySQL


main = Blueprint('question_blueprint', __name__)

# conexion = MySQL(main)

@main.route('/questions')
def index():

    connection = get_connection_MySQL()

    print(connection)

    with connection.cursor() as cursor:
        datas = cursor.execute("SELECT *  FROM questions")
        print(datas)


    return jsonify({"message": "Respuesta desde la API"})

