from flask import jsonify
from flask_restful import Resource,reqparse
from db import cursor,encode

class Tracking(Resource):
    def get(self):
        cursor.execute(f'''SELECT * FROM Rawdata''')
        result=encode(cursor.fetchall())
        return jsonify(result)
