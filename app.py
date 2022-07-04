from db import db
from flask import Flask
from flask_restful import Api
from resources import Import, Export
from service.utils.create_view import delta_view

app = Flask(__name__)
app.config.from_object("config.DevConfig")
api = Api(app)
db.init_app(app)

with app.app_context():
    db.create_all()
    db.engine.execute(delta_view)

api.add_resource(Import, "/import/xlsx")
api.add_resource(Export, "/export/<string:property>")


if __name__ == "__main__":
    app.run(port=5001, debug=True)
