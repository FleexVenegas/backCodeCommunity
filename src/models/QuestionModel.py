from database.db import get_connection_MySQL
from models.entities.Questions import Question
from models.entities.QuestionAndAnswer import Question_and_Answer
import json

class QuestionModel:

    @classmethod
    def add_question(self, question):
        try:
            connection = get_connection_MySQL()
            question_tags = json.dumps(question.tags)

            with connection.cursor() as cursor:
                cursor.execute(""" INSERT INTO questions (id_question, title, description, tags, id_user) 
                                    VALUES (%s, %s, %s, %s, %s)""", 
                                    (question.id, question.title, question.description, question_tags, question.id_user))
                affected_row = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_row 

        except Exception as ex:
            return str(ex)
    

    @classmethod
    def get_questions(self):
        try:
            connection = get_connection_MySQL()
            questions = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_question, title, description, tags, id_user, registration_date FROM questions ORDER BY registration_date ASC")
                result_set = cursor.fetchall()

                for row in result_set:
                    question = Question(row[0], row[1], row[2], row[3], "", row[5])
                    questions.append(question.to_JSON_Question())
                
            connection.close()
            return questions

        except Exception as ex:
            return str(ex)
        
    @classmethod    
    def get_question(self, id):
        try:
            connection = get_connection_MySQL()
            question_and_answer = {}

            with connection.cursor() as cursor:
                cursor.execute(""" SELECT questions.id_question, questions.title, questions.description, questions.tags, questions.registration_date,
                                    response.id_response, response.response, response.registration_date AS response_date FROM questions
                                    LEFT JOIN response ON questions.id_question = response.id_question WHERE questions.id_question = %s """, (id))
                result_set = cursor.fetchall()

                if result_set:
                    for row in result_set:
                        if row[0] not in question_and_answer:
                            question_and_answer[row[0]] = Question_and_Answer(row[0], row[1], row[2], row[3], row[4])
                        if row[5]:  # Verificar si hay una respuesta válida
                            question_and_answer[row[0]].add_answer( row[5], row[6], row[7] )

            question_and_answer_list = [qa.to_JSON_Answer() for qa in question_and_answer.values()]
            
            connection.close()
            return question_and_answer_list

        except Exception as ex:
            return str(ex)
        

    @classmethod
    def count_question(self, id):
        try:
            connection = get_connection_MySQL()

            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) AS questions FROM questions WHERE id_user = %s", (id))
                row = cursor.fetchone()

                total = None
                if row != None:
                    total = row[0]
            
            connection.close()
            return total
        
        except Exception as ex:
            return str(ex)
        

    @classmethod
    def count_response(self, id):
        try:
            connection = get_connection_MySQL()

            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) AS response FROM response WHERE id_user = %s", (id))
                row = cursor.fetchone()

                total = None
                if row != None:
                    total = row[0]
            
            connection.close()
            return total
        
        except Exception as ex:
            return str(ex)