#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User, Base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adding new user to table"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """Finding user by params"""
        if not kwargs:
            return InvalidRequestError

        cols_keys = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in cols_keys:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updating user"""
        if not kwargs:
            return None

        user = self.find_user_by(id=user_id)

        cols_keys = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in cols_keys:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()

        for key, value in kwargs.items():
            setattr(user, key, value)
        

        self._session.commit()
