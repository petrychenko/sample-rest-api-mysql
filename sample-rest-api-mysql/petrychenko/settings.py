_db = None

import mysql.connector

def getDBConn():
    """ TODO: place conn params in the separate conf file
        TODO: add pool name to introduce pooling
    """
    return mysql.connector.MySQLConnection(user='upout',password='upout',host='localhost',database='upout_test')


