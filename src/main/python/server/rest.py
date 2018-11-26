from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import create_engine

app = Flask(__name__)
api = Api(app)




e = create_engine('sqlite:///MyStudents.db')

parser = reqparse.RequestParser()
parser.add_argument('task')



class Schueler(Resource):
    def get(self, schueler_id):
        conn = e.connect()
        query = conn.execute("select * from SCHUELER where ID='%s';"%schueler_id)
        return {'schueler': [i[0] for i in query.cursor.fetchall()]},201

    def delete(self, schueler_id):
        conn = e.connect()
        query = conn.execute("DELETE from SCHUELER where ID='%s';" % schueler_id)
        return 204

    def put(self, schueler_id, email, username, picture):
        conn = e.connect()
        query = conn.execute("INSERT INTO SCHUELER (schueler_id,email,username,picture);")
        return 201

    def update(self, schueler_id, emailX, usernameX, pictureX):
        conn = e.connect()
        query = conn.execute("UPDATE SCHUELER SET email=emailX, username=usernameX, picture=pictureX WHERE ID='%s';")
        return 201


##
## Actually setup the Api resource routing here
##
api.add_resource(Schueler, '/schueler/get<int:schueler_id>')
api.add_resource(Schueler, '/schueler/delete<int:schueler_id>')
api.add_resource(Schueler, '/schueler/put<int:schueler_id>')
api.add_resource(Schueler, '/schueler/get<int:schueler_id>')

if __name__ == '__main__':
    app.run(debug=True)
