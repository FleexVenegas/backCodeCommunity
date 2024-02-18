from flask import Blueprint, jsonify, request
import uuid
from utils.Tools import Tools
from utils.Security import Security
from models.entities.Answer import Answers
from models.ModelAnswers import ModelAnswer

main = Blueprint("answer_blueprint", __name__)


@main.route('/add-answer', methods=['POST'])
def add_answer():
    response_string = request.form['response']
    response_json = Tools.convert_json(response_string)

    cookies_token = request.cookies.get("116111en")
    authentication = Security.verify_token(cookies_token)
    id = uuid.uuid4()

    if authentication:
        response = Answers(str(id), response_json['response'], response_json['id_user'], response_json['id_question'])
        affected_row = ModelAnswer.add_answer(response)

        if affected_row == 1:
            return({"message": "Answer added successfully"}), 200

        else:
            return jsonify({"message": "Error adding response", "error": str(affected_row)}), 500
        
    else:
        return jsonify({"message": "This action requires authentication. Please log in or register.", "error": "Unauthorized",}), 401
