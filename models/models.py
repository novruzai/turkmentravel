from sqlalchemy import *
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime

    
class Banner(Base):
    __tablename__ = 'banner'
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    image = relationship('Image', back_populates='banner')



class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    text = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    answer = relationship('Answer', back_populates='question')


class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey('question.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    question = relationship('Question', back_populates='answer')


class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, nullable=False)
    banner_id = Column(Integer, ForeignKey('banner.id'))
    create_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    banner = relationship('Banner', back_populates='image')