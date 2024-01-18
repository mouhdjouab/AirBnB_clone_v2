#!/usr/bin/python3
"""
Database model
"""
# handles the details of connecting to  database
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage():

    """
    Mysql preparation and session
    """
    __engine = None
    __session = None
    def __init__(self):
         __engine = None
    __session = None
    def __init__(self) -> None:
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        db_url = f"mysql+mysqldb://{username}:{password}@{host}/{db_name}"

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        """query on database"""
        if cls is None:
            objct=self.__session.query(State).all()
            objct.extend(self.__session.query(State).all())
            objct.extend(self.__session.query(User).all())
            objct.extend(self.__session.query(Place).all())
            objct.extend(self.__session.query(Review).all())
            objct.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls=eval(cls)
                objct=self.__session.query(cls).all()


        obj_dic = {}
        for obj in objct:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dic[key] = obj
        return obj_dic

    def new(self, obj):
        """ add to db"""
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """
            commit to db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            delete from db
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
            reload
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

