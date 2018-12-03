from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import create_engine
from  flask_cors import CORS


app = Flask(__name__)
api: Api = Api(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



e = create_engine('sqlite:///MyStudents')

parser = reqparse.RequestParser()
parser.add_argument('schueler_id')
parser.add_argument('emailX')
parser.add_argument('usernameX')
parser.add_argument('pictureX')


class SchuelerGetALL(Resource):
    def get(self):
        conn = e.connect()

        query = conn.execute("SELECT * FROM schueler;")
        return {'schueler': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]},200

class Schueler(Resource):
    def get(self):
        conn = e.connect()
        schueler_id = parser.parse_args().schueler_id
        query = conn.execute("select * from schueler where ID='%s';"%schueler_id)
        return {'schueler': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]},200

    def delete(self):
        conn = e.connect()
        schueler_id = parser.parse_args().schueler_id
        query = conn.execute("DELETE from schueler where ID='%s';"%schueler_id)
        return 201


    def put(self):
        conn = e.connect()
        schueler_id = parser.parse_args().schueler_id
        emailX = parser.parse_args().emailX
        usernameX = parser.parse_args().usernameX
        pictureX = parser.parse_args().pictureX
        try:
            query = conn.execute("INSERT INTO schueler VALUES('%s','%s','%s','%s');" % (schueler_id,emailX,usernameX,pictureX))
        except Exception:
            self.update()

        return 201

    def update(self):
        conn = e.connect()
        schueler_id = parser.parse_args().schueler_id
        emailX = parser.parse_args().emailX
        usernameX = parser.parse_args().usernameX
        pictureX = parser.parse_args().pictureX
        query = conn.execute("UPDATE schueler SET email='%s', username='%s', picture='%s' WHERE ID='%s';"%(emailX,usernameX,pictureX,schueler_id))
        return 201


##
## Actually setup the Api resource routing here
##
api.add_resource(Schueler, '/schuelerA')
#api.add_resource(Schueler, '/schueler/<int:schueler_id>')
api.add_resource(SchuelerGetALL, '/schueler')

if __name__ == '__main__':
    app.run(debug=True)
