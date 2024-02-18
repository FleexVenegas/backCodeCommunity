import uuid
from flask_cors import CORS
from utils.Tools import Tools
from utils.Security import Security
from flask import Blueprint, jsonify, request

# Model
from models.QuestionModel import QuestionModel

# Intities
from models.entities.Questions import Question


main = Blueprint('question_blueprint', __name__)
CORS(main, supports_credentials=True)


@main.route('/add-question', methods=['POST'])
def add_question():
    try:
        question_string = request.form["question"]
        question_dict = Tools.convert_json(question_string)
        question_id = uuid.uuid4()
        cookies = request.cookies.get("116111en")
        cookie_user = request.cookies.get("105d")

        authorization = Security.verify_token(cookies)

        if authorization:
            question = Question(str(question_id), question_dict['title'], question_dict['description'], question_dict['tags'], cookie_user)
            
            affected_row = QuestionModel.add_question(question)

            if affected_row == 1:
                return jsonify({"message": "Question registered correctly"}), 200

            else:
                return jsonify({"message": "Error registering question"}), 500

        else:
            return jsonify({"message": "This action requires authentication. Please log in or register.", "error": "Unauthorized",}), 401

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500    



@main.route('/get-questions', methods=['GET'])
def get_questions():
    try: 
        questions = QuestionModel.get_questions()
        return jsonify(questions)

    except Exception as ex:
        return jsonify({"message": str(ex)})
    


@main.route('/get-question/<id>', methods=['GET'])
def get_question(id):
    try:
        question = QuestionModel.get_question(id) 
        if question != None:
            return jsonify({"data": question}), 200
        
        else:
            return jsonify({"message": "Question not found"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)})
    

@main.route('/get-count/', methods=['GET'])
def count_question_answer():
    try:
        id_user = request.cookies.get("105d")

        total_questions = QuestionModel.count_question(id_user)
        total_responses = QuestionModel.count_response(id_user)

        return jsonify({"question_total": total_questions, "answer_total": total_responses})

    except Exception as ex:
        return jsonify({"message": str(ex)})












