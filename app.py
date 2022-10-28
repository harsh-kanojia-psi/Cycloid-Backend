from flask import Flask
from flask_restx import Api
from extensions import db
from Resource.input import saveData, Input

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/cycloid'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'harsh'
api = Api(app)


api.add_resource(saveData, '/inputs')
api.add_resource(Input, '/plot')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    from extensions import db
    db.init_app(app)
    app.run(port=5000, debug=True)


