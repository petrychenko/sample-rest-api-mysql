'''
Created on Oct 15, 2013

@author: petrychenko

HTTP Application that process HTTP requests to certain URLs.
See URLs in function @route decorators

'''

import bottle
from bottle import route, request
import json
from controllers import AppController

class ObjectEncoder(json.JSONEncoder):
    """A custom JSONEncoder class that knows how to encode core custom
    objects.

    """
    def default(self, obj):
        if isinstance(obj, object):
            return { obj.__dict__ } 
        else:
            return json.JSONEncoder.default(self, obj)
        
#controller supposed to be stateless so it is safe to have a singleton , one for all users 
controller = AppController();

def _get_json_body():
    request_body_stream = request.body
    body = str(request_body_stream.read(), encoding='UTF-8')
    new_event_dict = json.loads(body)
    return new_event_dict

@route('/users/', method='PUT')
def createUser():
    """ PUT json-encoded user record
    
    format:
     { "email": "petrichenko@gmail.com", "password": "123", "first_name": "Ivan", "last_name": "Petrychenko" }
     first_name and last_name are optional and can be omitted
    """
    controller.createUser( _get_json_body() )
    
@route('/users/<user_id:int>/events/', method='PUT')
def createEvent(user_id):
    """ PUT json-encoded event record
    
    format:
     { "name": "birthday's party", "comment": "white tie DC", "start": 1381878005, "end" : 1382310212, "lon" : 37.322325, "lat" : -122.053828}
     comment is optional and can be omitted
    """
    controller.createEvent( user_id, _get_json_body() )
    
@route('/users/<user_id:int>/events/<event_id:int>/', method='DELETE')
def deleteEvent(user_id, event_id):
    """ deletes event record by id

    no body required
    """
    controller.deleteEvent( user_id, event_id )
    
@route('/users/<user_id:int>/events/queries/delete/', method='POST')
def deleteEvents(user_id):
    """ deletes event records by set of ids

    body shell contain {"ids": [1,2,3] }
    """
    controller.deleteEvents( user_id, _get_json_body()["ids"] )
    
@route('/users/<user_id:int>/events/queries/filter/', method='POST')
def filterEvents(user_id):
    """ returns JSON representation of events that matches posted set of criteria 

    body shell contain only one of geo-filters, polygon or radius. If both are present radius is ignored.
    time constraints represents UNIX epoch time.
        {
        "radius": { 
            "point" :   {"lon" : 37.322325, "lat" : -122.053828},
            "miles" : 10
        },
        "polygon": {
            "points" : [  {"lon" : 37.322325, "lat" : -122.053828},  {"lon" : 37.322325, "lat" : -122.053028},  {"lon" : 37.322025, "lat" : -122.053028}, {"lon" : 37.322025, "lat" : -122.053828} ]
        },
        "timespan" : {
            "start" : 1381805402, 
            "end" : 1384573841 
        }
        
         }
    """
    event_list = controller.filterEvents(user_id, _get_json_body())
    result = []
    for event in event_list:
        result.append(event.__dict__)
    return json.dumps(result, cls= ObjectEncoder)
    
if __name__ == '__main__':
     bottle.run(host="localhost",port=9090, reloader=False, debug=True)
     
