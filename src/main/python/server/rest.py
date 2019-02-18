import sqlite3

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import create_engine
from  flask_cors import CORS
#from flask_oauth import OAuth
import json

'''oauth = OAuth()
the_remote_app = oauth.remote_app('the remote app',
    ...
)'''


app = Flask(__name__)
api: Api = Api(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def create():
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS schueler (
 id INTEGER PRIMARY KEY,
 name VARCHAR NOT NULL,
 email VARCHAR,
 bild VARCHAR
);""")
        conn.execute("DELETE FROM schueler;")
    except:
        pass

def insert():
    conn.execute("INSERT INTO schueler (id, name, email, bild) values('1000', 'Adrian', 's1@microgreen.com', 'NO_PIC')")
    conn.execute("INSERT INTO schueler (id, name, email, bild) values('1001', 'Adrian', 's1@microgreen.com', 'NO_PIC')")


db_path = r'MyStudents.db'
connt = sqlite3.connect(db_path)
conn = connt.cursor()
create()
insert()
connt.commit()


parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('email')
parser.add_argument('name')
parser.add_argument('bild')


class SchuelerGetALL(Resource):
    def get(self):
        connt = sqlite3.connect(db_path)
        conn = connt.cursor()

        query = conn.execute("SELECT * FROM schueler;")
        users = query.fetchall()
        userOut = []
        for i in range(len(users)):
            user = {"id": users[i][0], "email": users[i][1], "name": users[i][2], "bild": users[i][3]}
            userOut.append(user)
        json_with_quotes = json.dumps(userOut)
        return json.loads(json_with_quotes), 200

class Schueler(Resource):

    def get(self):
        connt = sqlite3.connect(db_path)
        conn = connt.cursor()

        id = parser.parse_args().id
        query = conn.execute("select t.* from schueler t where id='%s';"%id)
        users = query.fetchall()
        for i in range(len(users)):
            user = {"id": users[i][0], "email": users[i][1], "name": users[i][2], "bild": users[i][3]}
        json_with_quotes = json.dumps(user)
        return json.loads(json_with_quotes), 200

    def delete(self):
        connt = sqlite3.connect(db_path)
        conn = connt.cursor()
        id = parser.parse_args().id
        query = conn.execute("DELETE from schueler where id='%s';"%id)
        return 201


    def put(self):
        connt = sqlite3.connect(db_path)
        conn = connt.cursor()

        id = parser.parse_args().id
        email = parser.parse_args().email
        name = parser.parse_args().name
        bild = parser.parse_args().bild
        try:
            query = conn.execute("INSERT INTO schueler VALUES('%s','%s','%s','%s');" % (id,email,name,bild))
        except Exception:
            """"""
            self.update()

        return 201

    def update(self):

        id = parser.parse_args().id
        email = parser.parse_args().email
        name = parser.parse_args().name
        bild = parser.parse_args().bild
        query = conn.execute("UPDATE schueler SET email='%s', name='%s', bild='%s' WHERE id='%s';"%(email,name,bild,id))
        return 201


##
## Actually setup the Api resource routing here
##
api.add_resource(Schueler, '/schuelerA')
#api.add_resource(Schueler, '/schueler/<int:schueler_id>')
api.add_resource(SchuelerGetALL, '/schueler')

if __name__ == '__main__':
    app.run(debug=True)
