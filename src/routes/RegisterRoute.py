import uuid
from flask import Blueprint, request, jsonify
from utils.Json import Tools

# Intities
from models.entities.Register import Register

# Models
from models.RegisterModel import RegisterModel

main = Blueprint("register_blueprint", __name__)


@main.route("/get-users", methods=['GET'])
def get_registers():
    try:
        registers = RegisterModel.get_registers()
        return jsonify(registers)
    
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    

@main.route("/get-user/<id>", methods=['GET'])
def get_register(id):
    try:
        register = RegisterModel.get_register(id)

        if register != None:
            return jsonify(register)
        else:
            return jsonify({}), 404
            
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    

@main.route("/add-user", methods=['POST'])
def add_user():
    try:
        _string = request.form['formUser']
        _dict = Tools.convert_json(_string)

        user = _dict['username']
        email = _dict['email']
        password = _dict['password']
        id = uuid.uuid4()

        register = Register(str(id), user, email, password)
        affected_row = RegisterModel.add_register(register)

        if affected_row == 1:
            return jsonify(register.id)
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    

@main.route("/update-user/<id>", methods=['PUT'])
def update_user(id):
    try:
        _string = request.form['formUser']
        _dict = Tools.convert_json(_string)

        user = _dict['username']
        email = _dict['email']
        password = _dict['password']

        update_register = Register(id, user, email, password)
        affected_row = RegisterModel.update_register(update_register)

        if affected_row == 1:
            return jsonify(update_register.id)
        else:
            return jsonify({"message": "No user updated"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    

@main.route('/delete-user/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        register = Register(id)
        affected_row = RegisterModel.delete_register(register)

        if affected_row == 1:
            return jsonify(register.id)
        else:
            return jsonify({"message": "No user removed"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
