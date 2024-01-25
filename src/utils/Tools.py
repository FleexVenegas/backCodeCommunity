from flask import json

class Tools:
    
    @classmethod
    def convert_json(self, _string):
        # Convertir la string en formato JSON
        _dict = json.loads(_string)

        return _dict
    
    @classmethod
    def compare_password(self, password, confirm_password):
        # Compara las contraseñas
        if password == confirm_password:
            return True
        else:
            return False
    

    