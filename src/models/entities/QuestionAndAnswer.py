from utils.DateFormat import DateFormat

class Question_and_Answer:
    def __init__(self, id_question, title=None, description=None, tags=None, registration_date=None) -> None:
        self.id_question = id_question
        self.title = title
        self.description = description
        self.tags = tags
        self.registration_date = registration_date
        self.answers = []

    def add_answer(self, id_response, response, registration_date_answer):
        self.answers.append({
            "id_response": id_response,
            "response": response,
            "registration_date_answer": DateFormat.convert_date(registration_date_answer) if registration_date_answer else None
        })

    def to_JSON_Answer(self):
        return {
            "question": {
                "id_question": self.id_question,
                "title": self.title,
                "description": self.description,
                "tags": self.tags,
                "registration_date": DateFormat.convert_date(self.registration_date) if self.registration_date else None
            },
            "answers": self.answers
        }



# class Question_and_Answer:
#     def __init__(self, id_question, title=None, description=None, tags=None, registration_date=None, 
#                         response=None, id_response=None, registration_date_answer=None) -> None:
#         self.id_question = id_question
#         self.title = title
#         self.description = description
#         self.tags = tags
#         # self.id_user = id_user
#         self.registration_date = registration_date
#         self.response = response
#         self.id_response = id_response
#         self.registration_date_answer = registration_date_answer
    

#     def to_JSON_Answer(self):
#         return{
#             "question":{
#                 "id_question": self.id_question,
#                 "title": self.title,
#                 "description": self.description,
#                 "tags": self.tags,
#                 "registration_date": DateFormat.convert_date(self.registration_date)
#             },
#             "answers": [{
#                 "response": self.response,
#                 "id_response": self.id_response,
#                 "registration_date_answer": DateFormat.convert_date(self.registration_date_answer)
#             }]
#         }