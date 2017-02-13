from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import json

Base = declarative_base()

class School(Base):
    """
    just an example of class, feel free to alter it
    """
    __tablename__ = 'school'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True) # to be uuid
    name = Column(String(100))
    name_alias = Column(String(100))
    rank = relationship('Rank', backref='school')

    def __init__(self, name, name_alias):
        self.name = school_name
        self.name_alias = school_name_alias        

    def __str__(self):
        return json.dumps(self.serialize, indent=4)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {u"id": self.name,
                u"username": self.alias}

class Rank(Base):
    """
    Schema to declare table of requests
    """
    __tablename__ = 'rank'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True) # to be uuid
    value = Column(Integer)
    year = Column(Integer)    
    school_id = Column(Integer, ForeignKey('school.id'))

    def __init__(self, id, year, school_id):
        self.id = id
        self.value = int(value)
        self.year = int(year)
        self.school_id = school_id

    def __str__(self):
        return json.dumps(self.serialize, indent=4)

    def __repr__(self):
        return json.dumps(self.serialize)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {u"id": self.id,
                u"value": self.value,
                u"year": self.year,                
                u"school_id": self.school_id}