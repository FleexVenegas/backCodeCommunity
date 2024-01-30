from utils.DateFormat import DateFormat

class Question:
    def __init__(self, id, title=None, description=None, tags=None, id_user=None, registration_date=None) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.tags = tags
        self.id_user = id_user
        self.registration_date = registration_date

    
    def to_JSON_Question(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "tags": self.tags,
            "id_user": self.id_user,
            "registration_date": DateFormat.convert_date(self.registration_date)
        }



     