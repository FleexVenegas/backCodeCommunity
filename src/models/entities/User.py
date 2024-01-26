from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User:
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password
    
    @classmethod
    def check_password(self, hash_password, password):
        return bcrypt.check_password_hash(hash_password, password)