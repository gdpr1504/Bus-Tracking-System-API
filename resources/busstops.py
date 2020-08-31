from flask import jsonify
from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required,get_jwt_claims
from db import query
from decimal import Decimal

class BusStops(Resource):
    @jwt_required
    def post(self):
        vendorid=get_jwt_claims()['vendorid']
        parser=reqparse.RequestParser()
        parser.add_argument('routeId',type=int,required=True,help="routeId cannot be left blank!")
        parser.add_argument('busStopName',type=str,required=True,help="busStopName cannot be left blank!")
        parser.add_argument('latitude',type=str,required=True,help="latitude cannot be left blank!")
        parser.add_argument('longitude',type=str,required=True,help="longitude cannot be left blank!")
        parser.add_argument('busStopNum',type=int,required=True,help="busStopNum cannot be left blank!")
        data=parser.parse_args()
        try:
            imei=query(f"""SELECT IMEI FROM Bus WHERE routeId={data['routeId']} AND vendorId={vendorid}""",return_json=False)
            if len(imei)==0: return {"message":"Invalid routeId!"}, 404
            query(f"""INSERT INTO BusStops (routeId,busStopName,latitude,longitude,busStopNum)
                                    VALUES ({data['routeId']},'{data['busStopName']}',{Decimal(data['latitude'])},
                                            {Decimal(data['longitude'])},{data['busStopNum']})""")
        except:
            return {"message": "An error occurred while updating."}, 500
        return {"message": "BusStop created successfully."}, 201

    @jwt_required
    def delete(self):
        vendorid=get_jwt_claims()['vendorid']
        parser=reqparse.RequestParser()
        parser.add_argument('routeId',type=int,required=True,help="routeId cannot be left blank!")
        parser.add_argument('busStopNum',type=int,required=True,help="busStopNum cannot be left blank!")
        data=parser.parse_args()
        try:
            check=query(f"""SELECT bs.* FROM BusStops bs, Bus b
                            WHERE bs.routeId=b.routeId AND bs.routeId={data['routeId']} AND
                                  busStopNum={data['busStopNum']} AND b.vendorId={vendorid}""",return_json=False)
            if len(check)==0: return {"message" : "No such BusStop found."}, 404
            query(f"""DELETE FROM BusStops WHERE routeId={data['routeId']} AND busStopNum={data['busStopNum']}""")
        except:
            return {"message" : "An error occurred while deleting."}, 500
        return {"message" : "Deleted successfully."}, 200

    @jwt_required
    def get(self):
        vendorid=get_jwt_claims()['vendorid']
        parser=reqparse.RequestParser()
        parser.add_argument('routeId',type=string)
        data=parser.parse_args()
        routeId=int(data['routeId'])
        if data['routeId']==None:
            try:
                routeids=query(f"""SELECT DISTINCT bs.routeId FROM BusStops bs, Bus b
                                   WHERE bs.routeId=b.routeId AND b.vendorId={vendorid}""",return_json=False)
                routeids=[x['routeId'] for x in routeids]
                result={}
                for i in routeids:
                    busstops=query(f"""SELECT busStopNum,busStopName,latitude,longitude FROM BusStops
                                       WHERE routeId={i} ORDER BY busStopNum""",return_json=False)
                    result[i]=busstops
                return jsonify(result)
            except:
                return {"message" : "An error occurred while accessing BusStops table."}, 500
        else:
            try:
                return query(f"""SELECT busStopNum,busStopName,latitude,longitude FROM BusStops bs, Bus b
                                 WHERE bs.routeId=b.routeId AND bs.routeId={routeId} AND b.vendorId={vendorid}
                                 ORDER BY busStopNum""")
            except:
                return {"message" : "An error occurred while accessing BusStops table."}, 500
