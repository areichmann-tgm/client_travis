from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

schueler = {
    'abc@efg.hij': {'id':'1','username':"mmatouschek", 'picture':"https://www.xing.com/assets/frontend_minified/img/users/nobody_m.256x256.jpg"},
    'schueler2':{'id':'2','username':"areichmann", 'email':"abc@efg.hij", 'picture':"https://www.xing.com/assets/frontend_minified/img/users/nobody_m.256x256.jpg"},
    'schueler3':{'id':'3','username':"oiner", 'email':"abc@efg.hij", 'picture':"https://www.xing.com/assets/frontend_minified/img/users/nobody_m.256x256.jpg"}
}


def abort_if_schueler_doesnt_exist(schueler_id):
    if schueler_id not in schueler:
        abort(404, message="Schueler doesn't exist".format(schueler_id))

parser = reqparse.RequestParser()
parser.add_argument('task')



class Schueler(Resource):
    def get(self, schueler_id):
        abort_if_schueler_doesnt_exist(schueler_id)
        return schueler[schueler_id]

    def delete(self, schueler_id):
        abort_if_schueler_doesnt_exist(schueler_id)
        del schueler[schueler_id]
        return '', 204

    def put(self, schueler_id):
        args = parser.parse_args()
        task = {'schueler': args['schueler']}
        schueler[schueler_id] = task
        return task, 201


class SchuelerList(Resource):
    def get(self):
        return schueler

    def post(self):
        args = parser.parse_args()
        schueler_id = int(max(schueler.keys()).lstrip('schueler')) + 1
        schueler_id = 'Schueler%i' % schueler_id
        schueler[schueler_id] = {'task': args['task']}
        return schueler[schueler_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(SchuelerList, '/schuelerlist')
api.add_resource(Schueler, '/schuelerlist/<schueler_id>')


if __name__ == '__main__':
    app.run(debug=True)
