#!/usr/bin/env python
#coding: utf8
from sqlalchemy import (
    Column,
    Integer,
    Text,
    )
from sqlalchemy.orm import relationship

from .init import (
    Base,
    DBSession,
    )


class Chapter(Base):
    __tablename__ = 'chapter'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    paragraphs = relationship('Paragraph', backref='chapter')

    @classmethod
    def all(cls):
        return DBSession.query(Chapter).all()

