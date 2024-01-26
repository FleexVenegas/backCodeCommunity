from flask_cors import CORS
from utils.Tools import Tools
from utils.Security import Security
from models.entities.User import User
from models.LoginModel import LoginModel
from flask import Blueprint, request, jsonify

main = Blueprint("auth_blueprint", __name__)
CORS(main, supports_credentials=True)


@main.route('/validate-credentials', methods=['POST'])
def validate_credentials():

    datas_string = request.form["credentials"]
    credentials = Tools.convert_json(datas_string)

    user = User(0, credentials['username'], credentials['password'])
    logged_user = LoginModel.login(user)

    if logged_user != None:
        if logged_user.password:
            encode_token = Security.generate_token(logged_user)

            return jsonify(encode_token)
        
        else:
            return jsonify({"message": "Invalid Password"}), 400
        
    else:
        return jsonify({"message": "User no found"}), 400
    
    # return jsonify({})

        

    

