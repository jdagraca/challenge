from mongoengine import *
from src.utils.enviroment import Enviroment


class ConexionDB:
    db_client = None
    session = None
    host = None
    db = None

    @staticmethod
    def get_db():
        if ConexionDB.db_client is None:
            dbuser = Enviroment.get_variable("dbuser")
            dbpassword = Enviroment.get_variable("dbpassword")
            host = Enviroment.get_variable("host")
            dbport = int(Enviroment.get_variable("dbport"))
            db = Enviroment.get_variable("dbname")
            ConexionDB.db_client = connect(host=f"mongodb://{host}:{dbport}/{db}")

        return ConexionDB.db_client

    @staticmethod
    def close():
        if ConexionDB.db_client is not None:
            ConexionDB.db_client.close()

    @staticmethod
    def dropdb():
        if ConexionDB.db_client is not None:
            db = Enviroment.get_variable("dbname")
            ConexionDB.db_client.drop_database(db)
