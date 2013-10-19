import settings

class ModelException(Exception):
    def __init__(self, db_backed_mixin, msg):
        super(ModelException,self).__init__(str(db_backed_mixin.__class__)+" id = " + str( db_backed_mixin.__dict__[db_backed_mixin._id_field])+": "+msg)

class MandatoryFieldsAbsent(Exception):
    pass

class db_backed_mixin():
    # you need to override those fields:
    _table = None
    _id_field = None
    _mandatory_fields = set()
    _rest_fields = set()
    _passwd_fields = []
    _timestamps = []
        
    def __init__(self, new_dict=None):
        self.id = None
        if not new_dict:
            return
        
        #test if all mandatory fields are in
        new_fields = set( new_dict ) 
        
        if not self._mandatory_fields.issubset( new_fields ):
            diff_set = self._mandatory_fields.difference( self._mandatory_fields & new_fields  )
            raise MandatoryFieldsAbsent("Mandatory fields are absent: " + str(diff_set) )
        
        for mfield in self._mandatory_fields:
            self.__dict__[mfield] = new_dict[mfield]
            
        for rfield in self._rest_fields:
            if rfield in new_dict.keys() :
                self.__dict__[rfield] = new_dict[rfield]

    def update(self):
        #ToDo: implement
        pass
    
    def save(self):
        if( self.id ):
            self.update()
        else:
            self.insert()
            
    def _pairs(self, field_names):
        str_sql = ''
        for field in field_names:
            if field in self._passwd_fields:
                str_sql += field+"=PASSWORD(%("+field+")s), "
            elif field in self._timestamps:
                str_sql += field+"=FROM_UNIXTIME(%("+field+")s), "
            else:
                str_sql += field+"=%("+field+")s, " 
        str_sql = str_sql[0:-2]
        return str_sql
    
    def _field_list_str(self, field_names):
        str_sql = ''
        for field in field_names:
            if field in self._timestamps:
                str_sql += "UNIX_TIMESTAMP("+field+"), "
            else:
                str_sql += field+", " 
        str_sql = str_sql[0:-2]
        return str_sql   
    
    def _non_empty_fields(self):
        return  self._mandatory_fields | ( set(self.__dict__) & self._rest_fields )
    
    def _insert_sql(self):
        strsql = "INSERT INTO "+self._table+" SET "+self._pairs( self._non_empty_fields() )
        print( strsql )
        return strsql

    def _all_possible_fields(self):
        return [ self._id_field ] + list( self._mandatory_fields ) + list( self._rest_fields )
    
    def _select_sql(self):
        return "SELECT " +self._field_list_str( self._all_possible_fields() ) +" FROM " + self._table 

    def _select_by_id_sql(self):
        return self._select_sql() + " WHERE "+self._id_field+"=%s"
        
    def insert(self):
        conn = settings.getDBConn()
        cursor = conn.cursor()
        cursor.execute(self._insert_sql(), self.__dict__ )
        self.id =  cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()  
    
    def fillById(self, id):
        conn = settings.getDBConn()
        cursor = conn.cursor()
        cursor.execute(self._select_by_id_sql(), (id,) )
        for row in cursor:
            i=0;
            for field in self._all_possible_fields():
                self.__dict__[field] = row[i]
                i+=1
        cursor.close()
        conn.close()
        
    def delete(self):
        conn = settings.getDBConn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM "+self._table+" WHERE "+self._id_field+"=%s", (self.__dict__[self._id_field],) )
        conn.commit()
        cursor.close()
        conn.close()
        
    def loadByFilter(self, where_clause, params_tuple):
        str_sql = self._select_sql() +" WHERE "+ where_clause
        conn = settings.getDBConn()
        cursor = conn.cursor()
        cursor.execute(str_sql, params_tuple )
        result = []
        for row in cursor:
            new_obj = self.__class__()
            i=0;
            for field in self._all_possible_fields():
                new_obj.__dict__[field] = row[i]
                i+=1
            result.append(new_obj)
        cursor.close()
        conn.close()
        return result
        
    
    
