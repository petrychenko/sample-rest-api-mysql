'''
Created on Oct 15, 2013

@author: av
'''
from abc import ABCMeta, abstractmethod
import math

class GeoPoint():
    earth_radius = 3959
    
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
    def length(self, point2):
        delta_lat = math.radians( self.lat - point2.lat )
        delta_lon = math.radians( self.lon - point2.lon )
        a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.cos(math.radians(self.lat)) \
            * math.cos(math.radians(point2.lat)) * math.sin(delta_lon/2) * math.sin(delta_lon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = self.earth_radius * c
        return distance

    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon
        
class TimeSpan():
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def contains(self, timestamp):    
        return self.start <= timestamp and timestamp < self.end 
    
    def includes(self, timespan2):
        return self.contains(timespan2.start) and self.contains(timespan2.end)
    
        

#abstract
class EventFilter():
    __metaclass__= ABCMeta
    
    @abstractmethod
    def __init__(self, filter_dict): 
        pass
    
    @abstractmethod
    def mathched(self, event):
        """ reference implementation
        
            returns True for any event
        """
        return True
    
    def isIncompatible(self, another_filte):
        False
    
class RadiusFilter( EventFilter ):
    
    def __init__(self, filter_dict):
        self.point = GeoPoint( filter_dict['point']['lat'], filter_dict['point']['lon'] )
        self.radius = filter_dict['miles']
    
    def matched(self, event):
        return self.point.length( GeoPoint( event.lat, event.lon ) ) <= self.radius
              

class PolygonFilter(EventFilter):
    
    def __init__(self, filter_dict):
        self.points = []
        for points_pair in filter_dict['points']:
            self.points.append(GeoPoint(points_pair['lat'],points_pair['lon']))
    
    def matched(self, event):
        n = len(self.points)
        if n < 3:
            return True
        
        inside = False
    
        point1 = self.points[0]
        for i in range(n+1):
            point2 = self.points[i % n]
            if event.lat > min(point1.lat,point2.lat):
                if event.lat <= max(point1.lat,point2.lat):
                    if event.lon <= max(point1.lon,point2.lon):
                        if point1.lat != point2.lat:
                            xints = (event.lat-point1.lat)*(point2.lon-point1.lon)/(point2.lat-point1.lat)+point1.lon
                        if point1.lon == point2.lon or event.lon <= xints:
                            inside = not inside
            point1 = point2
    
        return inside
    
    def isIncompatible(self, another_filter):
        return isinstance( another_filter,  RadiusFilter)

class TimeSpanFilter(EventFilter):
    
    def __init__(self, filter_dict):
        self.timespan = TimeSpan( filter_dict[ 'start' ], filter_dict[ 'end' ])
    
    def matched(self, event):
        event_timespan = TimeSpan( event.start, event.end )
        return self.timespan.includes(event_timespan)
    
_filter_classes = { "radius" : RadiusFilter, "polygon" : PolygonFilter, "timespan" : TimeSpanFilter}

def getFilterByDict( filter_dict ):
    filter_objects = []
    for filter_name in filter_dict.keys():
        filter_class = _filter_classes[filter_name]
        filter_obj = filter_class( filter_dict[filter_name] )
        filter_objects.append( filter_obj )
            
    for filter_obj in filter_objects:
        for another_filter in filter_objects:
            if filter_obj.isIncompatible( another_filter ) :
                filter_objects.remove( another_filter )
    
    def filter_function( event ):
        for filter_obj in filter_objects:
            if not filter_obj.matched( event ):
                return False
        return True
            
    return filter_function


if __name__ == '__main__':
    pass

