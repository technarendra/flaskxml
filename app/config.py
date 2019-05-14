import os
from datetime import timedelta
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import datetime

#application directory
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DB_CONFIG = {
        'host': 'localhost',
        'port': '5432',
        'database': 'mydatabase',
        'user': 'narendra',
        'password': 'root',
    }

    # class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s" % DB_CONFIG
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    #secret key for signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"





# #application directory
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
#
#
# engine = create_engine('sqlite:///database.db', echo=True)
# Base = declarative_base()
#
#
# ########################################################################
# class User(Base):
#     """"""
#     __tablename__ = "user"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     country = Column('country', String(20), unique=True , index=True)
#     rank = Column('rank', String(10), nullable=False)
#     year = Column('year', String(50),unique=True , index=True, nullable=False)
#     neighbor = Column('neighbor', String(50),unique=True , index=True, nullable=False)
#     active = Column(Boolean(), nullable=False, server_default='0')
#
#     def get_id(self):
#         return unicode(self.alternative_id)
#
# #----------------------------------------------------------------------
# def __init__(self , country ,rank , year, neighbor):
#     self.country = country
#     self.rank = rank
#     self.year = year
#     self.neighbor = neighbor
#     self.registered_on = datetime.utcnow()
#
#
#
# # create tables
# Base.metadata.create_all(engine)
#
#
# #application directory
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
#
#
# class Config(object):
#     # DB_CONFIG = {
#     #     'host': 'localhost',
#     #     'port': '5432',
#     #     'database': 'postgres',
#     #     'user': 'postgres',
#     #     'password': 'p05tgre5',
#     # }
#
#     # class Config(object):
#     SQLALCHEMY_DATABASE_URI = 'sqlite://////home/narendra/narendra/xmlflaskpro/database.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     # Enable protection agains *Cross-site Request Forgery (CSRF)*
#     CSRF_ENABLED = True
#
#     #secret key for signing the data.
#     CSRF_SESSION_KEY = "secret"
#
#     # Secret key for signing cookies
#     SECRET_KEY = "thisissecretkey"
#
#     USER_ENABLE_EMAIL = False
#
#     USE_SESSION_FOR_NEXT = True
#
#     REMEMBER_COOKIE_DURATION = timedelta(seconds=90)