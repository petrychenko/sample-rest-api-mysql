from model.model_utils import db_backed_mixin, ModelException
from model import filters

class User(db_backed_mixin):
    _table = 'users';
    _id_field = 'id';
    _mandatory_fields = set( ['email', 'password'] )
    _rest_fields = set( ['first_name', 'last_name'] )
    _passwd_fields = ['password']
    _timestamps = []
    events = []
    
    def fillById(self, id):
        super(User,self).fillById( id )
        self.loadEvents()

    def createEvent(self, new_event_dict):
        new_event_dict["user_id"] = self.id 
        event = Event( new_event_dict )
        return event
    
    def loadEvents(self):
        event = Event()
        self.events = event.loadByFilter("user_id=%s", (self.id,) )

    def deleteEvent(self, event_id):
        for event in self.events:
            if event_id == event.id:
                event.delete()
                self.events.remove(event)
                break
        else:
            raise ModelException(self, 'Event not found for id ' + str( event_id ) )

    def deleteEvents(self, event_ids):
        for event in self.events:
            if event.id in event_ids:
                event.delete()
                self.events.remove(event)

    def getEventsByFilter(self, filter_dict):
        filter_func = filters.getFilterByDict(filter_dict)
        result = filter( filter_func, self.events )
        return result   

class Event(db_backed_mixin):
    _table = 'events';
    _id_field = 'id';
    _mandatory_fields = set( ["name",  "user_id", "start", "end", "lon", "lat"] )
    _rest_fields = set( ["comment"] )
    _passwd_fields = []
    _timestamps = ["start", "end"]
    
   
