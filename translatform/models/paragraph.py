#!/usr/bin/env python
#coding: utf8
import datetime
import hashlib
from sqlalchemy import (
    Column,
    Integer,
    String,
    UnicodeText,
    DateTime,
    ForeignKey,
    )
from sqlalchemy.orm import relationship

from .init import (Base, DBSession)
from ..utils.rst import (clean_format, md5, clean_space)


class Paragraph(Base):
    __tablename__ = 'paragraph'
    id = Column(Integer, primary_key=True)
    english = Column(UnicodeText, nullable=False)
    plain_text = Column(UnicodeText, nullable=False)
    identity = Column(String(32), index=True, nullable=False)
    translations = relationship('ParagraphTranslation',
                               backref='english')
    comments = relationship('ParagraphComment',
                            backref='paragraph')
    chap_id = Column(ForeignKey('chapter.id'), nullable=False)

    def __init__(self, english, translations=[], comments=[]):
        self.english = english
        self.plain_text = clean_format(english)
        self.translations = translations
        self.comments = comments
        self.identity = md5(clean_space(self.plain_text))

    def latest_translation(self):
        translations = self.translations
        return translations[-1].translation if translations else ''

    def add_translation(self, translation):
        t = ParagraphTranslation(author='system',
                                 translation=translation,
                                 para_id=self.id)
        DBSession.add(t)

    def all_translations(self):
        translations = DBSession.query(ParagraphTranslation).filter_by(para_id=self.id).order_by('id desc').all()
        return [t.translation for t in translations]


class ParagraphTranslation(Base):
    __tablename__ = 'paragraph_translation'
    id = Column(Integer, primary_key=True)
    author = Column(UnicodeText, nullable=False)
    time = Column(DateTime, default=datetime.datetime.now)
    translation = Column(UnicodeText, nullable=False)
    para_id = Column(ForeignKey('paragraph.id'), nullable=False)


class ParagraphComment(Base):
    __tablename__ = 'paragraph_comment'
    id = Column(Integer, primary_key=True)
    author = Column(UnicodeText, nullable=False)
    time = Column(DateTime, default=datetime.datetime.now)
    comment = Column(UnicodeText, nullable=False)
    para_id = Column(ForeignKey('paragraph.id'), nullable=False)
