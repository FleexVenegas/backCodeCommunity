from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Encrypt_password:

    @classmethod
    def encrypt_password(self, password):
        pw_hash = bcrypt.generate_password_hash(password)
        return pw_hash
    
