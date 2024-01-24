from database.db import get_connection_MySQL
from .entities.Register import Register

class RegisterModel:

    @classmethod
    def get_registers(self):
        try:
            connection = get_connection_MySQL()
            registers = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, username, email, password, registration_date FROM users ORDER BY username ASC")
                result_set = cursor.fetchall()

                for row in result_set:
                    register = Register(row[0], row[1], row[3], row[2], row[4])
                    registers.append(register.to_JSON())
            
            connection.close()
            return registers
        
        except Exception as ex:
            return str(ex)
        
    @classmethod
    def get_register(self, id):
        try:
            connection = get_connection_MySQL()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, username, email, password, registration_date FROM users WHERE id = %s", (id))
                row = cursor.fetchone()
                
                register = None
                if row != None:
                    register = Register(row[0], row[1], row[3], row[2], row[4])
                    register = register.to_JSON()
            
            connection.close()
            return register
        
        except Exception as ex:
            return str(ex)
        
    @classmethod
    def add_register(self, register):
        try:
            connection = get_connection_MySQL()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO users (id, username, email, password) 
                                    VALUES (%s, %s, %s, %s)""", 
                                    (register.id, register.user, register.password, register.email))
                affected_row = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_row
        
        except Exception as ex:
            return str(ex)
        
    @classmethod
    def delete_register(self, register):
        try:
            connection = get_connection_MySQL()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", (register.id))
                affected_row = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_row
        
        except Exception as ex:
            return str(ex)
    @classmethod

    def update_register(self, register):
        try:
            connection = get_connection_MySQL()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE users SET username = %s, email = %s, password = %s
                                    WHERE id = %s""", (register.user, register.password, register.email, register.id))
                affected_row = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_row
        
        except Exception as ex:
            return str(ex)



