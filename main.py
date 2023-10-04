from flask import Flask, request, jsonify
from flask_restful import Api, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class CardModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    meaning = db.Column(db.String(300),nullable=False)
    image = db.Column(db.String(500), nullable=False)


resource_fields = {
     'id': fields.Integer,
     'name': fields.String,
     'meaning' : fields.String,
     'image' : fields.String
}


class TarotCards(Resource):
    @marshal_with(resource_fields)
    def get(self, id=None):
        if id is not None:
            result = CardModel.query.filter_by(id=id).first()
        else:
            result = CardModel.query.all()
        return result

api.add_resource(TarotCards, "/", "/tarotcards", "/tarotcards/<string:id>")


with app.app_context():
    for card_name, card_info in cards.items():
        card = CardModel(name=card_name, meaning=card_info['meaning'], image=card_info['image'])
        db.session.add(card)
    db.session.commit()

with app.app_context():
    instances_to_delete = CardModel.query.filter(CardModel.id.between(79, 312)).all()

    for instance in instances_to_delete:
        db.session.delete(instance)

    db.session.commit()

if __name__ == "__main__":
    app.run(port=8000, debug=True)


