from utils.DateFormat import DateFormat



class Answers:
    def __init__(self, id, response=None, id_user=None, id_question=None, registration_date=None) -> None:
        self.id = id
        self.response = response
        self.id_user = id_user
        self.id_question = id_question
        self.registration_date = registration_date
    

    def to_JSON(self):
        return{
            "id": self.id,
            "response": self.response,
            "id_user": self.id_user,
            "id_question": self.id_question,
            "registration_date": DateFormat.convert_date(self.registration_date)
        }
        