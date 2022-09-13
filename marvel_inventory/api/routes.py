from operator import methodcaller
import token
from flask import Blueprint, request, jsonify
from marvel_inventory.helpers import token_required
from marvel_inventory.models import db, Marvel, marvel_schema, marvels_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return {'some': 'value'}

#create drone endpoint
@api.route('/marvels', methods = ["POST"])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    description = request.json['description']
    comics_appeared_in = request.json['comics_appeared_in']
    super_power = request.json['super_power']
    user_token = current_user_token.token

    print(f"User token: {current_user_token.token}")
    marvel = Marvel(name, description, comics_appeared_in, super_power, user_token = user_token)

    db.session.add(marvel)
    db.session.commit()

    response = marvel_schema.dump(marvel)

    return jsonify(response)

#retrieve one drone
@api.route('/marvels/<id>', methods = ['GET'])
@token_required
def getCharacter(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        marvel = Marvel.query.get(id)
        response = marvel_schema.dump(marvel)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}), 401


#retrieve all drones
@api.route('/marvels', methods = ['GET'])
@token_required
def getCharacters(current_user_token):
    owner = current_user_token.token
    marvels = Marvel.query.filter_by(user_token = owner).all()
    response = marvels_schema.dump(marvels)
    return jsonify(response)
  
#update drone endpoint
@api.route('/marvels/<id>', methods = ["POST", "PUT"])
@token_required
def update_Characters(current_user_token, id):
    marvel = Marvel.query.get(id)

    marvel.name = request.json['name']
    marvel.description = request.json['description']
    marvel.comics_appeared_in = request.json['comics_appeared_in']
    marvel.super_power = request.json['super_power']
    marvel.user_token = current_user_token.token

    db.session.commit()
    response = marvel_schema.dump(marvel)
    return jsonify(response)

#delete drone endpoint
@api.route('/marvels/<id>', methods = ["DELETE"])
@token_required
def delete_marvel(current_user_token, id):
    marvel = Marvel.query.get(id)

    db.session.delete(marvel)
    db.session.commit()
    response = marvel_schema.dump(marvel)
    return jsonify(response)