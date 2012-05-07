#!/usr/bin/env python
#coding: utf8
import os

from sqlalchemy import (
    Column,
    Integer,
    UnicodeText,
    Boolean,
    ForeignKey,
    )
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from .init import (
    Base,
    DBSession,
    )


class Chapter(Base):
    __tablename__ = 'chapter'
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText, nullable=False, index=True)
    title = Column(UnicodeText)
    body = Column(UnicodeText, default=u'', nullable=False)
    toc = Column(UnicodeText)
    display_toc = Column(Boolean)
    current_page_name = Column(UnicodeText)
    parents = Column(UnicodeText)
    prev = Column(UnicodeText)
    next = Column(UnicodeText)
    sourcename = Column(UnicodeText, nullable=False)

    paragraphs = relationship('Paragraph', backref='chapter')

    def __init__(self, title, body, toc, display_toc, current_page_name, parents, prev, next, sourcename, paragraphs=[]):
        self.title = title
        self.body = body
        self.toc = toc
        self.display_toc = display_toc
        self.current_page_name = current_page_name
        self.parents = parents
        self.prev = prev
        self.next = next
        self.sourcename = sourcename
        self.paragraphs = paragraphs
        self.name = os.path.splitext(self.sourcename)[0]

    @classmethod
    def all(cls):
        return DBSession.query(Chapter).all()
