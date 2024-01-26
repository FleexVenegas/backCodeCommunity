
from database.db import get_connection_MySQL
from .entities.User import User


class LoginModel:

    @classmethod
    def login(self, user):
        try:
            connection = get_connection_MySQL()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, username, password FROM users WHERE username = %s", (user.username))
                row = cursor.fetchone()

                if row != None:
                    found_user = User(row[0], row[1], User.check_password(row[2], user.password))
                    return found_user
                
                else:
                    return None
        
        except Exception as ex:
            return {"message": connection['message'], "Error": str(ex), "ErroStatus": 500}
