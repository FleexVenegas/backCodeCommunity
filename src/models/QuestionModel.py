from database.db import get_connection_MySQL
from models.entities.Questions import Question

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

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_question, title, description, tags, id_user, registration_date FROM questions WHERE id_question = %s", (id))
                row = cursor.fetchone()
                question = None
                if row != None:
                    question = Question(row[0], row[1], row[2], row[3], "", row[5])
                    question = question.to_JSON_Question()
            
            connection.close()
            return question

        except Exception as ex:
            return str(ex)