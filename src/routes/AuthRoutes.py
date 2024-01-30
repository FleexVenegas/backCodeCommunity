from flask_cors import CORS
from utils.Tools import Tools
from utils.Security import Security
from models.entities.User import User
from models.LoginModel import LoginModel
from flask import Blueprint, request, jsonify
from utils.CryptoGraphy.Cryptography import EncryptionManager

main = Blueprint("auth_blueprint", __name__)
CORS(main, supports_credentials=True)


@main.route('/validate-credentials', methods=['POST'])
def validate_credentials():
    try:
        datas_string = request.form["credentials"]
        credentials = Tools.convert_json(datas_string)

        user = User(0, credentials['username'], credentials['password'])
        logged_user = LoginModel.login(user)

        if logged_user != None:
            if logged_user.password:

                encrypt_user = EncryptionManager()
                encrypt_user = encrypt_user.encrypt_data(logged_user.username)
                encode_token = Security.generate_token(logged_user)

                return jsonify({"authToken": encode_token, "message": "Successful Authentication", "id": logged_user.id , "username": encrypt_user.decode('utf-8')}), 200
            
            else:
                return jsonify({"message": "Invalid Password"}), 400
            
        else:
            return jsonify({"message": "User no found"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)})

    
    # return jsonify({})


@main.route('/validate-akn', methods=['GET'])
def validate_token():
    try:
        authorization = Security.verify_token(request.headers)

        if authorization:
            return jsonify({"message": "Authorized access"}), 200
        else:
            return jsonify({"message": "Unauthorized access"}), 401
        
    except Exception as ex:
        return jsonify({"message": str(ex)})
    

@main.route('/decrypt-user', methods=['POST'])
def decrypt_user():
    try:
        user_string = request.form["user"]
        user = Tools.convert_json(user_string)
        
        if user != None:
            encrypt_user = EncryptionManager()
            encrypt_user = encrypt_user.decrypt_data(user['username'])

            return jsonify(encrypt_user)
        else:
            return jsonify({"message": "Error"})
        
    except Exception as ex:
         jsonify({"message": str(ex)})
    

