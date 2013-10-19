from model.domain import User

class ApplicationException(Exception):
    pass

class AppController():
    """ Application controller (facade) that provides business logic operations
    """

    def _getUser(self, user_id):
        user = User()
        user.fillById(user_id)
        if not user.id:
            raise ApplicationException('User not found for id ' + str(user_id))
        return user

    def createUser(self, new_user_dict):
        user = User( new_user_dict )
        user.save()
        return user.id

    def createEvent(self, user_id, new_event_dict):
        user = self._getUser(user_id)
        event = user.createEvent(new_event_dict)
        event.save()
    
    def deleteEvent(self, user_id, event_id):
        user = self._getUser(user_id)
        user.deleteEvent( event_id )
    
    def deleteEvents(self, user_id, event_ids):
        user = self._getUser(user_id)
        user.deleteEvents(event_ids)
    
    def filterEvents(self, user_id, filter_dict):
        user = self._getUser(user_id)
        result = user.getEventsByFilter( filter_dict )
        return result
    
    
    
        
        
    
    
        
    
    
    
    
    



