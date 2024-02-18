from flask_cors import CORS
from utils.Tools import Tools
from utils.Security import Security
from models.entities.User import User
from models.LoginModel import LoginModel
from flask import Blueprint, request, jsonify, make_response
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

                cookies_dict = {
                    "116111en": encode_token,
                    "105d": logged_user.id,
                    "117er": encrypt_user.decode('utf-8')
                }

                _make_response = make_response({"message": "Successful Authentication", "id": logged_user.id})
                for cookie_name, cookie_value in cookies_dict.items():
                    _make_response.set_cookie(cookie_name, value=cookie_value, httponly=True, samesite="None", secure=True)

                return _make_response, 200
            
            else:
                return jsonify({"message": "Invalid Password"}), 400
            
        else:
            return jsonify({"message": "User no found"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route('/validate-akn', methods=['GET'])
def validate_token():
    try:
        cookies = request.cookies.get('116111en')
        authorization = Security.verify_token(cookies)

        if authorization:
            return jsonify({"message": "Authorized access"}), 200
        else:
            return jsonify({"message": "Unauthorized access"}), 401

    except Exception as ex:
        return jsonify({"message": str(ex)})
    


@main.route('/decrypt-user', methods=['GET'])
def decrypt_user():
    try:
        getCookie_aut = request.cookies.get("116111en")
        authorization = Security.verify_token(getCookie_aut)

        if authorization:
            get_user = request.cookies.get("117er")

            if get_user != None:
                encrypt_user = EncryptionManager()
                encrypt_user = encrypt_user.decrypt_data(get_user)

                return jsonify(encrypt_user)
            else:
                return jsonify({"message": "Error"})
        
    except Exception as ex:
         jsonify({"message": str(ex)})



@main.route('/logout', methods=['GET'])
def logOut():
    try:

        response = make_response({"message": "Successful logout"})
        response.delete_cookie("116111en", httponly=True, samesite="None", secure=True)

        return response, 200
    
    except Exception as ex:
        return jsonify({"message": str(ex)})
    

