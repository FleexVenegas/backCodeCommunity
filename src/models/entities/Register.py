from utils.DateFormat import DateFormat

class Register:
    def __init__(self, id, user=None, password=None, email=None, registration_date=None) -> None:
        self.id = id
        self.user = user
        self.email = email
        self.password = password
        self.registration_date = registration_date
    
    def to_JSON(self):
        return { 
            "id": self.id, 
            "user": self.user, 
            "email": self.email, 
            "password": self.password, 
            "registration_date": DateFormat.convert_date(self.registration_date)
        }