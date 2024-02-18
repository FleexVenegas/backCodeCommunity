from database.db import get_connection_MySQL

class ModelAnswer:

    @classmethod
    def add_answer(self, response):
        try:
            connection = get_connection_MySQL()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO response (id_response, response, id_user, id_question)
                                    VALUES (%s, %s, %s, %s)""",
                                    (response.id, response.response, response.id_user, response.id_question))
                affected_row = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_row
        
        except Exception as ex:
            return str(ex)