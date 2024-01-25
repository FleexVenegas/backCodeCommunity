from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Encrypt_password:

    @classmethod
    def encrypt_password(self, password):
        pw_hash = bcrypt.generate_password_hash(password)
        return pw_hash
    
    @classmethod
    def check_password(self, hash_password, password):
        return bcrypt.check_password_hash(hash_password, password)