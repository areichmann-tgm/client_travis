from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import create_engine

app = Flask(__name__)
api: Api = Api(app)




e = create_engine('sqlite:///MyStudents.db')

parser = reqparse.RequestParser()
parser.add_argument('task')



class Schueler(Resource):
    def get(self):
        conn = e.connect()
        parser = reqparse.RequestParser()
        parser.add_argument('ID',type = int, location='args')
        schueler_id = parser.parse_args().ID
        query = conn.execute("select * from SCHUELER where ID='%s';"%schueler_id)
        return {'schueler': [i[0] for i in query.cursor.fetchall()]},201

    def delete(self):
        conn = e.connect()
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=int, location='args')
        schueler_id = parser.parse_args().ID
        query = conn.execute("DELETE from SCHUELER where ID='%s';"%schueler_id)
        return 204


    def put(self):
        conn = e.connect()
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        query = conn.execute("INSERT INTO SCHUELER (schueler_idX,emailX,usernameX,pictureX);")
        return 201

    def update(self):
        conn = e.connect()
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=int, location='args')
        parser.add_argument('email',type=str,location='args')
        parser.add_argument('username',type=str,location='args')
        parser.add_argument('picture',type=str,location='args')
        schueler_id = parser.parse_args().ID
        usernameX = parser.parse_args().username
        emailX = parser.parse_args().email
        query = conn.execute("UPDATE SCHUELER SET email=emailX, username=usernameX, picture=pictureX WHERE ID='%s';"%schueler_id)
        return 201


##
## Actually setup the Api resource routing here
##
api.add_resource(Schueler, '/schueler/get/<params>')


if __name__ == '__main__':
    app.run(debug=True)
